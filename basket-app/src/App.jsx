import React from 'react'
import NavBar from './components/NavBar'
import FreeDeliveryBanner from './components/FreeDeliveryBanner'
import BasketList from './components/BasketList'
import CrossSellSlider from './components/CrossSellSlider'
import PromoCode from './components/PromoCode'
import OrderSummary from './components/OrderSummary'
import TrustBadges from './components/TrustBadges'

export default function App() {
  return (
    <div className="min-h-screen flex flex-col bg-cream-50 font-sans pb-10">
      <NavBar />

      <main className="max-w-6xl mx-auto px-4 py-6 w-full flex-1 flex flex-col gap-6">
        {/* Page Title */}
        <h1 className="font-display font-bold text-forest-700 text-2xl sm:text-3xl leading-tight text-center sm:text-left">
          Shopping Basket
        </h1>

        {/* Dynamic Responsive Columns Layout */}
        <div className="grid grid-cols-1 lg:grid-cols-[1fr_360px] gap-6 items-start">
          {/* Main Area (Left Column on Desktop) */}
          <div className="flex flex-col gap-6 w-full">
            {/* 1. Free Delivery Banner */}
            <FreeDeliveryBanner />

            {/* 2. Main Basket List */}
            <BasketList />

            {/* 3. Cross-Sell Carousel */}
            <CrossSellSlider />

            {/* 4. Promo Code Container - Mobile Flow Position Override */}
            <div className="block lg:hidden">
              <PromoCode />
            </div>

            {/* 5. Informational Trust Badges - Mobile Flow Position Override */}
            <div className="block lg:hidden">
              <TrustBadges />
            </div>
          </div>

          {/* Sidebar Area (Right Column on Desktop) */}
          <div className="flex flex-col gap-6 w-full sticky top-20">
            {/* Promo Code - Desktop Flow */}
            <div className="hidden lg:block">
              <PromoCode />
            </div>

            {/* 2. Order Calculation Total Card */}
            <OrderSummary />

            {/* 3. Trust Banners - Desktop Flow */}
            <div className="hidden lg:block">
              <TrustBadges />
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}
