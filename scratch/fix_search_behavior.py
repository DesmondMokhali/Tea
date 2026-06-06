import os
import glob
import re

base_dir = r"C:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore"

# 1. Update index.html to read ?search= URL param
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    index_content = f.read()

init_pattern = r"const filterParam = urlParams\.get\('filter'\);.*?(?=}\);)"
new_init = """const filterParam = urlParams.get('filter');
  const searchParam = urlParams.get('search');
  
  if(filterParam === 'teas' || filterParam === 'pills' || filterParam === 'all') {
    setType(filterParam);
  } else {
    renderGrid();
  }
  
  if(searchParam) {
    const searchInput = document.getElementById('si');
    const mobileSearchInput = document.getElementById('si-mobile');
    if (searchInput) searchInput.value = searchParam;
    if (mobileSearchInput) mobileSearchInput.value = searchParam;
    doSearch(searchParam);
  }"""

if "searchParam = urlParams.get('search')" not in index_content:
    index_content = re.sub(init_pattern, new_init, index_content, flags=re.DOTALL)
    with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_content)
    print("Updated index.html URL Search initialization")

# 2. Add search redirection script and click listener to blog pages
search_redirect_js = """
// ── REDIRECT HEADER SEARCH TO STORE ──
function triggerHeaderSearch() {
  const si = document.getElementById('si');
  const sim = document.getElementById('si-mobile');
  const val = (si && si.value) || (sim && sim.value) || '';
  if (val.trim()) {
    window.location.href = 'index.html?search=' + encodeURIComponent(val.trim());
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const handleEnter = (e) => {
    if (e.key === 'Enter') {
      triggerHeaderSearch();
    }
  };
  const si = document.getElementById('si');
  const sim = document.getElementById('si-mobile');
  if (si) si.addEventListener('keypress', handleEnter);
  if (sim) sim.addEventListener('keypress', handleEnter);
});
"""

for filepath in glob.glob(os.path.join(base_dir, "*.html")):
    basename = os.path.basename(filepath)
    if basename == "index.html":
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Update search button onclick action
    content = content.replace(
        'onclick="doSearch(document.getElementById(\'si\').value)"',
        'onclick="triggerHeaderSearch()"'
    )
    
    # Inject redirection script
    if "triggerHeaderSearch" not in content:
        if "</script>" in content:
            parts = content.rsplit("</script>", 1)
            content = parts[0] + search_redirect_js + "</script>" + parts[1]
            print(f"Added search redirection logic to {basename}")
            
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Search behavior optimized successfully!")
