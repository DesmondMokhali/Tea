import React, { createContext, useContext, useReducer } from 'react'

// ── Seed Data ───────────────────────────────────────────────
export const CATALOGUE = [
  { id: 'TG-TEA-001', name: 'Abdomen Slimming Tea',    price: 100, image: '../images/abdomen_slimming_tea.png',       category: 'Tea' },
  { id: 'TG-TEA-003', name: 'Anti Stress Sleeping Tea', price: 100, image: '../images/anti_stress_sleeping_tea.png',   category: 'Tea' },
  { id: 'TG-TEA-007', name: 'Blood Cleaning Tea',       price: 100, image: '../images/blood_cleaning_tea.png',         category: 'Tea' },
  { id: 'TG-TEA-010', name: 'Coughing Tea',             price: 100, image: '../images/coughing_tea.png',               category: 'Tea' },
  { id: 'TG-TEA-011', name: 'Detox Tea',                price: 100, image: '../images/detox_tea.png',                  category: 'Tea' },
  { id: 'TG-TEA-012', name: 'Digestive Tea',            price: 100, image: '../images/digestive_tea.png',              category: 'Tea' },
  { id: 'TG-TEA-013', name: 'Ginseng Tea',              price: 100, image: '../images/ginseng_tea.png',                category: 'Tea' },
  { id: 'TG-TEA-014', name: 'Liver Care Tea',           price: 100, image: '../images/liver_care_tea.png',             category: 'Tea' },
  { id: 'TG-TEA-015', name: 'Kidney Care Tea',          price: 100, image: '../images/kidney_care_tea.png',            category: 'Tea' },
  { id: 'TG-PILL-001', name: 'Gan Mao Ling',            price: 100, image: '../images/gan_mao_ling.png',               category: 'Pill' },
  { id: 'TG-PILL-002', name: 'Liu Wei Di Huang Wan',    price: 100, image: '../images/liu_wei_di_huang_wan.png',       category: 'Pill' },
  { id: 'TG-PILL-003', name: 'Xiao Yao Wan',            price: 100, image: '../images/xiao_yao_wan.png',               category: 'Pill' },
]

export const INITIAL_BASKET = [
  { ...CATALOGUE[0], qty: 2 },
  { ...CATALOGUE[3], qty: 1 },
  { ...CATALOGUE[9], qty: 1 },
]

export const CROSS_SELL = [
  { ...CATALOGUE[10], badge: 'Popular' },
  { ...CATALOGUE[11], badge: 'Best Seller' },
  { ...CATALOGUE[4],  badge: 'New' },
  { ...CATALOGUE[5],  badge: null },
  { ...CATALOGUE[6],  badge: 'Popular' },
  { ...CATALOGUE[7],  badge: null },
]

export const FREE_DELIVERY_THRESHOLD = 500
export const DELIVERY_FEE = 75
export const PROMO_CODES = { TANGREN10: 0.10, HERB15: 0.15 }

// ── Reducer ──────────────────────────────────────────────────
function reducer(state, action) {
  switch (action.type) {
    case 'UPDATE_QTY':
      return {
        ...state,
        items: state.items.map(i =>
          i.id === action.id ? { ...i, qty: Math.max(1, action.qty) } : i
        ),
      }
    case 'REMOVE':
      return { ...state, items: state.items.filter(i => i.id !== action.id) }
    case 'ADD': {
      const existing = state.items.find(i => i.id === action.item.id)
      if (existing) {
        return {
          ...state,
          items: state.items.map(i =>
            i.id === action.item.id ? { ...i, qty: i.qty + 1 } : i
          ),
        }
      }
      return { ...state, items: [...state.items, { ...action.item, qty: 1 }] }
    }
    case 'APPLY_PROMO':
      return { ...state, promoCode: action.code, promoDiscount: action.discount }
    case 'REMOVE_PROMO':
      return { ...state, promoCode: null, promoDiscount: 0 }
    default:
      return state
  }
}

// ── Context ──────────────────────────────────────────────────
const BasketContext = createContext(null)

export function BasketProvider({ children }) {
  const [state, dispatch] = useReducer(reducer, {
    items: INITIAL_BASKET,
    promoCode: null,
    promoDiscount: 0,
  })

  const subtotal = state.items.reduce((s, i) => s + i.price * i.qty, 0)
  const discountAmt = Math.round(subtotal * state.promoDiscount)
  const discountedSubtotal = subtotal - discountAmt
  const delivery = discountedSubtotal >= FREE_DELIVERY_THRESHOLD ? 0 : DELIVERY_FEE
  const total = discountedSubtotal + delivery
  const remaining = FREE_DELIVERY_THRESHOLD - discountedSubtotal

  return (
    <BasketContext.Provider
      value={{ ...state, subtotal, discountAmt, discountedSubtotal, delivery, total, remaining, dispatch }}
    >
      {children}
    </BasketContext.Provider>
  )
}

export const useBasket = () => useContext(BasketContext)
