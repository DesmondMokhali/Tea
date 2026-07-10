/**
 * Tangren Herbal Teas — Secure Checkout Edge Function
 * 
 * Deployed to: Supabase Edge Functions
 * Invoked by:  index.html -> fetch('/functions/v1/checkout', ...)
 *
 * Security guarantees:
 *  ① Accepts only IDs + quantities from the browser — never trusts browser prices
 *  ② Fetches authoritative prices directly from the Supabase DB (bypasses RLS via service role)
 *  ③ Calculates the tamper-proof order total on the server
 *  ④ Forwards the clean, signed payload to Make.com via a secret env variable
 *
 * Environment variables (set in Supabase Dashboard → Settings → Edge Functions):
 *   SUPABASE_URL             — your project URL  (auto-injected by Supabase)
 *   SUPABASE_SERVICE_ROLE_KEY — secret admin key  (auto-injected by Supabase)
 *   MAKE_WEBHOOK_URL         — https://hook.eu1.make.com/gjgs9if1449mylxmt44hxc1n9rv1535n
 */

import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

// ── CORS headers (allow requests from your GitHub Pages domain) ──────────────
const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "https://desmondmokhali.github.io",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
};

const FREE_SHIPPING_THRESHOLD = 500;
const SHIPPING_FEE = 75;

serve(async (req: Request) => {
  // Handle preflight CORS request
  if (req.method === "OPTIONS") {
    return new Response(null, { status: 204, headers: CORS_HEADERS });
  }

  if (req.method !== "POST") {
    return new Response(
      JSON.stringify({ error: "Method not allowed" }),
      { status: 405, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } }
    );
  }

  try {
    // ── Parse incoming browser payload ────────────────────────────────────────
    const body = await req.json();
    const { clientCart, tracking_id, delivery_profile } = body;

    if (!clientCart || !Array.isArray(clientCart) || clientCart.length === 0) {
      return new Response(
        JSON.stringify({ error: "Cart is empty or malformed." }),
        { status: 400, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } }
      );
    }

    // ── Init Supabase admin client (service role bypasses RLS) ───────────────
    const supabase = createClient(
      Deno.env.get("SUPABASE_URL")!,
      Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!
    );

    // ── 🛡️ SECURITY STEP 1: Extract only IDs from the browser payload ─────────
    // The browser sends item_type ('single' | 'bundle'), database_id, and quantity.
    // We NEVER trust any price value sent from the browser.
    const productIds = clientCart
      .filter((i: any) => i.item_type === "single" && i.database_id)
      .map((i: any) => i.database_id);

    const bundleIds = clientCart
      .filter((i: any) => i.item_type === "bundle" && i.database_id)
      .map((i: any) => i.database_id);

    // ── 🛡️ SECURITY STEP 2: Query authoritative prices from Supabase ─────────
    const [productsResult, bundlesResult] = await Promise.all([
      productIds.length > 0
        ? supabase.from("products").select("id, retail_price, name").in("id", productIds)
        : Promise.resolve({ data: [], error: null }),
      bundleIds.length > 0
        ? supabase.from("bundles").select("id, retail_price, name").in("id", bundleIds)
        : Promise.resolve({ data: [], error: null }),
    ]);

    if (productsResult.error) throw new Error(`Products DB error: ${productsResult.error.message}`);
    if (bundlesResult.error)  throw new Error(`Bundles DB error: ${bundlesResult.error.message}`);

    const dbProducts: any[] = productsResult.data || [];
    const dbBundles:  any[] = bundlesResult.data  || [];

    // ── 🛡️ SECURITY STEP 3: Compute tamper-proof total on the server ─────────
    let subtotal = 0;
    const resolvedLineItems: any[] = [];

    for (const cartItem of clientCart) {
      const qty = Math.max(1, parseInt(cartItem.quantity, 10) || 1);

      if (cartItem.item_type === "single") {
        const match = dbProducts.find((p) => p.id === cartItem.database_id);
        if (!match) {
          return new Response(
            JSON.stringify({ error: `Product not found: ${cartItem.database_id}` }),
            { status: 400, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } }
          );
        }
        const lineTotal = parseFloat((match.retail_price * qty).toFixed(2));
        subtotal += lineTotal;
        resolvedLineItems.push({
          bundle_id: null,
          product_id: match.id,
          product_name: match.name,
          quantity: qty,
          unit_price: match.retail_price,
          line_total: lineTotal,
        });

      } else if (cartItem.item_type === "bundle") {
        const match = dbBundles.find((b) => b.id === cartItem.database_id);
        if (!match) {
          return new Response(
            JSON.stringify({ error: `Bundle not found: ${cartItem.database_id}` }),
            { status: 400, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } }
          );
        }
        const lineTotal = parseFloat((match.retail_price * qty).toFixed(2));
        subtotal += lineTotal;
        resolvedLineItems.push({
          bundle_id: match.id,
          product_id: null,
          product_name: match.name,
          quantity: qty,
          unit_price: match.retail_price,
          line_total: lineTotal,
        });
      }
    }

    // Calculate shipping server-side — cannot be influenced by the browser
    const shippingFee = subtotal >= FREE_SHIPPING_THRESHOLD ? 0 : SHIPPING_FEE;
    const orderTotal  = parseFloat((subtotal + shippingFee).toFixed(2));

    // ── 🛡️ SECURITY STEP 4: Build the final clean payload ────────────────────
    const cleanPayload = {
      tracking_id:      tracking_id || `ORD-SECURE-${Date.now()}`,
      delivery_profile: delivery_profile || {},
      line_items:       resolvedLineItems,
      shipping_fee:     shippingFee,
      order_total:      orderTotal,   // ← tamper-proof, computed server-side
      checkout_timestamp: new Date().toISOString(),
    };

    console.log("[Checkout] Clean payload dispatched:", JSON.stringify(cleanPayload));

    // ── Dispatch to Make.com via secret env variable ──────────────────────────
    const makeWebhookUrl = Deno.env.get("MAKE_WEBHOOK_URL");
    if (!makeWebhookUrl) throw new Error("MAKE_WEBHOOK_URL environment variable not set.");

    const makeResponse = await fetch(makeWebhookUrl, {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify(cleanPayload),
    });

    if (!makeResponse.ok) {
      throw new Error(`Make.com pipeline failed with status ${makeResponse.status}`);
    }

    return new Response(
      JSON.stringify({
        success: true,
        tracking_id: cleanPayload.tracking_id,
        order_total:  orderTotal,
        message:     "Order authenticated and processed successfully.",
      }),
      { status: 200, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } }
    );

  } catch (error: any) {
    console.error("[Checkout] Secure checkout error:", error.message);
    return new Response(
      JSON.stringify({ error: "Internal server security error. Please try again." }),
      { status: 500, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } }
    );
  }
});
