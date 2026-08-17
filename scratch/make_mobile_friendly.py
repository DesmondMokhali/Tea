import os
import glob

base_dir = r"C:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore"

# 1. Update blog posts
blog_responsive_css = """
/* ── MOBILE RESPONSIVENESS OVERRIDES ── */
@media (max-width: 768px) {
  .article-hero { padding: 48px 16px 0; }
  .article-wrap { padding: 32px 16px 60px; }
  .article-body h2 { margin: 36px 0 14px; }
  .article-body p { font-size: 16px; line-height: 1.75; }
  .article-body p:first-child { font-size: 17.5px; }
  .article-body ul li, .article-body ol li { font-size: 15.5px; padding: 6px 0 6px 24px; }
  .comp-matrix { display: block; width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch; }
  .comp-matrix th, .comp-matrix td { padding: 12px 14px; font-size: 13.5px; }
  .remedy-widget { padding: 20px 16px; margin: 32px 0; }
  .remedy-pair { grid-template-columns: 1fr; gap: 12px; }
  .type-a-multi-tier { padding: 20px 16px; margin: 28px 0; }
  .tier-item { flex-direction: column; gap: 12px; align-items: flex-start; padding-bottom: 20px; margin-bottom: 20px; }
  .tier-img { width: 70px; height: 70px; }
  .type-b-focus { padding: 24px 16px; margin: 32px 0; }
  .dialogue-wrap { padding: 20px 16px; margin: 28px 0; }
  .author-box { padding: 20px 16px; flex-direction: column; gap: 12px; }
  .author-ava { width: 48px; height: 48px; }
  .meta-divider { display: none; }
  .hero-meta { gap: 12px; }
}
@media (max-width: 480px) {
  .nlogo .ntext small { display: none; }
  nav { padding: 0 12px; }
  .nav-shop-btn { padding: 6px 12px; font-size: 11.5px; }
}
</style>"""

for filepath in glob.glob(os.path.join(base_dir, "blog-*.html")):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Avoid duplicate append
    if "MOBILE RESPONSIVENESS OVERRIDES" not in content:
        content = content.replace("</style>", blog_responsive_css)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated blog post: {os.path.basename(filepath)}")

# 2. Update blog.html
blog_list_css = """
/* ── MOBILE RESPONSIVENESS OVERRIDES ── */
@media (max-width: 480px) {
  .nlogo .ntext small { display: none; }
  nav { padding: 0 12px; }
  .nblog-cta { padding: 6px 12px; font-size: 11.5px; }
}
</style>"""

with open(os.path.join(base_dir, "blog.html"), "r", encoding="utf-8") as f:
    blog_content = f.read()

if "MOBILE RESPONSIVENESS OVERRIDES" not in blog_content:
    blog_content = blog_content.replace("</style>", blog_list_css)
    with open(os.path.join(base_dir, "blog.html"), "w", encoding="utf-8") as f:
        f.write(blog_content)
    print("Updated blog.html")

# 3. Update index.html
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    index_content = f.read()

# Replace the responsive styling block in index.html with a more comprehensive one
old_responsive = """/* ── RESPONSIVE ── */
@media(max-width:780px){
  .hero{grid-template-columns:1fr}
  .himg-wrap{display:none}
  .modal{grid-template-columns:1fr}
  .mimgcol{display:none}
  .nlinks{display:none}
  .swrap input{width:130px}
  .swrap input:focus{width:155px}
}
@media(max-width:460px){
  .mcol{padding:18px}
  .mprow{gap:6px}
  .mstock{margin-left:0}
}"""

new_responsive = """/* ── RESPONSIVE ── */
@media(max-width:780px){
  .hero{grid-template-columns:1fr; padding: 40px 24px;}
  .himg-wrap{display:none}
  .modal{grid-template-columns:1fr; max-height: 95vh;}
  .mimgcol{display:flex; min-height:240px; height:240px;}
  .mimgcol .mimg{width:100%; height:100%; padding:16px;}
  .mcol{max-height: calc(95vh - 240px);}
  .nlinks{display:none}
  .swrap input{width:110px}
  .swrap input:focus{width:130px}
}
@media(max-width:480px){
  nav { padding: 0 12px; }
  .nlogo .ntext small { display: none; }
  .swrap input { width: 90px; }
  .swrap input:focus { width: 110px; }
  .cbtn { padding: 6px 12px; font-size: 11.5px; }
  .mcol{padding:18px}
  .mprow{gap:6px}
  .mstock{margin-left:0}
}"""

if old_responsive in index_content:
    index_content = index_content.replace(old_responsive, new_responsive)
    with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_content)
    print("Updated index.html responsive styles")
else:
    print("Could not find the exact old_responsive CSS block in index.html, searching partially...")
    # fallback partial match if it changed slightly
    if "/* ── RESPONSIVE ── */" in index_content:
        # We can append or replace
        print("Responsive header found in index.html")
