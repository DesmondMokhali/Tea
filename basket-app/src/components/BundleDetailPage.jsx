import React, { useState } from 'react';

export default function BundleDetailPage() {
  const [activeTab, setActiveTab] = useState('routine');
  
  // Cart state representing the active bundle value and added add-ons
  const [bundlePrice, setBundlePrice] = useState(380);
  const [addedItems, setAddedItems] = useState([]);
  
  // Static catalog for cross-sell add-ons
  const addOnCatalog = [
    { id: 'TG-TEA-011', name: 'Detox Tea', price: 100, label: 'Detox' },
    { id: 'TG-TEA-012', name: 'Digestive Tea', price: 100, label: 'Digestion' },
    { id: 'TG-TEA-014', name: 'Liver Care Tea', price: 100, label: 'Liver' }
  ];

  // Static dataset representing the included bundle items with specific windows
  const includedProducts = [
    {
      id: 'TG-TEA-001',
      name: 'Abdomen Slimming Tea',
      qty: 2,
      timeMarker: '🌅 Morning',
      cat: 'Herbal Tea'
    },
    {
      id: 'TG-TEA-003',
      name: 'Anti Stress Sleeping Tea',
      qty: 1,
      timeMarker: '🌙 Night',
      cat: 'Herbal Tea'
    },
    {
      id: 'TG-PILL-001',
      name: 'Gan Mao Ling',
      qty: 1,
      timeMarker: '☀️ Afternoon',
      cat: 'Herbal Pill'
    }
  ];

  // Handle adding an add-on item dynamically to update prices and thresholds
  const handleAddOn = (item) => {
    if (addedItems.some(i => i.id === item.id)) {
      // Remove if clicked again (toggle behavior for demo checkout feel)
      setAddedItems(addedItems.filter(i => i.id !== item.id));
    } else {
      setAddedItems([...addedItems, item]);
    }
  };

  // Calculate totals
  const addOnsTotal = addedItems.reduce((acc, curr) => acc + curr.price, 0);
  const grandTotal = bundlePrice + addOnsTotal;
  const freeShippingThreshold = 500;
  const remainingForFreeShipping = Math.max(0, freeShippingThreshold - grandTotal);
  const qualifiesForFreeShipping = grandTotal >= freeShippingThreshold;

  return (
    <div className="min-h-screen bg-[#f8fafc] text-[#0f172a] font-sans antialiased pb-32">
      {/* Navigation Header */}
      <header className="border-b border-[#e2e8f0] bg-white sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <span className="h-8 w-8 rounded-full bg-[#1b3a28] flex items-center justify-center text-white font-bold text-sm">🌿</span>
            <span className="font-semibold text-lg tracking-tight">The Herbalist</span>
          </div>
          <nav className="hidden md:flex space-x-8 text-sm font-medium text-[#475569]">
            <a href="#catalogue" className="hover:text-[#1b3a28] transition">Catalogue</a>
            <a href="#about" className="hover:text-[#1b3a28] transition">Our Philosophy</a>
            <a href="#journal" className="hover:text-[#1b3a28] transition">Journal</a>
          </nav>
          <div className="flex items-center gap-4">
            <button className="text-sm font-semibold text-[#475569] hover:text-[#1b3a28]">Sign In</button>
            <button className="bg-[#1b3a28] text-white px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider hover:bg-[#224832] transition">
              Cart ({addedItems.length + 1})
            </button>
          </div>
        </div>
      </header>

      {/* Main Layout Container */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 lg:py-12">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-start mb-12">
          
          {/* Left Column: Image Gallery Placeholder & Details (7/12 width) */}
          <div className="lg:col-span-7 space-y-6">
            <div className="flex items-center gap-2 text-xs font-medium text-[#64748b]">
              <a href="#shop" className="hover:text-[#1b3a28]">Shop</a>
              <span>/</span>
              <a href="#bundles" className="hover:text-[#1b3a28]">Bundles</a>
              <span>/</span>
              <span className="text-[#0f172a]">Daily Wellness Essentials</span>
            </div>

            <div className="bg-white border border-[#e2e8f0] rounded-2xl overflow-hidden shadow-sm">
              <div className="aspect-[4/3] bg-gradient-to-br from-[#f1f5f9] to-[#e2e8f0] relative flex items-center justify-center p-8 group">
                <div className="absolute inset-0 opacity-10 bg-[radial-gradient(#000_1px,transparent_1px)] [background-size:16px_16px]"></div>
                <div className="text-center z-10">
                  <div className="text-5xl mb-4 transform group-hover:scale-110 transition duration-300">📦</div>
                  <h3 className="font-serif text-xl font-bold text-[#0f172a] mb-1">Daily Wellness Essentials</h3>
                  <p className="text-xs text-[#64748b] uppercase tracking-wider">Premium Image Gallery Placeholder</p>
                </div>
              </div>
              <div className="grid grid-cols-4 gap-4 p-4 border-t border-[#e2e8f0]">
                {[1, 2, 3, 4].map((i) => (
                  <div key={i} className="aspect-square bg-slate-100 rounded-lg border border-[#e2e8f0] flex items-center justify-center text-sm font-medium text-[#64748b] hover:border-[#1b3a28] cursor-pointer transition">
                    Img {i}
                  </div>
                ))}
              </div>
            </div>

            <div className="bg-white border border-[#e2e8f0] rounded-2xl p-6 lg:p-8 space-y-6 shadow-sm">
              <div>
                <h2 className="font-serif text-2xl font-bold text-[#0f172a] mb-3">Ritual Instructions</h2>
                <p className="text-[#475569] text-sm leading-relaxed">
                  Follow the designated time markers to achieve optimal synergistic balance. Morning blends activate cellular metabolism and gut health. Afternoon tablets regulate stress markers during peak hours, and evening infusions prepare the nervous system for deep restorative sleep cycles.
                </p>
              </div>
            </div>
          </div>

          {/* Right Column: Sticky Checkout Panel (5/12 width) */}
          <div className="lg:col-span-5 lg:sticky lg:top-24 space-y-6">
            <div className="bg-white border border-[#e2e8f0] rounded-2xl p-6 lg:p-8 shadow-md">
              
              {/* Header Info Block */}
              <div className="border-b border-[#e2e8f0] pb-5 mb-5">
                <span className="inline-block bg-[#f0e0c4] text-[#854d0e] px-2.5 py-0.5 rounded-full text-xs font-bold uppercase tracking-wider mb-3">
                  Restorative Ritual
                </span>
                <h1 className="font-serif text-3xl font-extrabold text-[#0f172a] leading-tight mb-2">
                  Daily Wellness Essentials
                </h1>
                <div className="flex items-center gap-2 mb-4">
                  <div className="flex text-amber-500 text-sm">★ ★ ★ ★ ★</div>
                  <span className="text-xs font-semibold text-[#64748b]">(48 Verified Reviews)</span>
                </div>
                <div className="flex items-baseline gap-3">
                  <span className="text-3xl font-extrabold text-[#059669]">R{grandTotal.toFixed(2)}</span>
                  {addOnsTotal === 0 && (
                    <span className="text-sm font-medium text-[#94a3b8] line-through">R400.00</span>
                  )}
                  <span className="text-xs font-bold text-[#166534] bg-[#eef7f2] px-2 py-0.5 rounded-md">
                    {qualifiesForFreeShipping ? 'Free Delivery Unlocked' : `Spend R${remainingForFreeShipping} more for Free Delivery`}
                  </span>
                </div>
              </div>

              {/* What's Included List Card Component */}
              <div className="mb-6">
                <h3 className="text-xs font-bold uppercase tracking-wider text-[#64748b] mb-3">What's Included</h3>
                <div className="border border-[#e2e8f0] rounded-xl overflow-hidden divide-y divide-[#e2e8f0] bg-[#f8fafc]">
                  {includedProducts.map((product) => (
                    <div key={product.id} className="flex items-center gap-4 p-4 hover:bg-white transition duration-150">
                      <input type="checkbox" checked disabled className="h-4 w-4 rounded border-gray-300 text-[#1b3a28] focus:ring-[#1b3a28] accent-[#1b3a28]" />
                      <div className="h-10 w-10 bg-white border border-[#e2e8f0] rounded-md flex items-center justify-center text-xs flex-shrink-0">🌱</div>
                      <div className="flex-1 min-w-0">
                        <p className="text-xs font-semibold text-[#64748b] uppercase tracking-wide">{product.cat}</p>
                        <p className="text-sm font-bold text-[#0f172a] truncate">{product.name}</p>
                      </div>
                      <div className="flex-shrink-0">
                        <span className="inline-block bg-white border border-[#e2e8f0] px-2 py-1 rounded-md text-xs font-medium text-[#475569] shadow-xs">
                          {product.timeMarker}
                        </span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Delivery Qualifications */}
              <div className="bg-[#f8fafc] border border-[#e2e8f0] rounded-xl p-4 mb-6 flex items-start gap-3">
                <span className="text-lg">🚚</span>
                <div>
                  <p className="text-xs font-bold text-[#0f172a]">
                    {qualifiesForFreeShipping ? 'Qualifies for FREE Delivery!' : `Add R${remainingForFreeShipping} to qualify for FREE Delivery`}
                  </p>
                  <p className="text-[11px] text-[#64748b]">Nationwide trackable shipping.</p>
                </div>
              </div>

              {/* Action Buttons */}
              <div className="space-y-4 text-center">
                <button className="w-full bg-[#0f172a] hover:bg-[#1e293b] text-white font-bold py-4 px-6 rounded-xl transition duration-200 shadow-sm text-sm uppercase tracking-wider">
                  Add Bundle to Cart
                </button>
                <a href="#specials" className="inline-block text-xs font-bold text-[#64748b] hover:text-[#0f172a] transition duration-150">
                  ← Back to Specials
                </a>
              </div>
            </div>
          </div>
        </div>

        {/* Tabbed Information Section (Directly Below Grid) */}
        <div className="bg-white border border-[#e2e8f0] rounded-2xl p-6 lg:p-8 shadow-sm">
          {/* Tab Navigation Menu */}
          <div className="flex border-b border-[#e2e8f0] mb-8 overflow-x-auto">
            <button
              onClick={() => setActiveTab('routine')}
              className={`pb-4 px-6 font-serif text-lg font-bold border-b-2 whitespace-nowrap transition duration-200 ${
                activeTab === 'routine'
                  ? 'border-[#1b3a28] text-[#1b3a28]'
                  : 'border-transparent text-[#64748b] hover:text-[#0f172a]'
              }`}
            >
              The Daily Routine
            </button>
            <button
              onClick={() => setActiveTab('benefits')}
              className={`pb-4 px-6 font-serif text-lg font-bold border-b-2 whitespace-nowrap transition duration-200 ${
                activeTab === 'benefits'
                  ? 'border-[#1b3a28] text-[#1b3a28]'
                  : 'border-transparent text-[#64748b] hover:text-[#0f172a]'
              }`}
            >
              Targeted Benefits
            </button>
            <button
              onClick={() => setActiveTab('ingredients')}
              className={`pb-4 px-6 font-serif text-lg font-bold border-b-2 whitespace-nowrap transition duration-200 ${
                activeTab === 'ingredients'
                  ? 'border-[#1b3a28] text-[#1b3a28]'
                  : 'border-transparent text-[#64748b] hover:text-[#0f172a]'
              }`}
            >
              Ingredients &amp; Dosing
            </button>
          </div>

          {/* Tab Content Panes */}
          <div className="transition-all duration-300">
            {activeTab === 'routine' && (
              <div className="space-y-8 relative before:absolute before:inset-0 before:left-4 before:w-[2px] before:bg-[#e2e8f0] py-2">
                <div className="relative pl-10">
                  <div className="absolute left-[9px] top-1 h-4 w-4 rounded-full border-2 border-[#1b3a28] bg-white"></div>
                  <h4 className="font-bold text-sm text-[#1b3a28] uppercase tracking-wider mb-1">Morning Activation</h4>
                  <h3 className="font-serif text-lg font-bold text-[#0f172a] mb-2">Abdomen Slimming Tea</h3>
                  <p className="text-sm text-[#475569] leading-relaxed max-w-2xl">
                    Steep 1 tablespoon of leaves in boiling water (95°C) for 5 minutes. Drink before breakfast to jumpstart digestion and eliminate abdominal stagnation.
                  </p>
                </div>
                
                <div className="relative pl-10">
                  <div className="absolute left-[9px] top-1 h-4 w-4 rounded-full border-2 border-[#1b3a28] bg-white"></div>
                  <h4 className="font-bold text-sm text-[#1b3a28] uppercase tracking-wider mb-1">Afternoon Defense</h4>
                  <h3 className="font-serif text-lg font-bold text-[#0f172a] mb-2">Gan Mao Ling Tablets</h3>
                  <p className="text-sm text-[#475569] leading-relaxed max-w-2xl">
                    Consume 2 tablets with lukewarm water post-lunch. Acts as a seasonal defense shield and targets systemic body heat build-up.
                  </p>
                </div>

                <div className="relative pl-10">
                  <div className="absolute left-[9px] top-1 h-4 w-4 rounded-full border-2 border-[#1b3a28] bg-white"></div>
                  <h4 className="font-bold text-sm text-[#1b3a28] uppercase tracking-wider mb-1">Evening Restorative</h4>
                  <h3 className="font-serif text-lg font-bold text-[#0f172a] mb-2">Anti Stress Sleeping Tea</h3>
                  <p className="text-sm text-[#475569] leading-relaxed max-w-2xl">
                    Steep 1 tea bag in water for 7 minutes. Drink 45 minutes before sleep to settle your nervous system and release muscle tension.
                  </p>
                </div>
              </div>
            )}

            {activeTab === 'benefits' && (
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="flex items-start gap-3 p-4 bg-[#f8fafc] border border-[#e2e8f0] rounded-xl">
                  <span className="text-[#059669] font-bold text-lg">✓</span>
                  <div>
                    <h4 className="font-bold text-sm text-[#0f172a] mb-1">Eliminates Gut Bloating</h4>
                    <p className="text-xs text-[#64748b]">TCM botanicals target food retention and soothe the intestinal lining.</p>
                  </div>
                </div>
                <div className="flex items-start gap-3 p-4 bg-[#f8fafc] border border-[#e2e8f0] rounded-xl">
                  <span className="text-[#059669] font-bold text-lg">✓</span>
                  <div>
                    <h4 className="font-bold text-sm text-[#0f172a] mb-1">Deep Nervous System Calming</h4>
                    <p className="text-xs text-[#64748b]">Nourishes the heart fire and calms the Shen to encourage restorative sleep cycles.</p>
                  </div>
                </div>
                <div className="flex items-start gap-3 p-4 bg-[#f8fafc] border border-[#e2e8f0] rounded-xl">
                  <span className="text-[#059669] font-bold text-lg">✓</span>
                  <div>
                    <h4 className="font-bold text-sm text-[#0f172a] mb-1">Seasonal Pathogen Protection</h4>
                    <p className="text-xs text-[#64748b]">Reinforces defensive Qi (Wei Qi) to protect the lungs against seasonal chills.</p>
                  </div>
                </div>
                <div className="flex items-start gap-3 p-4 bg-[#f8fafc] border border-[#e2e8f0] rounded-xl">
                  <span className="text-[#059669] font-bold text-lg">✓</span>
                  <div>
                    <h4 className="font-bold text-sm text-[#0f172a] mb-1">Gentle Organ Detoxification</h4>
                    <p className="text-xs text-[#64748b]">Supports liver and kidney pathways using mild natural antioxidant compounds.</p>
                  </div>
                </div>
              </div>
            )}

            {activeTab === 'ingredients' && (
              <div className="overflow-x-auto border border-[#e2e8f0] rounded-xl">
                <table className="w-full text-left border-collapse text-sm">
                  <thead>
                    <tr className="bg-[#f8fafc] border-b border-[#e2e8f0] text-xs font-bold text-[#64748b] uppercase tracking-wider">
                      <th className="p-4">Formula</th>
                      <th className="p-4">Botanical / Technical Name</th>
                      <th className="p-4">Key Ingredients</th>
                      <th className="p-4 text-right">Statutory Dosage</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-[#e2e8f0]">
                    <tr>
                      <td className="p-4 font-bold text-[#0f172a]">Abdomen Slimming Tea</td>
                      <td className="p-4 italic text-[#475569]">Folium Sennae, Crataegi Fructus</td>
                      <td className="p-4 text-[#475569]">Senna leaf, hawthorn berry, orange peel</td>
                      <td className="p-4 text-right font-medium text-[#1b3a28]">3-5g daily infusion</td>
                    </tr>
                    <tr>
                      <td className="p-4 font-bold text-[#0f172a]">Anti Stress Sleeping Tea</td>
                      <td className="p-4 italic text-[#475569]">Semen Ziziphi Spinosae, Radix Polygalae</td>
                      <td className="p-4 text-[#475569]">Spiny sour date seed, milkwort root, lavender</td>
                      <td className="p-4 text-right font-medium text-[#1b3a28]">1 tea bag night infusion</td>
                    </tr>
                    <tr>
                      <td className="p-4 font-bold text-[#0f172a]">Gan Mao Ling</td>
                      <td className="p-4 italic text-[#475569]">Radix Ilicis Asprellae, Flos Evodiae</td>
                      <td className="p-4 text-[#475569]">Rough-haired holly root, wild chrysanthemum</td>
                      <td className="p-4 text-right font-medium text-[#1b3a28]">2 tablets post-meals</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </div>
      </main>

      {/* Bottom Fixed Upsell Bar: Complete Your Ritual */}
      <footer className="fixed bottom-0 left-0 right-0 bg-white border-t border-[#e2e8f0] shadow-[0_-8px_24px_rgba(15,23,42,0.06)] z-40 py-3 px-4 sm:px-6">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row md:items-center justify-between gap-4">
          
          {/* Shipping Threshold Badge Status */}
          <div className="flex flex-col">
            <span className="text-xs font-bold uppercase tracking-wider text-[#64748b]">Complete Your Ritual</span>
            <div className="flex items-center gap-2 mt-1">
              <span className="text-lg font-extrabold text-[#0f172a]">Total: R{grandTotal.toFixed(2)}</span>
              {qualifiesForFreeShipping ? (
                <span className="text-[10px] font-bold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded-full">
                  FREE Delivery Unlocked!
                </span>
              ) : (
                <span className="text-[10px] font-bold text-[#854d0e] bg-[#fef3c7] px-2 py-0.5 rounded-full">
                  Add R{remainingForFreeShipping} more for FREE shipping
                </span>
              )}
            </div>
          </div>

          {/* Add-On Slider/Carousel */}
          <div className="flex items-center gap-3 overflow-x-auto pb-1 md:pb-0 scrollbar-none">
            {addOnCatalog.map((item) => {
              const isAdded = addedItems.some(i => i.id === item.id);
              return (
                <div key={item.id} className="flex items-center gap-3 bg-[#f8fafc] border border-[#e2e8f0] p-2 rounded-xl flex-shrink-0">
                  <div className="h-8 w-8 bg-white border border-[#e2e8f0] rounded-lg flex items-center justify-center text-xs">
                    🍵
                  </div>
                  <div>
                    <h5 className="text-xs font-bold text-[#0f172a]">{item.name}</h5>
                    <p className="text-[10px] font-medium text-[#64748b]">+ R{item.price}</p>
                  </div>
                  <button
                    onClick={() => handleAddOn(item)}
                    className={`text-[10px] font-bold px-3 py-1.5 rounded-lg border transition ${
                      isAdded 
                        ? 'bg-emerald-600 border-emerald-600 text-white hover:bg-emerald-700' 
                        : 'bg-white border-[#e2e8f0] text-[#0f172a] hover:bg-slate-50'
                    }`}
                  >
                    {isAdded ? 'Added' : 'Add'}
                  </button>
                </div>
              );
            })}
          </div>

          {/* Checkout CTA */}
          <div className="flex-shrink-0">
            <button className="w-full md:w-auto bg-[#0f172a] hover:bg-[#1e293b] text-white font-bold text-xs py-3 px-6 rounded-xl uppercase tracking-wider transition">
              Checkout Now
            </button>
          </div>

        </div>
      </footer>
    </div>
  );
}
