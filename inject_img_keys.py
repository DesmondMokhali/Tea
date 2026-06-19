"""
Inject 'img' keys into every tcmCatalogDetails entry in index.html.
Maps each product lookup key to its exact filename on GitHub Pages.
"""

img_map = {
    "AN SHEN BU XIN WAN": "AN_SHEN_BU_XIN_WAN_(CALM_SHENSPIRIT).png",
    "BA ZHENG WAN": "BA_ZHENG_WAN_(Clean_Urine).png",
    "BA ZHEN WAN": "BA_ZHEN_WAN_(EIGHT_TONIC_PILLS).png",
    "BAN LONG WAN": "BAN_LONG_WAN_(Tonify_Prime_Yang).png",
    "BAN XIA XIE XIN WAN": "BAN_XIA_XIE_XIN_WAN_(Harmonize_Stomach).png",
    "BAO HE WAN": "BAO_HE_WAN_(Digestion_Aid).png",
    "BI YAN WAN": "Bi_Yan_Wan_(Rhinitis_Pills).png",
    "Bi Yan Wan": "Bi_Yan_Wan_(Rhinitis_Pills).png",
    "BU ZHONG YI QI WAN": "BU_ZHONG_YI_QI_WAN_(Tonify_Center_Qi).png",
    "CHAI HU SHU GAN WAN": "CHAI_HU_SHU_GAN_WAN_(Liver_Harmonize).png",
    "CHUAN XIN LIAN KANG YAN WAN": "CHUAN_XIN_LIAN_KANG_YAN_WAN_(Anti-Inflammation).png",
    "CHUAN XIONG CHA TIAO WAN": "CHUAN_XIONG_CHA_TIAO_WAN_(Head_Clear).png",
    "DA BU YIN WAN": "DA_BU_YIN_WAN_(Nourish_Yin_Plus).png",
    "DANG GUI WAN": "DANG_GUI_WAN_(Angelica_Pills).png",
    "DU HUO JI SHENG WAN": "DU_HUO_JI_SHENG_WAN_(Joint_&_Back_Aid).png",
    "ER CHEN WAN": "ER_CHEN_WAN_(PhlegmDampness).png",
    "FANG FENG TONG SHENG WAN": "FANG_FENG_TONG_SHENG_WAN_(Clear_Heat).png",
    "FU ZHENG FANG": "FU_ZHENG_FANG_(Immune_Aid).png",
    "FU ZI LI ZHONG WAN": "FU_ZI_LI_ZHONG_WAN_(Warm_Middle).png",
    "GAN MAO LING": "GAN_MAO_LING_(Common_Cold).png",
    "GUAN JIE YAN WAN": "GUAN_JIE_YAN_WAN_(Joint_Health).png",
    "GUI PI WAN": "GUI_PI_WAN_(Spleen_Aid).png",
    "GUI ZHI FU LING WAN": "GUI_ZHI_FU_LING_WAN_(Uterus_Stagnation).png",
    "HUAI JIAO WAN": "HUAI_JIAO_WAN_(Sophora_Fruit_Pills).png",
    "HUO XIANG ZHENG QI WAN": "HUO_XIANG_ZHENG_QI_WAN_(Regulate_Stomach).png",
    "JIANG DAN GU CHUAN WAN": "JIANG_DAN_GU_CHUAN_WAN_(Lower_Cholesterol).png",
    "JIANG YA WAN": "JIANG_YA_WAN_(Hypertension_Pills).png",
    "JIA WEI XIAO YAO WAN": "JIA_WEI_XIAO_YAO_WAN_(Ease_Life_Plus).png",
    "JIE GENG WAN": "JIE_GENG_WAN_(Platycodon_Pills).png",
    "JIN GUI SHEN QI WAN": "JIN_GUI_SHEN_QI_WAN_(Kidney_Yang).png",
    "JIN SUO GU JING WAN": "JIN_SUO_GU_JING_WAN_(Control_Emission).png",
    "JIU WEI QIANG HUO WAN": "JIU_WEI_QIANG_HUO_WAN_(Dispel_Wind-Cold).png",
    "KANG GU ZENG SHENG WAN": "KANG_GU_ZENG_SHENG_WAN_(Anti_Hyperosteogeny).png",
    "LIAN QIAO BAI DU WAN": "LIAN_QIAO_BAI_DU_WAN_(Skin_Detox).png",
    "LI DAN PAI SHI WAN": "LI_DAN_PAI_SHI_WAN_(Gallstone).png",
    "LI DAN WAN": "LI_DAN_WAN_(Gallbladder_Heat).png",
    "LI ZHONG WAN": "LI_ZHONG_WAN_(Regulate_Middle).png",
    "LIU WEI DI HUANG WAN": "LIU_WEI_DI_HUANG_WAN_(Nourish_Yin).png",
    "LONG DAN XIE GAN WAN": "LONG_DAN_XIE_GAN_WAN_(Purge_Damp-Heat).png",
    "MAI WEI DI HUANG WAN": "MAI_WEI_DI_HUANG_WAN_(Nourish_Lung_&_Kidney).png",
    "MING MU DI HUANG WAN": "MING_MU_DI_HUANG_WAN_(Eye_Bright).png",
    "MU XIANG SHUN QI WAN": "MU_XIANG_SHUN_QI_WAN_(Reduce_Bloating).png",
    "PIAN TOU TONG WAN": "PIAN_TOU_TONG_WAN_(Migraine_Pill).png",
    "QIAN LIE SHU WAN": "QIAN_LIE_SHU_WAN_(Prostate_Health).png",
    "QING QI HUA TAN WAN": "QING_QI_HUA_TAN_WAN_(Phlegm_Clear).png",
    "QING RE AN CHUANG WAN": "QING_RE_AN_CHUANG_WAN_(Acne_&_Boil).png",
    "QI JU DI HUANG WAN": "QI_JU_DI_HUANG_WAN_(Nourish_Yin_&_Eye).png",
    "SHAO FU ZHU YU WAN": "SHAO_FU_ZHU_YU_WAN_(Abdominal_Stasis).png",
    "SHENG MAI WAN": "SHENG_MAI_WAN_(Generate_Pulse).png",
    "SHEN JING SHUAI RUO WAN": "SHEN_JING_SHUAI_RUO_WAN_(Brain_Tonic_Pills).png",
    "SHEN LING BAI ZHU WAN": "SHEN_LING_BAI_ZHU_WAN_(Consolidate_Digestion).png",
    "SHOU WU WAN": "SHOU_WU_WAN_(_Fo_Ti_Hair_Tonic).png",
    "SI JUN ZI WAN": "SI_JUN_ZI_WAN_(Four_Gentlemen).png",
    "SI MIAO WAN": "SI_MIAO_WAN_(Clear_Dampness).png",
    "SI WU TANG WAN": "SI_WU_TANG_WAN_(Nourish_Blood).png",
    "TAO HONG SI WU WAN": "TAO_HONG_SI_WU_WAN_(Blood_Deficiency_&_Stagnation).png",
    "TE XIAO BI MIN GAN WAN": "TE_XIAO_BI_MIN_GAN_WAN_(Nasal_Allergy).png",
    "TE XIAO JING ZHUI TONG WAN": "TE_XIAO_JING_ZHUI_TONG_WAN_(Neck_Relief).png",
    "TIAN MA GOU TENG WAN": "TIAN_MA_GOU_TENG_WAN_(Liver_Wind_Clear).png",
    "TIAN WANG BU XIN WAN": "TIAN_WANG_BU_XIN_WAN_(Nourish_Heart_Yin).png",
    "TIAO JING CU YUN WAN": "TIAO_JING_CU_YUN_WAN_(Fertility_Aid).png",
    "TONG JING WAN": "TONG_JING_WAN_(Period_Pain_Pills).png",
    "WEN JING WAN": "WEN_JING_WAN_(Warm_Mense).png",
    "WU JI BAI FENG WAN": "WU_JI_BAI_FENG_WAN_(Lady's_Tonic).png",
    "WU LING WAN": "WU_LING_WAN_(Edema_Relief).png",
    "WU ZI YAN ZONG WAN": "WU_ZI_YAN_ZONG_WAN_(Men's_Fertility).png",
    "XIANG SHA LIU JUN WAN": "XIANG_SHA_LIU_JUN_WAN_(Stomach_Harmonize).png",
    "XIANG SHA YANG WEI WAN": "XIANG_SHA_YANG_WEI_WAN_(Stomach_Tonic).png",
    "XIAO CHAI HU TANG WAN": "XIAO_CHAI_HU_TANG_WAN_(Shaoyang_Harmonize).png",
    "XIAO HUO LUO WAN": "XIAO_HUO_LUO_WAN_(Unblock_Meridian).png",
    "XIAO YAO WAN": "XIAO_YAO_WAN_(Ease_Life).png",
    "XUE FU ZHU YU WAN": "XUE_FU_ZHU_YU_WAN_(Blood_Stasis).png",
    "YANG XUE SHENG FA WAN": "YANG_XUE_SHENG_FA_WAN_(Hair_Grow_Pills).png",
    "YU PING FENG WAN": "YU_PING_FENG_WAN_(Protective_Screen).png",
    "ZHEN ZHU AN CHUANG WAN": "ZHEN_ZHU_AN_CHUANG_WAN_(Pearl_Skin).png",
    "ZHI BAI DI HUANG WAN": "ZHI_BAI_DI_HUANG_WAN_(Yin_Deficiency_&_Heat).png",
    "ZHI KE DING CHUAN WAN": "ZHI_KE_DING_CHUAN_WAN_(Wheeze_&_Cough).png",
    "ZHI YANG WAN": "ZHI_YANG_WAN_(Anti_Itching).png",
    "ZHUANG YANG WAN": "ZHUANG_YANG_WAN_(Tonify_Yang).png",
    "ZUO GU SHEN JING TONG WAN": "ZUO_GU_SHEN_JING_TONG_WAN_(Sciatic_Pain).png",
    # Teas with exact filenames
    "ANTI-CANCER TEA": "ANTI-CANCER_TEA.png",
    "ANTI-STRESS SLEEPING TEA": "ANTI-STRESS_SLEEPING_TEA.png",
    "ANTI-VIRUS TEA": "ANTI-VIRUS_TEA.png",
    "GINSENG TEA (SACHETS)": "GINSENG_TEA_(SACHETS).png",
    "GINSENG TEA (TEA BAGS)": "GINSENG_TEA_(TEA_BAGS).png",
}

import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Locate the tcmCatalogDetails block
start_marker = "const tcmCatalogDetails"
block_start = content.find(start_marker)
if block_start == -1:
    print("ERROR: could not find tcmCatalogDetails")
    exit(1)

# For each key in img_map, find the entry and inject img if not present
patched = 0
for key, filename in img_map.items():
    # Match: "KEY (Something)": { ... or "KEY": { ...
    # Let's match the key name followed by any optional characters up to the colon and open brace
    escaped_key = re.escape(key)
    pattern = rf'("{escaped_key}(?:\s*\([^)]+\))?"\s*:\s*\{{)'
    match = re.search(pattern, content[block_start:])
    if not match:
        print(f"  SKIP (not found): {key}")
        continue

    abs_pos = block_start + match.start()
    brace_open = block_start + match.end()  # position just after the opening {

    # Find the matching closing brace
    depth = 1
    i = brace_open
    while i < len(content) and depth > 0:
        if content[i] == '{':
            depth += 1
        elif content[i] == '}':
            depth -= 1
        i += 1
    brace_close = i - 1  # position of the closing }

    entry_body = content[brace_open:brace_close]

    # Skip if img already injected
    if "img:" in entry_body:
        print(f"  ALREADY has img: {key}")
        continue

    # Inject img as the first property
    new_entry_body = f'\n        img: "{filename}",' + entry_body
    content = content[:brace_open] + new_entry_body + content[brace_close:]
    patched += 1
    print(f"  PATCHED: {key} -> {filename}")
    # Recalculate block_start since content length changed
    block_start = content.find(start_marker)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print(f"\nDone. {patched} entries patched.")
