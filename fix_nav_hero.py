import os
import re
import glob

base_dir = r"C:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore"

# ── 1. GLOBAL NAV: remove "Our Teas" orphan link, fix Products dropdown to trigger JS filter
old_nav_block = """      <div class="nlinks">
    <a href="index.html">Home</a>
    <div class="nav-dropdown">
      <a href="index.html" class="nav-dropbtn">Products ▼</a>
      <div class="nav-dropdown-content">
        <a href="index.html#ga">Herbal Teas</a>
        <a href="index.html#ga">Herbal Pills</a>
      </div>
    </div>
    <a href="blog.html">Blog</a>
    <a href="#contact">Contact Us</a>
  </div>
    </div>
    <a href="index.html#ga">Our Teas</a>
  </div>"""

new_nav_block = """  <div class="nlinks">
    <a href="index.html">Home</a>
    <div class="nav-dropdown">
      <a href="index.html#ga" class="nav-dropbtn">Products ▼</a>
      <div class="nav-dropdown-content">
        <a href="index.html#ga" onclick="if(window.setType){setTimeout(()=>setType('all'),100)}">All Products</a>
        <a href="index.html#ga" onclick="if(window.setType){setTimeout(()=>setType('teas'),100)}">Herbal Teas</a>
        <a href="index.html#ga" onclick="if(window.setType){setTimeout(()=>setType('pills'),100)}">Herbal Pills</a>
      </div>
    </div>
    <a href="blog.html">Blog</a>
    <a href="#contact">Contact Us</a>
  </div>"""

# ── 2. HERO BADGE: Replace the generic sparkles badge with something premium
old_badge = '<div class="hbadge"><i data-lucide="sparkles" style="width:14px;height:14px"></i> Featured Tea of the Season</div>'
new_badge = '<div class="hbadge"><span class="hbadge-dot"></span> Practitioner\'s Choice &nbsp;·&nbsp; Winter 2025</div>'

# ── 3. View All Teas button → more specific
old_view_btn = 'View All Teas ↓'
new_view_btn = 'Browse All Teas ↓'

# ── 4. Update CSS for premium badge styling (inject into </style>)
badge_css = """
/* ── PREMIUM BADGE ── */
.hbadge {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: rgba(255,255,255,0.75);
  border: 1px solid rgba(255,255,255,0.2);
  background: rgba(255,255,255,0.06);
  backdrop-filter: blur(8px);
  padding: 7px 16px;
  border-radius: 99px;
  margin-bottom: 20px;
}
.hbadge-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #7ecb8f;
  box-shadow: 0 0 0 3px rgba(126,203,143,0.3);
  animation: pulse-dot 2s ease-in-out infinite;
}
@keyframes pulse-dot {
  0%, 100% { box-shadow: 0 0 0 3px rgba(126,203,143,0.3); }
  50% { box-shadow: 0 0 0 6px rgba(126,203,143,0.1); }
}
</style>"""

for filepath in glob.glob(os.path.join(base_dir, "*.html")):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # Fix nav
    content = content.replace(old_nav_block, new_nav_block)

    # Fix hero badge (only in index.html)
    if os.path.basename(filepath) == "index.html":
        content = content.replace(old_badge, new_badge)
        content = content.replace(old_view_btn, new_view_btn)
        # Inject CSS for badge
        if '.hbadge-dot' not in content:
            content = content.replace('</style>', badge_css)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {os.path.basename(filepath)}")

print("All done.")
