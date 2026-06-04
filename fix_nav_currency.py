import os
import glob
import re

base_dir = r'C:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore'

# We replace the Blog dropdown with a simple link
new_blog_nav = '<a href="blog.html">Blog</a>'

for filepath in glob.glob(os.path.join(base_dir, '*.html')):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the Blog dropdown
    content = re.sub(
        r'<div class="nav-dropdown">\s*<a href="blog\.html" class="nav-dropbtn">Blog ▼</a>\s*<div class="nav-dropdown-content">.*?</div>\s*</div>',
        new_blog_nav,
        content,
        flags=re.DOTALL
    )
    
    # Fix the $50 in index.html
    if 'Free Delivery Over $50' in content:
        content = content.replace('Free Delivery Over $50', 'Free Delivery Over R500')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated nav and currency across site.")
