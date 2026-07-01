import { useBasket } from '../context/BasketContext'

export default function OrderSummary() {
  const { subtotal, discountAmt, discountedSubtotal, delivery, total } = useBasket()

  const handleCheckoutClick = () => {
    // If embedding with the legacy index.html checkout modal, we can open it:
    if (window.opener) {
      try {
        window.opener.openCheckout()
        window.close()
      } catch (e) {
        window.location.href = '../index.html?openCheckout=true'
      }
    } else {
      window.location.href = '../index.html?openCheckout=true'
    }
  }

  return (
    <div className="bg-white rounded-2xl shadow-card p-5 border border-cream-100 flex flex-col gap-4">
      <h3 className="font-display font-bold text-forest-700 text-base border-b border-cream-100 pb-3">
        Summary
      </h3>

      <div className="flex flex-col gap-2.5 text-sm">
        {/* Subtotal */}
        <div className="flex justify-between text-forest-500">
          <span>Subtotal</span>
          <span className="font-semibold text-forest-700">R{subtotal.toFixed(2)}</span>
        </div>

        {/* Promo Discount */}
        {discountAmt > 0 && (
          <div className="flex justify-between text-sage-600">
            <span>Discount</span>
            <span className="font-bold">-R{discountAmt.toFixed(2)}</span>
          </div>
        )}

        {/* Delivery Charge */}
        <div className="flex justify-between text-forest-500">
          <span>Delivery Charge</span>
          <span className={`font-semibold ${delivery === 0 ? 'text-sage-600 font-bold' : 'text-forest-700'}`}>
            {delivery === 0 ? 'FREE (Spend R500+)' : 'R 75'}
          </span>
        </div>

        {/* Total Divider */}
        <div className="border-t border-cream-200 my-1" />

        {/* Grand Total */}
        <div className="flex justify-between items-baseline">
          <span className="font-display font-bold text-forest-700 text-base">Estimated Total</span>
          <span className="font-display font-bold text-forest-700 text-xl">R{total.toFixed(2)}</span>
        </div>
      </div>

      {/* Action Button */}
      <button
        onClick={handleCheckoutClick}
        className="w-full bg-forest-700 hover:bg-forest-800 text-white font-bold py-3.5 px-6 rounded-xl
                   transition-all shadow-md active:scale-[0.98] text-sm uppercase tracking-wider mt-2"
      >
        Proceed to checkout
      </button>
    </div>
  )
}
