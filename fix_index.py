import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update numeric indexes in loadDynamicCatalog
old_name_logic = 'let name = item["Product"] || item["n"] || item["product"] || item[0];'
new_name_logic = 'let name = item["Product"] || item["n"] || item["product"] || item[0] || item["0"];'
content = content.replace(old_name_logic, new_name_logic)

old_price_logic = 'let rawPrice = item["Retail price"] || item.p || 0;'
new_price_logic = 'let rawPrice = item["Retail price"] || item.p || item[1] || item["1"] || 0;'
content = content.replace(old_price_logic, new_price_logic)

# 2. Fix dynamic image name generation to replace () with _
old_img_logic = "const safeNameForUrl = name.replace(/[^a-zA-Z0-9 -]/g, '').replace(/ /g, '_');"
new_img_logic = "const safeNameForUrl = name.replace(/[()]/g, '_').replace(/[^a-zA-Z0-9 _-]/g, '').replace(/_+/g, '_');"
content = content.replace(old_img_logic, new_img_logic)

# 3. Replace all static images/ with assets/images/
content = re.sub(r'src="images/', 'src="assets/images/', content)

# 4. Remove parentheses from static image paths
def strip_parens(match):
    return match.group(0).replace('(', '_').replace(')', '_').replace('__', '_')
content = re.sub(r'src="assets/images/[^"]+"', strip_parens, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Replacements complete.')
