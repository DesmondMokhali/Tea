import { useBasket } from '../context/BasketContext'
import { Minus, Plus, Trash2 } from 'lucide-react'

function BasketItem({ item }) {
  const { dispatch } = useBasket()

  return (
    <div className="flex gap-3 py-4 border-b border-cream-200 last:border-0 group">
      {/* Thumbnail */}
      <div className="w-20 h-20 sm:w-24 sm:h-24 flex-shrink-0 rounded-xl overflow-hidden bg-cream-100 border border-cream-200">
        <img
          src={item.image}
          alt={item.name}
          className="w-full h-full object-contain p-1"
          onError={e => { e.target.style.display = 'none' }}
        />
      </div>

      {/* Info block */}
      <div className="flex-1 min-w-0 flex flex-col gap-2">
        {/* Name + Remove */}
        <div className="flex items-start justify-between gap-2">
          <h3 className="font-display font-semibold text-forest-700 text-sm sm:text-base leading-tight">
            {item.name}
          </h3>
          <button
            onClick={() => dispatch({ type: 'REMOVE', id: item.id })}
            className="flex-shrink-0 p-1.5 rounded-lg text-cream-200 hover:text-red-500 hover:bg-red-50
                       transition-colors group-hover:text-red-400"
            aria-label={`Remove ${item.name}`}
          >
            <Trash2 className="w-4 h-4" />
          </button>
        </div>

        {/* Unit price */}
        <p className="text-xs text-forest-500 font-medium">R{item.price.toFixed(2)} each</p>

        {/* Qty + Row Total */}
        <div className="flex items-center justify-between mt-auto">
          {/* Qty Counter */}
          <div className="flex items-center gap-0 border border-cream-200 rounded-lg overflow-hidden bg-white shadow-sm">
            <button
              onClick={() =>
                item.qty === 1
                  ? dispatch({ type: 'REMOVE', id: item.id })
                  : dispatch({ type: 'UPDATE_QTY', id: item.id, qty: item.qty - 1 })
              }
              className="w-9 h-9 flex items-center justify-center text-forest-700 hover:bg-cream-100
                         transition-colors font-bold text-lg active:scale-95"
              aria-label="Decrease quantity"
            >
              <Minus className="w-3.5 h-3.5" />
            </button>
            <span className="w-9 h-9 flex items-center justify-center text-sm font-bold text-forest-700 border-x border-cream-200">
              {item.qty}
            </span>
            <button
              onClick={() => dispatch({ type: 'UPDATE_QTY', id: item.id, qty: item.qty + 1 })}
              className="w-9 h-9 flex items-center justify-center text-forest-700 hover:bg-cream-100
                         transition-colors active:scale-95"
              aria-label="Increase quantity"
            >
              <Plus className="w-3.5 h-3.5" />
            </button>
          </div>

          {/* Row Total */}
          <span className="font-bold text-forest-700 text-sm sm:text-base">
            R{(item.price * item.qty).toFixed(2)}
          </span>
        </div>
      </div>
    </div>
  )
}

export default function BasketList() {
  const { items } = useBasket()

  if (items.length === 0) {
    return (
      <div className="bg-white rounded-2xl shadow-card p-10 text-center space-y-3">
        <div className="text-5xl">🛒</div>
        <h3 className="font-display text-xl text-forest-700">Your basket is empty</h3>
        <p className="text-sm text-forest-500">Add some herbal wellness products to get started.</p>
        <a
          href="../index.html"
          className="inline-block mt-2 bg-forest-700 text-white text-sm font-semibold
                     px-6 py-2.5 rounded-xl hover:bg-forest-800 transition-colors"
        >
          Browse Products
        </a>
      </div>
    )
  }

  return (
    <div className="bg-white rounded-2xl shadow-card">
      {/* Card Header */}
      <div className="px-5 pt-5 pb-3 border-b border-cream-100 flex items-center justify-between">
        <h2 className="font-display font-bold text-forest-700 text-lg">
          Your Basket
          <span className="ml-2 text-xs bg-cream-100 text-forest-500 font-sans font-medium px-2 py-0.5 rounded-full">
            {items.length} {items.length === 1 ? 'item' : 'items'}
          </span>
        </h2>
      </div>

      {/* Items */}
      <div className="px-5">
        {items.map(item => (
          <BasketItem key={item.id} item={item} />
        ))}
      </div>
    </div>
  )
}
