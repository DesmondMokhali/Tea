import os
import glob

base_dir = r"C:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore"

old_block = """    <div class="top-bar-left">
      <span>📞 Careline: +27 (0) 11 888 3000</span>
      <span class="bar-sep">|</span>
      <span>🌿 Free Delivery on Orders Over R500</span>
    </div>"""

new_block = """    <div class="top-bar-left">
      <span><i data-lucide="phone" style="width:12px;height:12px;display:inline-block;vertical-align:middle;margin-right:5px;color:var(--gl)"></i>Careline: +27 (0) 11 888 3000</span>
      <span class="bar-sep">|</span>
      <span><i data-lucide="truck" style="width:12px;height:12px;display:inline-block;vertical-align:middle;margin-right:5px;color:var(--gl)"></i>Free Delivery on Orders Over R500</span>
    </div>"""

for filepath in glob.glob(os.path.join(base_dir, "*.html")):
    basename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if old_block in content:
        content = content.replace(old_block, new_block)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Replaced emojis with icons in {basename}")
    else:
        # Fallback if whitespace differs
        print(f"Warning: Could not find exact top-bar-left block in {basename}")

print("Emoji replacement complete!")
