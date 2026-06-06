import os
import glob
import re

base_dir = r"C:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore"

for filepath in glob.glob(os.path.join(base_dir, "*.html")):
    basename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False
    
    # 1. Ensure lucide JS script is loaded
    if "lucide.min.js" not in content:
        content = content.replace("</body>", '<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>\n</body>')
        modified = True
        print(f"Added lucide.min.js script to {basename}")

    # 2. Ensure lucide.createIcons() is called on load
    if "lucide.createIcons" not in content:
        if "</script>" in content:
            parts = content.rsplit("</script>", 1)
            content = parts[0] + "\n// Initialize Lucide Icons\nif (typeof lucide !== 'undefined') lucide.createIcons();\n" + "</script>" + parts[1]
            modified = True
            print(f"Added lucide.createIcons() call to {basename}")
        else:
            script_block = '\n<script>\nif (typeof lucide !== "undefined") lucide.createIcons();\n</script>\n'
            content = content.replace("</body>", script_block + "</body>")
            modified = True
            print(f"Created script block with lucide.createIcons() for {basename}")

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

print("Lucide rendering initialized on all pages successfully!")
