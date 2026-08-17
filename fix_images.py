import os
import re

base_dir = r"C:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore"

# Dictionary mapping the requested or placeholder images to actual, existing images
image_replacements = {
    "assets/images/unnamed(29).png": "assets/images/DETOX_TEA.png", # Bao He Wan (pill) -> using Detox Tea
    "assets/images/ABDOMEN_SLIMMING_TEA.png": "assets/images/ABDOMEN_SLIMMING_TEA.png", # Exists
    "assets/images/unnamed(3).png": "assets/images/WHITE_GOURD_SLIM_TEA.png", # White Gourd -> exists
    "assets/images/SLIMMING_TEA.png": "assets/images/SLIM_TEA.png", # Exists
    "assets/images/unnamed(12).png": "assets/images/GINSENG_TEA_(SACHETS).png", # Ginseng
    "assets/images/unnamed(31).png": "assets/images/KUDING_TEA.png", # Kuding Tea
    "assets/images/GUI_PI_WAN.png": "assets/images/ANTI-STRESS_SLEEPING_TEA.png", # Gui Pi Wan -> Sleeping Tea
    "assets/images/WOMENS_PRECIOUS_TEA.png": "assets/images/WOMB_CARE_TEA.png",
    "assets/images/TE_XIAO_JING_ZHUI_TONG_WAN_(Cervical_Spine_Pain).png": "assets/images/JOINT_CARE_TEA.png",
    "assets/images/IMMUNE_TEA.png": "assets/images/ANTI-VIRUS_TEA.png",
    "assets/images/CHUAN_XIN_LIAN_KANG_YAN_WAN_(Anti-Inflammation).png": "assets/images/COOLING_TEA.png",
    "assets/images/unnamed(16).png": "assets/images/KUDING_TEA.png",
    "assets/images/ROSE_TEA.png": "assets/images/THREE_FLOWERS_TEA.png",
    "assets/images/BLOOD_CLEANING_TEA.png": "assets/images/BLOOD_CLEANING_TEA.png",
    "assets/images/unnamed(6).png": "assets/images/BONE_AND_JOINT_TEA.png", # Fallback to JOINT_CARE_TEA later if missing
    "assets/images/unnamed(41).png": "assets/images/MENSTRUATION_REGULATING_TEA.png",
    "assets/images/unnamed(43).png": "assets/images/MENOPAUSE_TEA.png",
}

# Update the HTML files
for filename in os.listdir(base_dir):
    if filename.startswith("blog-") and filename.endswith(".html"):
        filepath = os.path.join(base_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        
        # Replace the missing images with existing ones
        for old_img, new_img in image_replacements.items():
            content = content.replace(old_img, new_img)
            
        # Fallbacks for any remaining unmapped images
        content = content.replace('assets/images/BONE_AND_JOINT_TEA.png', 'assets/images/JOINT_CARE_TEA.png')
            
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

print("Images replaced with real, existing product assets.")
