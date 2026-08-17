import os
import glob
import re

base_dir = r"C:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore"

new_nlinks = (
    '  <div class="nlinks">\n'
    '    <a href="index.html">Home</a>\n'
    '    <div class="nav-dropdown">\n'
    '      <a href="index.html?filter=all#ga" class="nav-dropbtn">Products &#9660;</a>\n'
    '      <div class="nav-dropdown-content">\n'
    '        <a href="index.html?filter=all#ga">All Products</a>\n'
    '        <a href="index.html?filter=teas#ga">Herbal Teas</a>\n'
    '        <a href="index.html?filter=pills#ga">Herbal Pills</a>\n'
    '      </div>\n'
    '    </div>\n'
    '    <a href="blog.html">Blog</a>\n'
    '    <a href="index.html#contact">Contact Us</a>\n'
    '  </div>\n'
)

updated = 0
for filepath in glob.glob(os.path.join(base_dir, "*.html")):
    fname = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    orig = content
    content = re.sub(
        r'<div class="nlinks">.*?</div>\s*(?=<a[^>]*nav-shop-btn|</nav>)',
        new_nlinks,
        content,
        flags=re.DOTALL
    )
    if content != orig:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        updated += 1
        print("Updated: " + fname)

print("Done. Updated " + str(updated) + " files.")
