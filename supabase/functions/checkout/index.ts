import { serve } from "https://deno.land/std@0.168.0/http/server.ts"
import { createClient } from "https://esm.sh/@supabase/supabase-js@2"

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}

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

    const supabaseAdmin = createClient(
      Deno.env.get('SUPABASE_URL') ?? '',
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''
    )

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
      .select('external_id, name, retail_price')  // 'name' is the actual column; frontend maps it to .title
      .in('external_id', productCodes.length > 0 ? productCodes : ['__none__'])

    if (productError) throw new Error(`Supabase products query failed: ${productError.message}`)

    // Fetch all bundles and match client slugs in-memory to handle title
    // formatting differences (spaces vs hyphens, case, ampersands, etc.)
    const { data: dbBundles, error: bundleError } = await supabaseAdmin
      .from('bundles')
      .select('title, bundle_retail_price')

    if (bundleError) throw new Error(`Supabase bundles query failed: ${bundleError.message}`)

    // Slug normaliser: converts "Metabolic & Weight" → "metabolic-and-weight"
    const toSlug = (str: string) => (str || '').toLowerCase()
      .replace(/&/g, 'and')
      .replace(/[^a-z0-9\s-]/g, '')
      .replace(/[-\s]+/g, '_')
      .replace(/_+/g, '_')
      .replace(/^_|_$/g, '')
      .replace(/_/g, '-')

    // ── Calculate verified server-side order total ──────────────────────────
    let calculatedOrderTotal = 0
    const pricedLineItems: any[] = []

    for (const cartItem of clientCart) {
      if (cartItem.item_type === 'single') {
        const match = dbProducts?.find((p: any) => p.external_id === cartItem.database_id)
        if (!match) {
          // Surface the exact failing SKU — this is what was causing empty totals
          console.error(`[checkout] No product found for external_id="${cartItem.database_id}". Check Supabase products table.`)
          throw new Error(`Product not found in database: "${cartItem.database_id}". Order cannot be completed.`)
        }
        const lineTotal = match.retail_price * cartItem.quantity
        calculatedOrderTotal += lineTotal
        pricedLineItems.push({
          item_type:   'single',
          database_id: cartItem.database_id,
          title:       match.name,          // DB column is 'name'; exposed as 'title' in payload
          unit_price:  match.retail_price,
          quantity:    cartItem.quantity,
          line_total:  lineTotal
        })

      } else if (cartItem.item_type === 'bundle') {
        const targetSlug = toSlug(cartItem.database_id)
        const match = dbBundles?.find((b: any) => toSlug(b.title) === targetSlug)
        if (!match) {
          console.error(`[checkout] No bundle matched slug="${targetSlug}" (original="${cartItem.database_id}"). Check Supabase bundles table.`)
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
    const makePayload = {
      tracking_id,
      delivery_profile,
      shipping_fee:  shippingFeeNum,
      order_total:   calculatedOrderTotal,          // always a valid number
      item_count:    pricedLineItems.reduce((s: number, i: any) => s + i.quantity, 0),
      // Full line items — each has item_type, database_id, title, unit_price, quantity, line_total
      line_items:    pricedLineItems,
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
