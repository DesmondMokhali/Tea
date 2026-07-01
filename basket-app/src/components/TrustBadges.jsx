import { Truck, ShieldCheck, HeartHandshake } from 'lucide-react'

export default function TrustBadges() {
  return (
    <div className="flex flex-col gap-3">
      {/* Badge 1: Courier */}
      <div className="bg-white rounded-xl border border-cream-200 p-4 flex gap-3 shadow-sm hover:shadow-card transition-shadow">
        <div className="w-10 h-10 rounded-xl bg-sage-100 flex items-center justify-center text-sage-600 flex-shrink-0">
          <Truck className="w-5 h-5" />
        </div>
        <div>
          <h4 className="text-xs font-bold text-forest-700 uppercase tracking-wider">Fast Courier Delivery</h4>
          <p className="text-[11px] text-forest-500 mt-1 leading-normal">
            Delivered directly to your door in 3-5 working days. Nationwide shipping across South Africa.
          </p>
        </div>
      </div>

      {/* Badge 2: Returns */}
      <div className="bg-white rounded-xl border border-cream-200 p-4 flex gap-3 shadow-sm hover:shadow-card transition-shadow">
        <div className="w-10 h-10 rounded-xl bg-sage-100 flex items-center justify-center text-sage-600 flex-shrink-0">
          <ShieldCheck className="w-5 h-5" />
        </div>
        <div>
          <h4 className="text-xs font-bold text-forest-700 uppercase tracking-wider">7-Day Quality Guarantee</h4>
          <p className="text-[11px] text-forest-500 mt-1 leading-normal">
            If you are not satisfied with the seal or quality, return within 7 days for a hassle-free exchange.
          </p>
        </div>
      </div>

      {/* Badge 3: Support */}
      <div className="bg-white rounded-xl border border-cream-200 p-4 flex gap-3 shadow-sm hover:shadow-card transition-shadow">
        <div className="w-10 h-10 rounded-xl bg-sage-100 flex items-center justify-center text-sage-600 flex-shrink-0">
          <HeartHandshake className="w-5 h-5" />
        </div>
        <div>
          <h4 className="text-xs font-bold text-forest-700 uppercase tracking-wider">Customer Support</h4>
          <p className="text-[11px] text-forest-500 mt-1 leading-normal">
            Need dosage advice or help checking out? Chat with us directly on WhatsApp for premium service.
          </p>
        </div>
      </div>
    </div>
  )
}
