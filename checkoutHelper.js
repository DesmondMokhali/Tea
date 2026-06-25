/**
 * Compiles a structured, unauthenticated guest order payload optimized for WhatsApp dispatch modules.
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

  // Compile line items dynamically with zero-padded External ID matching
  const lineItems = (cartState.items || []).map(item => {
    const unitPrice = parseFloat(item.retailPrice) || 0;
    const qty = parseInt(item.quantity, 10) || 0;
    
    return {
      external_id: (item.externalId || "").trim(),
      quantity: qty,
      retail_price: unitPrice,
      total_cost: parseFloat((unitPrice * qty).toFixed(2))
    };
  });

  // Calculate order total
  const orderTotal = lineItems.reduce((sum, item) => sum + item.total_cost, 0);

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

  const response = await fetch('https://hook.eu1.make.com/y9xdj0ntph4f02zfzvn5ksbbsrrirnug', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(compiledPayload)
  });

  return response;
}
