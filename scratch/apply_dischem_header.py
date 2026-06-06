import os
import glob
import re

base_dir = r"C:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore"

# New HTML header layout
new_header_html = """<!-- ── TOP UTILITY BAR ── -->
<div class="top-bar">
  <div class="top-bar-inner">
    <div class="top-bar-left">
      <span>📞 Careline: +27 (0) 11 888 3000</span>
      <span class="bar-sep">|</span>
      <span>🌿 Free Delivery on Orders Over R500</span>
    </div>
    <div class="top-bar-right">
      <a href="index.html#contact">Track Order</a>
      <span class="bar-sep">|</span>
      <a href="#" onclick="alert('Benefit Rewards program details coming soon!')">Benefit Card</a>
      <span class="bar-sep">|</span>
      <a href="#" onclick="alert('Accounts integration coming soon!')">Login / Register</a>
    </div>
  </div>
</div>

<!-- ── MAIN HEADER ── -->
<header class="main-header">
  <div class="main-header-inner">
    <!-- Hamburger Button (Mobile Only) -->
    <button class="hamburger-btn" onclick="toggleMobileMenu(true)">
      <i data-lucide="menu"></i>
    </button>

    <!-- Brand Logo -->
    <a class="nlogo" href="index.html">
      <div class="nmark"><i data-lucide="leaf"></i></div>
      <div class="ntext"><b>The Herbalist</b><small>Traditional Chinese Wellness</small></div>
    </a>

    <!-- Large Central Search Bar -->
    <div class="header-search-wrap">
      <span class="search-icon"><i data-lucide="search"></i></span>
      <input type="text" id="si" placeholder="Search products, remedies, ingredients..." oninput="doSearch(this.value)">
      <button class="search-btn" onclick="doSearch(document.getElementById('si').value)">Search</button>
    </div>

    <!-- Actions -->
    <div class="header-actions">
      <a href="#" class="action-link" onclick="alert('Benefit Rewards Card & Accounts coming soon!')">
        <i data-lucide="user"></i>
        <span class="action-text">Account</span>
      </a>
      <button class="header-cart-btn" onclick="showCart()">
        <div class="cart-icon-wrap">
          <i data-lucide="shopping-cart"></i>
          <span class="cart-badge" id="cnt">0</span>
        </div>
        <div class="cart-btn-text">
          <span class="cart-label">Basket</span>
          <span class="cart-total" id="header-cart-total">R0.00</span>
        </div>
      </button>
    </div>
  </div>
</header>

<!-- ── MOBILE SEARCH ROW ── -->
<div class="mobile-search-row">
  <div class="header-search-wrap">
    <span class="search-icon"><i data-lucide="search"></i></span>
    <input type="text" id="si-mobile" placeholder="Search products, remedies..." oninput="doSearch(this.value); document.getElementById('si').value = this.value;">
  </div>
</div>

<!-- ── CATEGORY NAVIGATION BAR ── -->
<nav class="category-nav">
  <div class="category-nav-inner">
    <a href="index.html" class="cat-link">Home</a>
    <div class="nav-dropdown">
      <a href="index.html?filter=all#ga" class="nav-dropbtn">Products <i data-lucide="chevron-down" style="width:12px;height:12px;display:inline-block;vertical-align:middle;margin-left:3px"></i></a>
      <div class="nav-dropdown-content">
        <a href="index.html?filter=all#ga">All Products</a>
        <a href="index.html?filter=teas#ga">Herbal Teas</a>
        <a href="index.html?filter=pills#ga">Herbal Pills</a>
      </div>
    </div>
    <a href="blog.html" class="cat-link">Wellness Blog</a>
    <a href="index.html#contact" class="cat-link">Contact Us</a>
  </div>
</nav>

<!-- ── MOBILE MENU DRAWER ── -->
<div class="mobile-menu-overlay" id="mobile-menu-overlay" onclick="toggleMobileMenu(false)"></div>
<div class="mobile-menu-drawer" id="mobile-menu-drawer">
  <div class="mobile-menu-hdr">
    <h3>Menu</h3>
    <button class="mobile-menu-close" onclick="toggleMobileMenu(false)">&times;</button>
  </div>
  <div class="mobile-menu-body">
    <a href="index.html" onclick="toggleMobileMenu(false)">Home</a>
    <div class="mobile-menu-section">
      <div class="mobile-menu-section-title">Products</div>
      <a href="index.html?filter=all#ga" onclick="toggleMobileMenu(false)">All Products</a>
      <a href="index.html?filter=teas#ga" onclick="toggleMobileMenu(false)">Herbal Teas</a>
      <a href="index.html?filter=pills#ga" onclick="toggleMobileMenu(false)">Herbal Pills</a>
    </div>
    <a href="blog.html" onclick="toggleMobileMenu(false)">Wellness Blog</a>
    <a href="index.html#contact" onclick="toggleMobileMenu(false)">Contact Us</a>
  </div>
</div>"""

# CSS for the new Dis-Chem styled header
header_css = """/* ─────────────────────────────────────────────────────────────
   ✦  DIS-CHEM STYLE PREMIUM HEADER & NAVIGATION  ✦
───────────────────────────────────────────────────────────── */
:root {
  --header-bg: var(--f);
  --header-border: rgba(255, 255, 255, 0.1);
  --header-text: var(--gl);
  --search-bg: rgba(255, 255, 255, 0.08);
}

/* ── Top Utility Bar ── */
.top-bar {
  background: #112519;
  color: rgba(255,255,255,0.70);
  font-size: 11.5px;
  height: 32px;
  display: flex;
  align-items: center;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}
.top-bar-inner {
  width: 100%;
  max-width: 1300px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  justify-content: space-between;
}
.top-bar-left, .top-bar-right {
  display: flex;
  align-items: center;
  gap: 12px;
}
.top-bar-right a {
  color: rgba(255,255,255,0.70);
  text-decoration: none;
  transition: color var(--tr);
}
.top-bar-right a:hover {
  color: var(--gl);
}
.bar-sep {
  color: rgba(255,255,255,0.15);
}

/* ── Main Header ── */
.main-header {
  background: var(--header-bg);
  border-bottom: 1px solid var(--header-border);
  padding: 12px 24px;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 24px rgba(0,0,0,0.2);
}
.main-header-inner {
  max-width: 1300px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

/* Logo customizations (matches original gold/green) */
.main-header .nlogo {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
}
.main-header .nlogo .ntext b {
  font-family: 'Playfair Display', serif;
  font-size: 17px;
  font-weight: 600;
  color: var(--gl);
  letter-spacing: 0.04em;
  display: block;
}
.main-header .nlogo .ntext small {
  font-size: 9.5px;
  color: var(--sl);
  letter-spacing: 0.14em;
  text-transform: uppercase;
}
.main-header .nlogo .nmark {
  width: 34px;
  height: 34px;
  background: var(--g);
  color: var(--f);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
  flex-shrink: 0;
}

/* Central Search Bar */
.header-search-wrap {
  flex: 1;
  max-width: 580px;
  position: relative;
  display: flex;
  align-items: center;
}
.header-search-wrap input {
  width: 100%;
  background: var(--search-bg);
  border: 1.5px solid rgba(255,255,255,0.15);
  border-radius: 24px;
  padding: 10px 100px 10px 42px;
  font-family: 'DM Sans', sans-serif;
  font-size: 13.5px;
  color: #fff;
  outline: none;
  transition: all var(--tr);
}
.header-search-wrap input::placeholder {
  color: rgba(255,255,255,0.4);
}
.header-search-wrap input:focus {
  background: rgba(255,255,255,0.12);
  border-color: var(--g);
  box-shadow: 0 0 0 3px rgba(200,160,110,0.15);
}
.header-search-wrap .search-icon {
  position: absolute;
  left: 16px;
  color: rgba(255,255,255,0.4);
  display: flex;
  align-items: center;
  pointer-events: none;
}
.header-search-wrap .search-icon svg {
  width: 15px;
  height: 15px;
}
.header-search-wrap .search-btn {
  position: absolute;
  right: 5px;
  background: var(--g);
  color: var(--f);
  border: none;
  border-radius: 20px;
  padding: 6px 16px;
  font-family: 'DM Sans', sans-serif;
  font-size: 12px;
  font-weight: 700;
  cursor: pointer;
  transition: all var(--tr);
}
.header-search-wrap .search-btn:hover {
  background: var(--gl);
}

/* Header Action Buttons */
.header-actions {
  display: flex;
  align-items: center;
  gap: 20px;
}
.action-link {
  display: flex;
  align-items: center;
  gap: 8px;
  color: rgba(255,255,255,0.85);
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 600;
  transition: color var(--tr);
}
.action-link:hover {
  color: var(--gl);
}
.action-link svg {
  width: 18px;
  height: 18px;
  color: var(--gl);
}

/* Premium Cart Button */
.header-cart-btn {
  background: var(--g);
  color: var(--f);
  border: none;
  border-radius: 28px;
  padding: 8px 18px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 12px;
  transition: all var(--tr);
}
.header-cart-btn:hover {
  background: var(--gl);
  transform: translateY(-1px);
}
.cart-icon-wrap {
  position: relative;
  display: flex;
  align-items: center;
}
.cart-icon-wrap svg {
  width: 18px;
  height: 18px;
  color: var(--f);
}
.cart-badge {
  position: absolute;
  top: -8px;
  right: -10px;
  background: var(--f);
  color: var(--g);
  font-size: 9px;
  font-weight: 700;
  min-width: 16px;
  height: 16px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 4px;
  border: 1px solid var(--g);
  transition: transform 0.2s ease;
}
.cart-btn-text {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  line-height: 1.1;
}
.cart-label {
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: rgba(27,58,40,0.7);
}
.cart-total {
  font-size: 12.5px;
  font-weight: 700;
  color: var(--f);
}

/* ── Category Navigation Bar ── */
.category-nav {
  background: var(--fm);
  border-bottom: 1px solid rgba(0,0,0,0.12);
  padding: 10px 24px;
}
.category-nav-inner {
  max-width: 1300px;
  margin: 0 auto;
  display: flex;
  gap: 28px;
  align-items: center;
}
.cat-link {
  color: rgba(255,255,255,0.75);
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  transition: color var(--tr);
}
.cat-link:hover {
  color: var(--gl);
}

/* Category Nav Dropdown */
.category-nav .nav-dropdown {
  position: relative;
}
.category-nav .nav-dropbtn {
  color: rgba(255,255,255,0.75);
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  transition: color var(--tr);
}
.category-nav .nav-dropdown:hover .nav-dropbtn {
  color: var(--gl);
}

/* Mobile Hamburger */
.hamburger-btn {
  display: none;
  background: none;
  border: none;
  color: var(--gl);
  cursor: pointer;
  padding: 4px;
}
.hamburger-btn svg {
  width: 24px;
  height: 24px;
}

/* Mobile Search Row (Hidden on Desktop) */
.mobile-search-row {
  display: none;
  background: var(--f);
  padding: 8px 16px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}

/* Mobile Drawer Menu */
.mobile-menu-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.5);
  z-index: 300;
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--tr);
}
.mobile-menu-overlay.on {
  opacity: 1;
  pointer-events: all;
}
.mobile-menu-drawer {
  position: fixed;
  top: 0;
  left: -280px;
  width: 280px;
  height: 100vh;
  background: var(--f);
  z-index: 310;
  box-shadow: 4px 0 24px rgba(0,0,0,0.3);
  display: flex;
  flex-direction: column;
  transition: left 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.mobile-menu-drawer.on {
  left: 0;
}
.mobile-menu-hdr {
  padding: 16px 20px;
  border-bottom: 1px solid rgba(255,255,255,0.1);
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.mobile-menu-hdr h3 {
  font-family: 'Playfair Display', serif;
  color: var(--gl);
  font-size: 18px;
}
.mobile-menu-close {
  background: none;
  border: none;
  font-size: 24px;
  color: var(--sl);
  cursor: pointer;
}
.mobile-menu-body {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  overflow-y: auto;
}
.mobile-menu-body a {
  color: rgba(255,255,255,0.85);
  text-decoration: none;
  font-size: 14.5px;
  font-weight: 600;
  padding: 6px 0;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}
.mobile-menu-body a:hover {
  color: var(--gl);
}
.mobile-menu-section {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding-left: 12px;
  border-left: 2px solid rgba(255,255,255,0.15);
  margin: 6px 0;
}
.mobile-menu-section-title {
  font-size: 11px;
  text-transform: uppercase;
  color: var(--sl);
  font-weight: 700;
  letter-spacing: 0.08em;
}

/* ── RESPONSIVE MEDIA QUERIES ── */
@media (max-width: 991px) {
  .header-search-wrap {
    max-width: 400px;
  }
}

@media (max-width: 768px) {
  .top-bar, .category-nav, .header-actions .action-link {
    display: none;
  }
  .hamburger-btn {
    display: block;
  }
  .main-header {
    padding: 10px 16px;
    top: 0;
  }
  .main-header-inner {
    gap: 12px;
  }
  .main-header .header-search-wrap {
    display: none;
  }
  .mobile-search-row {
    display: block;
    position: sticky;
    top: 60px;
    z-index: 90;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  }
  .mobile-search-row .header-search-wrap {
    display: flex;
    max-width: 100%;
  }
  .header-actions {
    gap: 12px;
  }
  .header-cart-btn {
    padding: 6px 12px;
  }
  .cart-btn-text {
    display: none; /* Only show icon/badge on mobile */
  }
}
"""

js_mobile_menu = """
// ── MOBILE MENU TOGGLE ──
function toggleMobileMenu(open) {
  const drawer = document.getElementById('mobile-menu-drawer');
  const overlay = document.getElementById('mobile-menu-overlay');
  if (drawer && overlay) {
    if (open) {
      drawer.classList.add('on');
      overlay.classList.add('on');
      document.body.style.overflow = 'hidden';
    } else {
      drawer.classList.remove('on');
      overlay.classList.remove('on');
      document.body.style.overflow = '';
    }
  }
}
"""

# Process all files
for filepath in glob.glob(os.path.join(base_dir, "*.html")):
    basename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update HTML nav block
    # Search for <nav> ... </nav> block
    nav_pattern = r"<nav>.*?</nav>"
    if re.search(nav_pattern, content, re.DOTALL):
        content = re.sub(nav_pattern, new_header_html, content, flags=re.DOTALL)
        print(f"Updated HTML Nav structure in {basename}")
    else:
        print(f"Warning: Could not find <nav> tag in {basename}")

    # 2. Update CSS styles for nav
    css_nav_pattern = r"(/\* ── NAV ── \*/|/\* ── NAV \(matches main site\) ── \*/).*?(?=(/\* ── HERO ── \*/|/\* ── HERO \*/|/\* ── BLOG HERO ── \*/|/\* ── ARTICLE HERO ── \*/))"
    if re.search(css_nav_pattern, content, re.DOTALL):
        content = re.sub(css_nav_pattern, header_css + "\\n\\n", content, flags=re.DOTALL)
        print(f"Updated CSS Nav styles in {basename}")
    else:
        print(f"CSS Nav pattern not matched in {basename}")

    # 3. Add JS toggleMobileMenu function
    if "toggleMobileMenu" not in content:
        if "</script>" in content:
            parts = content.rsplit("</script>", 1)
            content = parts[0] + js_mobile_menu + "</script>" + parts[1]
            print(f"Injected JS toggleMobileMenu in {basename}")

    # 4. Special cases for index.html (header cart total update)
    if basename == "index.html":
        subtotal_replace = """subtotalVal.textContent = `R${subtotal.toFixed(2)}`;
    if (headerTotal) headerTotal.textContent = `R${subtotal.toFixed(2)}`;"""
        content = content.replace("subtotalVal.textContent = `R${subtotal.toFixed(2)}`;", subtotal_replace)
        
        content = content.replace("cntBadge.textContent = totalQty;", """cntBadge.textContent = totalQty;
  const headerTotal = document.getElementById('header-cart-total');
  if (headerTotal) {
    if (cart.length === 0) {
      headerTotal.textContent = 'R0.00';
    }
  }""")
        print("Updated index.html updateCart to update header basket total")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("All headers updated successfully!")
