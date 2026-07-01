import { useBasket } from '../context/BasketContext'
import { ShoppingCart } from 'lucide-react'

export default function NavBar() {
  const { items } = useBasket()
  const totalQty = items.reduce((s, i) => s + i.qty, 0)

  return (
    <header className="sticky top-0 z-50 bg-forest-700 shadow-lg">
      <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
        {/* Logo */}
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-full bg-sage-400 flex items-center justify-center text-white text-xs font-display font-bold">
            T
          </div>
          <div>
            <span className="text-white font-display font-semibold text-base leading-none block">
              Tangren
            </span>
            <span className="text-sage-200 text-[10px] tracking-widest uppercase leading-none">
              Herbal Wellness
            </span>
          </div>
        </div>

        {/* Back + Cart Icon */}
        <div className="flex items-center gap-4">
          <a
            href="../index.html"
            className="text-cream-100 hover:text-white text-sm font-medium transition-colors hidden sm:block"
          >
            ← Continue Shopping
          </a>
          <div className="relative">
            <ShoppingCart className="w-6 h-6 text-white" />
            {totalQty > 0 && (
              <span className="absolute -top-2 -right-2 bg-sage-500 text-white text-[10px] font-bold
                               w-5 h-5 rounded-full flex items-center justify-center leading-none">
                {totalQty}
              </span>
            )}
          </div>
        </div>
      </div>
    </header>
  )
}
