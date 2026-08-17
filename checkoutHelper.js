/**
 * Compiles a structured, unauthenticated guest order payload optimized for WhatsApp dispatch modules.
 * 
 * Each line item explicitly identifies whether it is a bundle or a standalone product:
 *   - Bundle:     { bundle_id: <id>, product_id: null,  quantity, unit_price, line_total }
 *   - Standalone: { bundle_id: null,  product_id: <sku>, quantity, unit_price, line_total }
 *
 * @param {Object} cartState - Current guest cart items (e.g. from context/local storage).
 * @param {Object} formData - Form inputs filled out by the guest during checkout.
 * @returns {Object} The complete compiled JSON checkout payload.
 */
export function compileCheckoutPayload(cartState, formData) {
  // Extract and format individual address parts into a single flat, legible string
  const addressParts = [
    formData.streetAddress,
    formData.suburb,
    formData.city,
    formData.province,
    formData.postalCode
  ].filter(part => part && part.trim() !== "");

  const deliveryInstructions = addressParts.join(", ");

  const deliveryProfile = {
    recipient_name: (formData.fullName || "").trim(),
    recipient_whatsapp: (formData.whatsappNumber || "").trim(),
    delivery_instructions: deliveryInstructions,
    special_notes: (formData.specialNotes || "").trim()
  };

  // Compile line items with explicit bundle vs standalone product identification
  const lineItems = (cartState.items || []).map(item => {
    const unitPrice = parseFloat(item.retailPrice) || 0;
    const qty = parseInt(item.quantity, 10) || 0;
    const lineTotal = parseFloat((unitPrice * qty).toFixed(2));

    // Bundle items carry a bundleId — standalone products do not
    if (item.bundleId) {
      return {
        bundle_id: item.bundleId,
        product_id: null,
        quantity: qty,
        unit_price: unitPrice,
        line_total: lineTotal
      };
    }

    return {
      bundle_id: null,
      product_id: (item.externalId || item.sku || "").trim(),
      quantity: qty,
      unit_price: unitPrice,
      line_total: lineTotal
    };
  });

  // Calculate order total
  const orderTotal = lineItems.reduce((sum, item) => sum + item.line_total, 0);

  return {
    delivery_profile: deliveryProfile,
    line_items: lineItems,
    order_total: parseFloat(orderTotal.toFixed(2)),
    checkout_timestamp: new Date().toISOString()
  };
}

/**
 * Compiles and dispatches the checkout payload directly to the downstream Make.com webhook.
 * 
 * @param {Object} cartState - Current guest cart items.
 * @param {Object} formData - Form inputs filled out by the guest.
 * @returns {Promise<Response>} The fetch Response promise.
 */
export async function submitCheckoutOrder(cartState, formData) {
  const compiledPayload = compileCheckoutPayload(cartState, formData);

  const response = await fetch('https://hook.eu1.make.com/gjgs9if1449mylxmt44hxc1n9rv1535n', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(compiledPayload)
  });

  return response;
}
