import { useRef } from 'react'
import { useBasket, CROSS_SELL } from '../context/BasketContext'
import { ChevronLeft, ChevronRight, Plus, CheckCheck } from 'lucide-react'
import { useState } from 'react'

const BADGE_COLORS = {
  Popular:     'bg-amber-100 text-amber-700',
  'Best Seller': 'bg-sage-100 text-sage-600',
  New:         'bg-blue-50 text-blue-600',
}

function CrossSellCard({ product }) {
  const { items, dispatch } = useBasket()
  const inCart = items.some(i => i.id === product.id)
  const [added, setAdded] = useState(inCart)

  const handleAdd = () => {
    dispatch({ type: 'ADD', item: product })
    setAdded(true)
  }

  return (
    <div className="snap-start flex-shrink-0 w-40 sm:w-48 bg-white rounded-xl border border-cream-200
                    shadow-card hover:shadow-hover transition-shadow overflow-hidden flex flex-col">
      {/* Badge */}
      <div className="relative">
        <div className="h-36 bg-cream-50 flex items-center justify-center p-2">
          <img
            src={product.image}
            alt={product.name}
            className="w-full h-full object-contain"
            onError={e => { e.target.style.display = 'none' }}
          />
        </div>
        {product.badge && (
          <span
            className={`absolute top-2 left-2 text-[9px] font-bold uppercase tracking-wider
                        px-1.5 py-0.5 rounded-md ${BADGE_COLORS[product.badge] || 'bg-cream-100 text-forest-500'}`}
          >
            {product.badge}
          </span>
        )}
      </div>

      {/* Info */}
      <div className="p-3 flex flex-col gap-1.5 flex-1">
        <p className="text-xs font-semibold text-forest-700 leading-tight line-clamp-2">
          {product.name}
        </p>
        <p className="text-sm font-bold text-forest-700">R{product.price.toFixed(2)}</p>
        <button
          onClick={handleAdd}
          disabled={added}
          className={`mt-auto w-full flex items-center justify-center gap-1 py-2 rounded-lg text-xs font-bold
                      transition-all active:scale-95
                      ${added
                        ? 'bg-sage-100 text-sage-600 cursor-default'
                        : 'bg-forest-700 text-white hover:bg-forest-800'}`}
        >
          {added ? (
            <><CheckCheck className="w-3 h-3" /> Added</>
          ) : (
            <><Plus className="w-3 h-3" /> Add to basket</>
          )}
        </button>
      </div>
    </div>
  )
}

export default function CrossSellSlider() {
  const scrollRef = useRef(null)

  const scroll = dir => {
    if (scrollRef.current) {
      scrollRef.current.scrollBy({ left: dir * 200, behavior: 'smooth' })
    }
  }

  // Filter out items already prominently in basket (don't cross-sell own cart)
  const { items } = useBasket()
  const basketIds = new Set(items.map(i => i.id))
  const suggestions = CROSS_SELL.filter(p => !basketIds.has(p.id))

  if (suggestions.length === 0) return null

  return (
    <div className="bg-white rounded-2xl shadow-card p-5">
      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <div>
          <h3 className="font-display font-bold text-forest-700 text-base">You might also like</h3>
          <p className="text-[11px] text-forest-500 mt-0.5">Frequently paired with your selection</p>
        </div>
        {/* Arrow controls — desktop only */}
        <div className="hidden sm:flex gap-1">
          <button
            onClick={() => scroll(-1)}
            className="w-8 h-8 rounded-full border border-cream-200 flex items-center justify-center
                       hover:bg-cream-50 text-forest-700 transition-colors"
          >
            <ChevronLeft className="w-4 h-4" />
          </button>
          <button
            onClick={() => scroll(1)}
            className="w-8 h-8 rounded-full border border-cream-200 flex items-center justify-center
                       hover:bg-cream-50 text-forest-700 transition-colors"
          >
            <ChevronRight className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* Scroll container — touch-swipe on mobile */}
      <div
        ref={scrollRef}
        className="flex gap-3 overflow-x-auto scrollbar-hide snap-x-mandatory pb-1"
        style={{ scrollSnapType: 'x mandatory', WebkitOverflowScrolling: 'touch' }}
      >
        {suggestions.map(p => (
          <CrossSellCard key={p.id} product={p} />
        ))}
      </div>

      {/* Mobile swipe hint */}
      <p className="sm:hidden mt-2 text-center text-[10px] text-forest-500 tracking-wide">
        ← Swipe to explore →
      </p>
    </div>
  )
}
