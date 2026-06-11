import os
import glob
import re

base_dir = r"C:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore"

# The toggleMobileMenu function content to add
menu_js_code = """
// ── MOBILE MENU FUNCTION ──
function toggleMobileMenu(isOpen) {
  const overlay = document.getElementById('mobile-menu-overlay');
  const drawer = document.getElementById('mobile-menu-drawer');
  if (overlay && drawer) {
    if (isOpen) {
      overlay.classList.add('on');
      drawer.classList.add('on');
      document.body.style.overflow = 'hidden';
    } else {
      overlay.classList.remove('on');
      drawer.classList.remove('on');
      document.body.style.overflow = '';
    }
  }
}
"""

updated = 0
for filepath in glob.glob(os.path.join(base_dir, "*.html")):
    # skip index.html since we already edited it
    if "index.html" in filepath:
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "function toggleMobileMenu" in content:
        print(f"Skipping (already exists): {os.path.basename(filepath)}")
        continue
        
    # We want to find the last inline <script> tag (that doesn't have src)
    # and append our code inside it before the closing </script>
    inline_script_matches = list(re.finditer(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', content, re.DOTALL))
    
    if inline_script_matches:
        # Get the last inline script tag
        last_match = inline_script_matches[-1]
        script_block = last_match.group(0) # <script>...</script>
        script_inner = last_match.group(1) # content inside
        
        # Append our function before the closing tag
        new_script_block = script_block.replace(script_inner, script_inner + menu_js_code)
        
        content = content[:last_match.start()] + new_script_block + content[last_match.end():]
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        updated += 1
        print(f"Added menu toggle to: {os.path.basename(filepath)}")
    else:
        print(f"No inline script block found in: {os.path.basename(filepath)}")

print(f"\nCompleted. Updated {updated} files.")
