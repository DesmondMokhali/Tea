import os
import re

blog_html_path = r'C:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore\blog.html'

with open(blog_html_path, 'r', encoding='utf-8') as f:
    content = f.read()

articles_data = [
    {"file": "blog-deep-sleep.html", "cat": "sleep", "cat_name": "Sleep & Anxiety", "title": "The Blueprint for Deep Sleep: Why Tea and Herbs Work Faster Together", "img": "assets/images/blog_sleep_tea.png", "desc": "Science now confirms what TCM has known for centuries — combining adaptogenic herbs with bedtime rituals deepens REM cycles.", "date": "2 June 2025", "author": "Dr. Lin Wei", "tags": "sleep anxiety insomnia"},
    {"file": "blog-tcm-101.html", "cat": "education", "cat_name": "Herbal Education", "title": "TCM 101: A Beginner's Guide to Chinese Herbal Medicine", "img": "assets/images/blog_detox_water.png", "desc": "Discover the foundational principles of Traditional Chinese Medicine. Learn about Qi, Yin and Yang, and natural balance.", "date": "3 June 2025", "author": "Mei Huang, MHSc", "tags": "education basic qi yin yang"},
    {"file": "blog-herbal-formulas.html", "cat": "education", "cat_name": "Herbal Education", "title": "The Architecture of Healing: How TCM Formulas Are Built", "img": "assets/images/blog_vitality_herbs.png", "desc": "Discover the ancient architecture of Chinese herbal formulas. Learn about the King, Minister, Assistant, and Courier herbs.", "date": "3 June 2025", "author": "Mei Huang, MHSc", "tags": "education formulas theory"},
    {"file": "blog-evidence-based.html", "cat": "education", "cat_name": "Herbal Education", "title": "The Science of Herbal Synergy: Evidence-Based Validation", "img": "assets/images/blog_liver_detox.png", "desc": "Explore the modern scientific research behind Traditional Chinese Medicine formulas and botanical synergy.", "date": "3 June 2025", "author": "Dr. Lin Wei", "tags": "education science research"},
    {"file": "blog-weight-management.html", "cat": "weight", "cat_name": "Weight Management", "title": "The Post-Meal Metabolic Hack: Supporting Fast Fat Digestion Daily", "img": "assets/images/SLIMMING_TEA.png", "desc": "Learn how to break down heavy fats and prevent weight storage right after lunch or dinner with this simple daily habit.", "date": "4 June 2025", "author": "Clinic Team", "tags": "weight fat metabolism diet"},
    {"file": "blog-mens-health.html", "cat": "mens", "cat_name": "Men's Health", "title": "The Modern Man's Tonic: Restoring Deep Physical Reserve and Drive", "img": "assets/images/unnamed(12).png", "desc": "High-stress work and physical exhaustion deplete core male vitality. Here is the daily energy-building ritual you need.", "date": "4 June 2025", "author": "Clinic Team", "tags": "mens vitality energy testosterone"},
    {"file": "blog-womens-health.html", "cat": "womens", "cat_name": "Women's Health", "title": "Balancing Your Cycle: The Daily Herbal Routine for Smooth Transitions", "img": "assets/images/unnamed(41).png", "desc": "Manage hormonal shifts, PMS discomfort, and mood swings while building iron-rich blood health naturally.", "date": "4 June 2025", "author": "Clinic Team", "tags": "womens hormones period pms"},
    {"file": "blog-immunity.html", "cat": "immunity", "cat_name": "Immunity Shielding", "title": "The Daily Invisible Shield: Keeping Flu Out of Your Household", "img": "assets/images/ANTI-VIRUS_TEA.png", "desc": "Build a strong daily defense grid so cold and flu strains never take root in your household.", "date": "4 June 2025", "author": "Clinic Team", "tags": "immunity flu cold defense"},
    {"file": "blog-pain-relief.html", "cat": "pain", "cat_name": "Pain & Muscles", "title": "Erasing the Grind: Relieving Lower Back and Nerve Tension Safely", "img": "assets/images/JOINT_CARE_TEA.png", "desc": "Perfect for people dealing with everyday body aches from sitting long hours at computers, gym recovery, or manual work.", "date": "4 June 2025", "author": "Clinic Team", "tags": "pain muscle back nerve tension"},
    {"file": "blog-senior-wellness.html", "cat": "senior", "cat_name": "Senior Wellness", "title": "Golden Years Vitality: Gentle Daily Support for Stiff Joints and Clear Minds", "img": "assets/images/unnamed(43).png", "desc": "Tailored for older adults looking to maintain independent mobility, warm up cold limbs, and support memory.", "date": "4 June 2025", "author": "Clinic Team", "tags": "senior joints aging memory"},
    {"file": "blog-childrens-health.html", "cat": "kids", "cat_name": "Children's Health", "title": "Natural Focus and Gentle Tummies: The Safe Way to Nurture Growing Kids", "img": "assets/images/unnamed(16).png", "desc": "Helping parents find safe, plant-based remedies to boost their children's attention spans and ease stomach aches.", "date": "4 June 2025", "author": "Clinic Team", "tags": "kids children focus tummy"},
    {"file": "blog-maternity-care.html", "cat": "maternity", "cat_name": "Maternity Care", "title": "The Gentle Maternity Guide: Safe, Soothing Herbs for Expectant Mothers", "img": "assets/images/ROSE_TEA.png", "desc": "Educating mothers on what is safe to drink during and after pregnancy to soothe nausea and reduce swollen ankles.", "date": "4 June 2025", "author": "Clinic Team", "tags": "maternity pregnancy nausea"},
    {"file": "blog-bone-joint.html", "cat": "bone", "cat_name": "Bone & Joint", "title": "Feeding Your Skeleton: How Herbs Protect Your Knees and Spine", "img": "assets/images/unnamed(6).png", "desc": "Traditional root extracts supply the deep nourishment needed to rebuild joint fluids and strengthen bone density.", "date": "4 June 2025", "author": "Clinic Team", "tags": "bone joint knee spine"},
    {"file": "blog-heart-health.html", "cat": "heart", "cat_name": "Heart & Blood", "title": "The Oxygen Highway: Maximizing Clean Blood Flow and Cardiovascular Health", "img": "assets/images/BLOOD_CLEANING_TEA.png", "desc": "Vital for managing high cholesterol or fighting cold fingers and toes caused by poor daily circulation.", "date": "4 June 2025", "author": "Clinic Team", "tags": "heart blood pressure circulation"}
]

cats = set([a['cat_name'] for a in articles_data])
cat_opts = '\n'.join([f'<option value="{c.lower().replace(" ", "-")}">{c}</option>' for c in sorted(cats)])

new_filter_section = f"""
<!-- ── FILTER & GRID ── -->
<section class="filter-section" id="articles">
  <div class="filter-header" style="display:flex; justify-content:space-between; align-items:flex-end; flex-wrap:wrap; gap:16px;">
    <div>
      <h2>All <span>Articles</span></h2>
      <span class="article-count" id="article-count">{len(articles_data)} articles</span>
    </div>
    
    <div class="blog-filter-dropdown">
      <label for="category-select" style="font-size:12px; font-weight:600; color:var(--muted); text-transform:uppercase; margin-right:8px;">Filter by Goal:</label>
      <select id="category-select" onchange="setFilter(this.value)" style="padding:10px 16px; border:1px solid var(--border); border-radius:8px; font-family:inherit; font-size:14px; font-weight:600; color:var(--text); background:var(--card); cursor:pointer; outline:none; box-shadow:0 2px 8px rgba(0,0,0,0.05);">
        <option value="all">All Goals & Articles</option>
        {cat_opts}
      </select>
    </div>
  </div>

  <div class="article-grid" id="article-grid">
"""

for a in articles_data:
    cat_val = a["cat_name"].lower().replace(" ", "-")
    new_filter_section += f"""
    <article class="art-card" data-cat="{cat_val}" data-tags="{a["tags"]}">
      <div class="card-img-wrap">
        <img src="{a["img"]}" alt="{a["title"]}" loading="lazy" onerror="this.style.background='linear-gradient(135deg,#c8e6c9,#a5d6a7)'">
        <div class="card-cat-badge badge-{cat_val}" style="background:var(--green); color:#fff; border:none; padding:4px 10px; border-radius:99px; font-size:10px; font-weight:700;">
          {a["cat_name"]}
        </div>
      </div>
      <div class="card-body">
        <div class="card-cat-text" style="color:var(--green); font-size:11px; font-weight:700; text-transform:uppercase; margin-bottom:8px;">{a["cat_name"]}</div>
        <h3 class="card-title">{a["title"]}</h3>
        <p class="card-excerpt">{a["desc"]}</p>
        <div class="card-divider"></div>
        <div class="card-footer">
          <div class="card-author-row">
            <div class="card-avatar"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.58-7 8-7s8 3 8 7"/></svg></div>
            <div class="card-meta-text">
              <span class="card-author">{a["author"]}</span>
              <span class="card-date">{a["date"]}</span>
            </div>
          </div>
          <a href="{a["file"]}" class="card-read-btn">
            Read Article
            <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
        </div>
      </div>
    </article>
    """

new_filter_section += """
    <div class="no-results" id="no-results" style="display:none">
      <div class="no-results-icon">🌿</div>
      <h3>No articles found</h3>
      <p>Try a different filter.</p>
    </div>
  </div>
</section>
"""

# Replace the entire filter-section and filter-tabs
content = re.sub(r'<!-- ── FILTER & GRID ── -->.*?</section>', new_filter_section, content, flags=re.DOTALL)

# Update Javascript setFilter function
new_js = """
function setFilter(cat) {
  const cards = document.querySelectorAll('.art-card');
  let count = 0;
  cards.forEach(c => {
    if (cat === 'all' || c.getAttribute('data-cat') === cat) {
      c.style.display = 'block';
      count++;
    } else {
      c.style.display = 'none';
    }
  });
  document.getElementById('article-count').textContent = count + (count === 1 ? ' article' : ' articles');
  document.getElementById('no-results').style.display = count === 0 ? 'flex' : 'none';
}
</script>
"""

content = re.sub(r'function setFilter\(cat\).*?</script>', new_js, content, flags=re.DOTALL)

with open(blog_html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("blog.html rebuilt successfully!")
