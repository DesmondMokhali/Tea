import { useState } from 'react'
import { useBasket, PROMO_CODES } from '../context/BasketContext'
import { Ticket, X } from 'lucide-react'

export default function PromoCode() {
  const { promoCode, promoDiscount, dispatch } = useBasket()
  const [code, setCode] = useState('')
  const [error, setError] = useState('')

  const handleApply = (e) => {
    e.preventDefault()
    setError('')
    const cleanCode = code.trim().toUpperCase()
    
    if (!cleanCode) return

    if (PROMO_CODES[cleanCode] !== undefined) {
      dispatch({
        type: 'APPLY_PROMO',
        code: cleanCode,
        discount: PROMO_CODES[cleanCode]
      })
      setCode('')
    } else {
      setError('Invalid promotional code')
    }
  }

  const handleRemove = () => {
    dispatch({ type: 'REMOVE_PROMO' })
  }

  return (
    <div className="bg-white rounded-2xl shadow-card p-5">
      <h3 className="font-display font-bold text-forest-700 text-sm mb-3 flex items-center gap-2">
        <Ticket className="w-4 h-4 text-sage-500" /> Promo Code
      </h3>

      {promoCode ? (
        <div className="flex items-center justify-between bg-sage-50 border border-sage-100 rounded-xl px-4 py-2.5">
          <div>
            <p className="text-xs text-sage-600 font-bold tracking-wider">{promoCode} Applied</p>
            <p className="text-[11px] text-sage-500 font-medium">({Math.round(promoDiscount * 100)}% Discount)</p>
          </div>
          <button
            onClick={handleRemove}
            className="p-1 rounded-lg text-sage-400 hover:text-red-500 hover:bg-red-50 transition-colors"
          >
            <X className="w-4 h-4" />
          </button>
        </div>
      ) : (
        <form onSubmit={handleApply} className="flex gap-2">
          <div className="flex-1">
            <input
              type="text"
              value={code}
              onChange={(e) => setCode(e.target.value)}
              placeholder="e.g. TANGREN10"
              className="w-full px-4 py-2.5 border border-cream-200 rounded-xl text-sm outline-none focus:border-sage-400 transition-colors uppercase font-medium tracking-wide"
            />
          </div>
          <button
            type="submit"
            className="px-5 py-2.5 bg-forest-700 hover:bg-forest-800 text-white text-xs font-bold rounded-xl transition-all active:scale-95 flex-shrink-0"
          >
            Apply
          </button>
        </form>
      )}

      {error && <p className="text-[11px] text-red-500 font-semibold mt-1.5 ml-1">{error}</p>}
      <p className="text-[10px] text-forest-500 mt-2 ml-1">Use promo code TANGREN10 to get 10% off your purchase.</p>
    </div>
  )
}
