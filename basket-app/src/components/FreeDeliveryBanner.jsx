import { useBasket, FREE_DELIVERY_THRESHOLD } from '../context/BasketContext'
import { Truck, CheckCircle2 } from 'lucide-react'

export default function FreeDeliveryBanner() {
  const { discountedSubtotal, remaining } = useBasket()
  const pct = Math.min(100, Math.round((discountedSubtotal / FREE_DELIVERY_THRESHOLD) * 100))
  const qualified = discountedSubtotal >= FREE_DELIVERY_THRESHOLD

  return (
    <div
      className={`rounded-xl px-4 py-3 flex flex-col gap-2 border transition-colors
        ${qualified
          ? 'bg-sage-100 border-sage-200'
          : 'bg-amber-50 border-amber-100'}`}
    >
      {/* Top row */}
      <div className="flex items-center gap-2">
        {qualified ? (
          <CheckCircle2 className="w-4 h-4 text-sage-500 flex-shrink-0" />
        ) : (
          <Truck className="w-4 h-4 text-amber-500 flex-shrink-0" />
        )}
        <p className={`text-sm font-semibold ${qualified ? 'text-sage-600' : 'text-amber-700'}`}>
          {qualified
            ? 'Congratulations! Your order qualifies for FREE delivery.'
            : `Spend R${remaining} more to get FREE courier delivery.`}
        </p>
      </div>

      {/* Progress bar */}
      <div className="h-1.5 rounded-full bg-cream-200 overflow-hidden">
        <div
          className={`h-full rounded-full transition-all duration-500
            ${qualified ? 'bg-sage-500' : 'bg-amber-400'}`}
          style={{ width: `${pct}%` }}
        />
      </div>

      {!qualified && (
        <p className="text-[11px] text-amber-600 font-medium">
          R{discountedSubtotal} of R{FREE_DELIVERY_THRESHOLD} — {pct}% there
        </p>
      )}
    </div>
  )
}
