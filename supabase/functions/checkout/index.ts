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
    const { clientCart, tracking_id, delivery_profile, shipping_fee } = await req.json()

    const supabaseAdmin = createClient(
      Deno.env.get('SUPABASE_URL') ?? '',
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''
    )

    // Extract the text-based identifiers sent by the browser
    const productCodes = clientCart.filter((i: any) => i.item_type === 'single').map((i: any) => i.database_id)
    const bundleCodes = clientCart.filter((i: any) => i.item_type === 'bundle').map((i: any) => i.database_id)

    // 🛠️ FIX: Query using text columns instead of numerical 'id'
    const { data: dbProducts } = await supabaseAdmin.from('products').select('external_id, retail_price').in('external_id', productCodes)
    
    // Fetch all bundles to run in-memory slug comparison (avoids exact string match failure against title)
    const { data: dbBundles } = await supabaseAdmin.from('bundles').select('title, bundle_retail_price')

    // Normalization helper: converts both DB titles and client slugs to a matched lower-case slug comparison format
    const toSlug = (str: string) => (str || '').toLowerCase()
      .replace(/&/g, 'and')
      .replace(/[^a-z0-9\s-]/g, '')
      .replace(/[-\s]+/g, '_')
      .replace(/_+/g, '_')
      .replace(/^_|_$/g, '')
      .replace(/_/g, '-'); // converts to clean hyphenated-slug

    let calculatedOrderTotal = 0

    clientCart.forEach((cartItem: any) => {
      if (cartItem.item_type === 'single') {
        const match = dbProducts?.find(p => p.external_id === cartItem.database_id)
        if (match) calculatedOrderTotal += (match.retail_price * cartItem.quantity)
      } else if (cartItem.item_type === 'bundle') {
        const targetSlug = toSlug(cartItem.database_id);
        const match = dbBundles?.find(b => toSlug(b.title) === targetSlug)
        if (match) calculatedOrderTotal += (match.bundle_retail_price * cartItem.quantity)
      }
    })

    calculatedOrderTotal += Number(shipping_fee)

    const cleanPayload = {
      tracking_id,
      delivery_profile,
      shipping_fee: Number(shipping_fee),
      order_total: calculatedOrderTotal,
      line_items: clientCart.map((item: any) => ({
        bundle_id: item.item_type === 'bundle' ? item.database_id : null,
        product_id: item.item_type === 'single' ? item.database_id : null,
        quantity: item.quantity
      }))
    }

    const makeWebhookUrl = Deno.env.get('MAKE_WEBHOOK_URL') ?? ''
    const makeResponse = await fetch(makeWebhookUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(cleanPayload)
    })

    if (!makeResponse.ok) throw new Error('Forwarding payload to Make automation failed')

    return new Response(JSON.stringify({ success: true, message: 'Order verified and processed' }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 200,
    })

  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 400,
    })
  }
})
