import os
import glob
import re

base_dir = r"C:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore"

css_rule = """
.nav-dropdown:hover .nav-dropdown-content,
.nav-dropdown.open .nav-dropdown-content {
  display: block;
}
"""

js_code = """
  // Toggle nav dropdowns on click/tap (especially for touch screens)
  document.querySelectorAll('.nav-dropdown').forEach(dropdown => {
    const btn = dropdown.querySelector('.nav-dropbtn');
    if (btn) {
      btn.addEventListener('click', (e) => {
        if (window.innerWidth <= 991 || ('ontouchstart' in window)) {
          e.preventDefault();
          e.stopPropagation();
          const isOpen = dropdown.classList.contains('open');
          document.querySelectorAll('.nav-dropdown').forEach(d => d.classList.remove('open'));
          if (!isOpen) {
            dropdown.classList.add('open');
          }
        }
      });
    }
  });

  // Close dropdown when clicking outside
  document.addEventListener('click', () => {
    document.querySelectorAll('.nav-dropdown').forEach(dropdown => {
      dropdown.classList.remove('open');
    });
  });
"""

updated = 0
for filepath in glob.glob(os.path.join(base_dir, "*.html")):
    if "index.html" in filepath:
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    original = content
    
    # 1. Update CSS: replace ".nav-dropdown:hover .nav-dropdown-content { display: block; }" or similar
    # with the one supporting ".nav-dropdown.open"
    content = re.sub(
        r'\.nav-dropdown:hover\s*\.nav-dropdown-content\s*\{\s*display:\s*block;?\s*\}',
        css_rule.strip(),
        content
    )
    
    # 2. Update JS: find DOMContentLoaded or another script block and insert the click handler
    if "document.querySelectorAll('.nav-dropdown').forEach" not in content:
        # Find the last inline script tag
        inline_script_matches = list(re.finditer(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', content, re.DOTALL))
        if inline_script_matches:
            last_match = inline_script_matches[-1]
            script_block = last_match.group(0)
            script_inner = last_match.group(1)
            
            # Let's insert at the beginning of DOMContentLoaded listener if it exists, or just inside the script tag
            dom_loaded_match = re.search(r"document\.addEventListener\('DOMContentLoaded',\s*\(\)\s*=>\s*\{", script_inner)
            if dom_loaded_match:
                insert_idx = dom_loaded_match.end()
                new_inner = script_inner[:insert_idx] + js_code + script_inner[insert_idx:]
                new_script_block = script_block.replace(script_inner, new_inner)
                content = content[:last_match.start()] + new_script_block + content[last_match.end():]
            else:
                # otherwise just append it
                new_inner = script_inner + f"\n// Click toggle for dropdown\ndocument.addEventListener('DOMContentLoaded', () => {{ {js_code} }});\n"
                new_script_block = script_block.replace(script_inner, new_inner)
                content = content[:last_match.start()] + new_script_block + content[last_match.end():]

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        updated += 1
        print(f"Updated dropdown logic in: {os.path.basename(filepath)}")

print(f"\nCompleted. Updated {updated} files.")
