import { serve } from "https://deno.land/std@0.168.0/http/server.ts"
import { createClient } from "https://esm.sh/@supabase/supabase-js@2"

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}

// Add this bundle slug-to-ID lookup map at the top of your handler
const BUNDLE_ID_MAP: Record<string, number> = {
  "high-performance-engine": 1,
  "metabolic-weight-flush": 2,
  "stress-anxiety-mood-fortress": 3,
  "sinus-respiratory-shield": 4,
  "alpha-male-vitality": 5,
  "whole-body-longevity": 6,
  "womb-wellness-cycle": 7,
  "deep-systemic-detox": 8,
  "gastric-reflux-gut-harmony": 9,
  "golden-years-joint-mobility": 10,
  "joint-mobility-rescue": 10,
  "screen-time-eye-strain": 11,
  "blood-sugar-craving-control": 12,
  "advanced-cystic-acne": 13,
  "vascular-blood-pressure": 14,
  "weekend-recovery": 15
};

serve(async (req) => {
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
  }

  try {
    const body = await req.json()
    const { clientCart, tracking_id, delivery_profile, shipping_fee } = body

    // ── Validate incoming payload ───────────────────────────────────────────
    if (!Array.isArray(clientCart) || clientCart.length === 0) {
      throw new Error('clientCart is empty or missing. No items to process.')
    }

    // Every item must have database_id and item_type
    const malformed = clientCart.filter((i: any) => !i.database_id || !i.item_type)
    if (malformed.length > 0) {
      throw new Error(
        `clientCart contains ${malformed.length} item(s) missing database_id or item_type: ` +
        JSON.stringify(malformed)
      )
    }

    const serviceRoleKey = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? '';
    const supabaseUrl = Deno.env.get('SUPABASE_URL') ?? '';

    if (!serviceRoleKey) {
      console.error('[checkout] SUPABASE_SERVICE_ROLE_KEY environment variable is not defined!');
      throw new Error('Server environment is misconfigured: Admin authorization key is missing.');
    }

    const supabaseAdmin = createClient(supabaseUrl, serviceRoleKey)

    // ── Extract SKUs and bundle identifiers from the cart ───────────────────
    const productCodes = clientCart
      .filter((i: any) => i.item_type === 'single')
      .map((i: any) => i.database_id)

    const bundleCodes = clientCart
      .filter((i: any) => i.item_type === 'bundle')
      .map((i: any) => i.database_id)

    // ── Fetch matching rows from Supabase ───────────────────────────────────
    const { data: dbProducts, error: productError } = await supabaseAdmin
      .from('products')
      .select('external_id, title, retail_price')
      .in('external_id', productCodes.length > 0 ? productCodes : ['__none__'])

    if (productError) throw new Error(`Supabase products query failed: ${productError.message}`)

    // Map of bundle slug names to their corresponding database integer IDs
    const BUNDLE_SLUG_TO_ID: Record<string, number> = {
      'high-performance-engine': 1,
      'metabolic-weight-flush': 2,
      'stress-anxiety-fortress': 3,
      'stress-anxiety-mood-fortress': 3,
      'sinus-respiratory-shield': 4,
      'alpha-male-vitality': 5,
      'longevity-organ-shield': 6,
      'whole-body-longevity': 6,
      'womb-wellness-ritual': 7,
      'womb-wellness-cycle': 7,
      'detox-liver-flush': 8,
      'deep-systemic-detox': 8,
      'gastric-reflux-harmony': 9,
      'gastric-reflux-gut-harmony': 9,
      'golden-years-mobility': 10,
      'golden-years-joint-mobility': 10,
      'joint-mobility-rescue': 10,
      'screen-time-eye-strain': 11,
      'blood-sugar-craving-control': 12,
      'cystic-acne-skin-ritual': 13,
      'advanced-cystic-acne': 13,
      'vascular-blood-pressure': 14,
      'weekend-recovery': 15
    };

    const getBundleId = (id: any): number | null => {
      if (typeof id === 'number') return id;
      const num = Number(id);
      if (!isNaN(num)) return num;
      return BUNDLE_SLUG_TO_ID[id] ?? null;
    };

    const bundleIds = bundleCodes
      .map(getBundleId)
      .filter((id): id is number => id !== null);

    // Fetch all bundles matching the resolved integer IDs
    const { data: dbBundles, error: bundleError } = await supabaseAdmin
      .from('bundles')
      .select('id, title, bundle_retail_price')
      .in('id', bundleIds.length > 0 ? bundleIds : [-1])

    if (bundleError) throw new Error(`Supabase bundles query failed: ${bundleError.message}`)

    // ── Calculate verified server-side order total ──────────────────────────
    let calculatedOrderTotal = 0
    const pricedLineItems: any[] = []

    for (const cartItem of clientCart) {
      if (cartItem.item_type === 'single') {
        const match = dbProducts?.find((p: any) => p.external_id === cartItem.database_id)
        if (!match) {
          console.error(`[checkout] No product found for external_id="${cartItem.database_id}". Check Supabase products table.`)
          throw new Error(`Product not found in database: "${cartItem.database_id}". Order cannot be completed.`)
        }
        const lineTotal = match.retail_price * cartItem.quantity
        calculatedOrderTotal += lineTotal
        pricedLineItems.push({
          item_type:   'single',
          database_id: cartItem.database_id,
          title:       match.title || match.name,
          unit_price:  match.retail_price,
          quantity:    cartItem.quantity,
          line_total:  lineTotal
        })

      } else if (cartItem.item_type === 'bundle') {
        const intId = getBundleId(cartItem.database_id)
        if (!intId) {
          throw new Error(`Invalid bundle identifier: "${cartItem.database_id}".`)
        }
        const match = dbBundles?.find((b: any) => b.id === intId)
        if (!match) {
          console.error(`[checkout] No bundle found for id=${intId} (slug="${cartItem.database_id}"). Check Supabase bundles table.`)
          throw new Error(`Bundle not found in database: "${cartItem.database_id}". Order cannot be completed.`)
        }
        const lineTotal = match.bundle_retail_price * cartItem.quantity
        calculatedOrderTotal += lineTotal
        pricedLineItems.push({
          item_type:   'bundle',
          database_id: cartItem.database_id,
          title:       match.title,
          unit_price:  match.bundle_retail_price,
          quantity:    cartItem.quantity,
          line_total:  lineTotal
        })
      }
    }

    // Add shipping to verified total
    const shippingFeeNum = Number(shipping_fee) || 0
    calculatedOrderTotal += shippingFeeNum

    // ── Build the Make.com payload ──────────────────────────────────────────
    // Includes the full priced line items array so Make.com has all context
    const processedLineItems = pricedLineItems.map((item: any) => {
      if (item.item_type === "bundle") {
        // Look up the integer ID from the map using the lowercase slug string
        const slug = item.database_id; 
        const numericId = BUNDLE_ID_MAP[slug];
        
        return {
          ...item,
          // Assign the clean integer ID if found, otherwise keep original fallback
          database_id: numericId ? numericId : item.database_id 
        };
      }
      
      // Return single items exactly as they are
      return item;
    });

    const makePayload = {
      tracking_id,
      delivery_profile,
      shipping_fee:  shippingFeeNum,
      order_total:   calculatedOrderTotal,          // always a valid number
      item_count:    pricedLineItems.reduce((s: number, i: any) => s + i.quantity, 0),
      // Full line items — each has item_type, database_id, title, unit_price, quantity, line_total
      line_items:    processedLineItems,
      // Raw clientCart forwarded verbatim so Make.com can re-check database_id if needed
      client_cart:   clientCart
    }

    const makeWebhookUrl = Deno.env.get('MAKE_WEBHOOK_URL') ?? ''
    if (!makeWebhookUrl) throw new Error('MAKE_WEBHOOK_URL environment variable is not set.')

    const makeResponse = await fetch(makeWebhookUrl, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify(makePayload)
    })

    if (!makeResponse.ok) {
      const errText = await makeResponse.text()
      throw new Error(`Make.com webhook returned ${makeResponse.status}: ${errText}`)
    }

    return new Response(
      JSON.stringify({
        success:     true,
        message:     'Order verified and processed',
        order_total: calculatedOrderTotal,
        item_count:  makePayload.item_count
      }),
      { headers: { ...corsHeaders, 'Content-Type': 'application/json' }, status: 200 }
    )

  } catch (error: any) {
    console.error('[checkout] Error:', error.message)
    return new Response(
      JSON.stringify({ error: error.message }),
      { headers: { ...corsHeaders, 'Content-Type': 'application/json' }, status: 400 }
    )
  }
})
