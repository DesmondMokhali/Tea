import os, glob, re

base_dir = r"C:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore"

# New correct nav block with URL params - to apply on ALL html files
new_nav = """  <div class="nlinks">
    <a href="index.html">Home</a>
    <div class="nav-dropdown">
      <a href="index.html?filter=all#ga" class="nav-dropbtn">Products &#9660;</a>
      <div class="nav-dropdown-content">
        <a href="index.html?filter=all#ga">All Products</a>
        <a href="index.html?filter=teas#ga">Herbal Teas</a>
        <a href="index.html?filter=pills#ga">Herbal Pills</a>
      </div>
    </div>
    <a href="blog.html">Blog</a>
    <a href="index.html#contact">Contact Us</a>
  </div>"""

updated = 0
for filepath in glob.glob(os.path.join(base_dir, "*.html")):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    orig = content
    # Replace any nlinks block that doesn't already have the URL params
    content = re.sub(
        r'<div class="nlinks">.*?</div>(?=\s*(?:</div>)?\s*<div class="nright">)',
        new_nav,
        content,
        flags=re.DOTALL
    )
    if content != orig:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        updated += 1
        print(f"  Fixed: {os.path.basename(filepath)}")

print(f"\nNav updated in {updated} files.")
