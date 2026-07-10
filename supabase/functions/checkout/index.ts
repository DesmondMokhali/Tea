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
    const { data: dbBundles } = await supabaseAdmin.from('bundles').select('name, retail_price').in('name', bundleCodes)
    // NOTE: If your bundles table uses a 'slug' column for 'performance-engine', change 'name' above to 'slug'

    let calculatedOrderTotal = 0

    clientCart.forEach((cartItem: any) => {
      if (cartItem.item_type === 'single') {
        const match = dbProducts?.find(p => p.external_id === cartItem.database_id)
        if (match) calculatedOrderTotal += (match.retail_price * cartItem.quantity)
      } else if (cartItem.item_type === 'bundle') {
        const match = dbBundles?.find(b => b.name === cartItem.database_id) // Match against the text identifier
        if (match) calculatedOrderTotal += (match.retail_price * cartItem.quantity)
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
