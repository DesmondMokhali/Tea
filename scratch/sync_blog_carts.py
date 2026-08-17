import os
import re

directory = r"c:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore"

# Find all html files starting with blog
for filename in os.listdir(directory):
    if filename.startswith("blog") and filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Define showCart function and add localStorage sync at the start of DOMContentLoaded
        # We search for the start of DOMContentLoaded event listener
        pattern = r'(//\s*Click toggle for dropdown\s*\n\s*document\.addEventListener\(\s*\'DOMContentLoaded\'\s*,\s*\(\s*\)\s*=>\s*\{\s*)'
        
        replacement = (
            "// ── CART PERSISTENCE & REDIRECT ──\n"
            "function showCart() {\n"
            "  window.location.href = 'index.html?showCart=1';\n"
            "}\n\n"
            "// Click toggle for dropdown\n"
            "document.addEventListener('DOMContentLoaded', () => {\n"
            "  // Sync cart badge and total on load from localStorage\n"
            "  try {\n"
            "    const savedQty = localStorage.getItem('tangren_cart_qty') || '0';\n"
            "    const savedTotal = localStorage.getItem('tangren_cart_total') || '0.00';\n"
            "    const cntBadge = document.getElementById('cnt');\n"
            "    if (cntBadge) cntBadge.textContent = savedQty;\n"
            "    const headerTotal = document.getElementById('header-cart-total');\n"
            "    if (headerTotal) headerTotal.textContent = 'R' + parseFloat(savedTotal).toFixed(2);\n"
            "  } catch (e) {\n"
            "    console.error('Failed to load cart stats:', e);\n"
            "  }\n"
        )
        
        # Check if showCart is already defined in the page to avoid duplicates
        if "function showCart()" in content:
            print(f"{filename} already has showCart, skipping or handling differently")
            continue
            
        new_content, count = re.subn(pattern, replacement, content, flags=re.IGNORECASE)
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Synced cart persistence for {filename}")
        else:
            print(f"Could not find DOMContentLoaded pattern in {filename}")
