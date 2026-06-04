import os
import glob
import re

base_dir = r'C:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore'

new_nav = """  <div class="nlinks">
    <a href="index.html">Home</a>
    <div class="nav-dropdown">
      <a href="index.html" class="nav-dropbtn">Products ▼</a>
      <div class="nav-dropdown-content">
        <a href="index.html#ga">Herbal Teas</a>
        <a href="index.html#ga">Herbal Pills</a>
      </div>
    </div>
    <div class="nav-dropdown">
      <a href="blog.html" class="nav-dropbtn">Blog ▼</a>
      <div class="nav-dropdown-content">
        <a href="blog.html">All Articles</a>
        <a href="blog-weight-management.html">Weight Management</a>
        <a href="blog-mens-health.html">Men's Health</a>
        <a href="blog-womens-health.html">Women's Health</a>
        <a href="blog-immunity.html">Immunity Shielding</a>
        <a href="blog-pain-relief.html">Pain Relief & Muscles</a>
        <a href="blog-senior-wellness.html">Senior Wellness</a>
        <a href="blog-childrens-health.html">Children's Health</a>
        <a href="blog-maternity-care.html">Pregnancy & Maternity</a>
        <a href="blog-bone-joint.html">Bone & Joint Strength</a>
        <a href="blog-heart-health.html">Blood & Heart Health</a>
      </div>
    </div>
    <a href="#contact">Contact Us</a>
  </div>"""

count = 0
for filepath in glob.glob(os.path.join(base_dir, '*.html')):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'<div class="nlinks">.*?</div>', new_nav, content, flags=re.DOTALL)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
print(f"Updated navigation in {count} HTML files.")
