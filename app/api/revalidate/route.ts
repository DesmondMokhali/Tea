import { NextRequest, NextResponse } from 'next/server';
import { revalidatePath, revalidateTag } from 'next/cache';

export async function POST(request: NextRequest) {
  // 1. Check for secret token in query params: /api/revalidate?secret=...
  const secret = request.nextUrl.searchParams.get('secret');
  
  if (secret !== process.env.REVALIDATION_SECRET_TOKEN) {
    return NextResponse.json({ message: 'Invalid token' }, { status: 401 });
  }

  try {
    const body = await request.json();

    // 2. Read the updated table and row data sent by Supabase
    const table = body.table; // 'products' or 'bundles'
    const record = body.record; // The updated product/bundle row

    // 3. Purge cache based on what changed
    if (table === 'products') {
      // Clears cache for main shop page and specific product page
      revalidatePath('/shop');
      if (record?.external_id) {
        revalidatePath(`/products/${record.external_id}`);
      }
    } else if (table === 'bundles') {
      revalidatePath('/bundles');
      if (record?.slug) {
        revalidatePath(`/bundles/${record.slug}`);
      }
    }

    // Also clear global cache tags if you use fetch tags
    revalidateTag('catalog');

    return NextResponse.json({ 
      revalidated: true, 
      now: Date.now(),
      message: `Successfully revalidated cache for ${table}` 
    });
  } catch (err) {
    return NextResponse.json({ message: 'Error revalidating', error: String(err) }, { status: 500 });
  }
}
