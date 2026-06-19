import os
import re

directory = r"c:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore"

# Find all html files
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Pattern to match: <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"> ... </script>
        pattern = r'<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js">\s*// Initialize Lucide Icons\s*if \(typeof lucide !== \'undefined\'\) lucide.createIcons\(\);\s*</script>'
        
        new_block = '<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>\n<script>\n// Initialize Lucide Icons\nif (typeof lucide !== \'undefined\') lucide.createIcons();\n</script>'
        
        new_content, count = re.subn(pattern, new_block, content, flags=re.IGNORECASE)
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {filename}: replaced {count} occurrence(s).")
        else:
            # Let's try matching with flexible whitespace/newlines just in case
            pattern_flexible = r'<script\s+src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"[^>]*>\s*(//[^\n]*\n)?\s*(if\s*\(typeof\s+lucide\s*!==\s*[\'"]undefined[\'"]\)\s*lucide\.createIcons\(\);)?\s*</script>'
            new_content, count = re.subn(pattern_flexible, new_block, content, flags=re.IGNORECASE)
            if count > 0:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed (flexible) {filename}: replaced {count} occurrence(s).")
            else:
                print(f"No match found in {filename}")
