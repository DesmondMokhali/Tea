import os
import re

base_dir = r"C:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore"
filepath = os.path.join(base_dir, "index.html")

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update the CSS for the Hero Carousel (colors, styling, banners, label under image, dischem font)
new_hero_css = """/* ── HERO CAROUSEL ── */
.hero-carousel {
  position: relative;
  overflow: hidden;
  min-height: 480px;
}
.hero-track {
  display: flex;
  transition: transform 0.65s cubic-bezier(0.4,0,0.2,1);
  will-change: transform;
}
.hero-slide {
  min-width: 100%;
  padding: clamp(36px,5vw,75px) clamp(16px,5vw,80px);
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 48px;
  align-items: center;
  position: relative;
  overflow: hidden;
}

/* Background Color/Gradient Themes for Slides to attract customers */
.hero-slide.theme-metabolic { background: linear-gradient(135deg, #1b3d2b 0%, #11271b 100%); }
.hero-slide.theme-drainage { background: linear-gradient(135deg, #2b1f3d 0%, #171122 100%); }
.hero-slide.theme-cognitive { background: linear-gradient(135deg, #3d2b1f 0%, #251a13 100%); }
.hero-slide.theme-hormone { background: linear-gradient(135deg, #44182a 0%, #2c0f1b 100%); }
.hero-slide.theme-spinal { background: linear-gradient(135deg, #112d3d 0%, #0a1b25 100%); }
.hero-slide.theme-seasonal { background: linear-gradient(135deg, #443510 0%, #2a200a 100%); }

.hero-slide::after {
  content:'';position:absolute;top:-120px;right:-80px;
  width:480px;height:480px;
  background:radial-gradient(circle,rgba(255,255,255,0.06) 0%,transparent 70%);
  pointer-events:none;
}
.hero-text { position: relative; z-index: 1; }

/* Subheading / Label styling - NO BORDER, put under images style */
.hero-badge-clean {
  display: inline-block;
  font-size: 11px;
  color: var(--gl);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  font-weight: 700;
  margin-bottom: 12px;
}

.hero-urgency-clean {
  display: inline-block;
  font-size: 11px;
  color: #ff5c5c;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  font-weight: 700;
  margin-bottom: 12px;
  animation: pulse-urg 2s ease-in-out infinite;
}

@keyframes pulse-urg {
  0%,100%{opacity: 0.8;}
  50%{opacity: 1; color: #ff8e8e;}
}

/* Heading Font style changed to match Dischem (Montserrat font hierarchy) */
.hero-slide h1 {
  font-family: 'Montserrat', 'DM Sans', sans-serif;
  font-size: clamp(26px, 3.2vw, 42px);
  font-weight: 800;
  color: #fff;
  line-height: 1.15;
  margin-bottom: 15px;
  letter-spacing: -0.02em;
  text-transform: uppercase;
}
.hero-slide h1 em { color: var(--gl); font-style: normal; font-weight: 800; }
.hero-slide .hsub {
  font-size: clamp(13px,1.3vw,15px);
  color: rgba(255,255,255,.75);
  margin-bottom: 28px;
  max-width: 540px;
  line-height: 1.7;
}

/* Action button area containing 1 or 2 CTAs */
.hero-action-row {
  display: flex;
  align-items: center;
  gap: 15px;
  flex-wrap: wrap;
}
.hero-price-tag {
  font-family: 'Montserrat', sans-serif;
  font-size: 20px;
  font-weight: 800;
  color: var(--gl);
  margin-right: 5px;
}

.hero-slide .btnp {
  background: var(--g);color: var(--f);border:none;border-radius:6px;
  padding: 13px 24px;font-family: 'Montserrat', sans-serif;
  font-size: 13px;font-weight: 800;cursor:pointer;
  transition:all var(--tr);letter-spacing:.04em;text-transform: uppercase;
  display:inline-flex;align-items:center;gap:8px;
}
.hero-slide .btnp svg { width:15px;height:15px;stroke:currentColor;stroke-width:2.5;fill:none;flex-shrink:0; }
.hero-slide .btnp:hover { background:var(--gl);transform:translateY(-2px);box-shadow:0 6px 20px rgba(200,160,110,.4); }

.hero-slide .btno {
  background:transparent;color:#fff;border:1.5px solid rgba(255,255,255,.3);
  border-radius:6px;padding:12px 20px;font-family: 'Montserrat', sans-serif;
  font-size: 12.5px;font-weight: 700;cursor:pointer;transition:all var(--tr);
  text-transform: uppercase;letter-spacing: .04em;
}
.hero-slide .btno:hover { border-color:rgba(255,255,255,.8);background:rgba(255,255,255,.1); }

/* Creative styling for Actual Product Images */
.hero-imgs {
  position:relative;
  z-index:1;
  display:flex;
  align-items:center;
  justify-content:center;
  height: 280px;
}
/* Stacked layout for creative positioning */
.hero-img-stack-left {
  position: absolute;
  left: 5%;
  top: 15%;
  z-index: 2;
  transform: rotate(-6deg);
  transition: transform 0.3s ease;
}
.hero-img-stack-right {
  position: absolute;
  right: 5%;
  bottom: 10%;
  z-index: 3;
  transform: rotate(8deg);
  transition: transform 0.3s ease;
}
.hero-img-stack-center {
  position: absolute;
  left: 35%;
  top: 5%;
  z-index: 4;
  transform: scale(1.08) rotate(-2deg);
  transition: transform 0.3s ease;
}
.hero-imgs:hover .hero-img-stack-left { transform: rotate(-12deg) scale(1.03); }
.hero-imgs:hover .hero-img-stack-right { transform: rotate(15deg) scale(1.03); }
.hero-imgs:hover .hero-img-stack-center { transform: scale(1.12) rotate(2deg); }

.hero-img-box {
  width: 140px;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 12px;
  padding: 10px;
  text-align: center;
  backdrop-filter: blur(10px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}
.hero-img-box img {
  width: 100%;
  height: 120px;
  object-fit: contain;
  display: block;
  margin: 0 auto 8px;
}
/* Clean under-image description details instead of frame borders */
.hero-img-desc {
  font-size: 10px;
  font-weight: 700;
  color: rgba(255,255,255,0.9);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  line-height: 1.3;
}
.hero-img-label-under {
  font-size: 9px;
  color: var(--gl);
  margin-top: 2px;
  display: block;
}

/* Carousel controls */
.hero-dots {
  position:absolute;bottom:16px;left:50%;transform:translateX(-50%);
  display:flex;gap:7px;z-index:10;
}
.hero-dot {
  width:8px;height:8px;border-radius:50%;
  background:rgba(255,255,255,.28);border:none;cursor:pointer;
  transition:all var(--tr);padding:0;
}
.hero-dot.active { background:var(--g);transform:scale(1.25); }
.hero-arrow {
  position:absolute;top:50%;transform:translateY(-50%);
  width:38px;height:38px;border-radius:50%;
  background:rgba(255,255,255,.1);border:1.5px solid rgba(255,255,255,.2);
  color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;
  transition:all var(--tr);z-index:10;backdrop-filter:blur(6px);
}
.hero-arrow:hover { background:rgba(200,160,110,.25);border-color:var(--g); }
.hero-arrow svg { width:16px;height:16px;stroke:currentColor;stroke-width:2;fill:none; }
.hero-prev { left:16px; }
.hero-next { right:16px; }

@media(max-width:991px){
  .hero-slide { grid-template-columns:1fr; padding:40px 24px; gap: 30px; }
  .hero-imgs { height: 260px; max-width: 450px; margin: 0 auto; }
  .hero-img-box { width: 120px; padding: 8px; }
  .hero-img-box img { height: 95px; }
}
@media(max-width:480px){
  .hero-img-box { width: 100px; }
  .hero-img-box img { height: 80px; }
  .hero-img-desc { font-size: 9px; }
}
"""

# Replace the css block
css_pattern = r'/\* ── HERO CAROUSEL ── \*/.*?(?=(/\* ── TRUST BAR ── \*/|/\* ── TRUST BAR ── \*/))'
content = re.sub(css_pattern, new_hero_css + '\n', content, flags=re.DOTALL)
print("Updated Hero Carousel CSS with Dischem styled Montserrat typography, stack layouts, clean margins, and theme categories.")

# 2. Update the Hero Slide Banners HTML
new_hero_html = """<!-- ── HERO CAROUSEL ── -->
<section class="hero-carousel" id="hero-carousel">
  <div class="hero-track" id="hero-track">

    <!-- SLIDE 1: Metabolic (Bao He Wan + Abdomen Slimming) -->
    <div class="hero-slide theme-metabolic">
      <div class="hero-text">
        <div class="hero-badge-clean">Metabolic Bundle &nbsp;·&nbsp; Digestive System</div>
        <h1>RE-ENGINEER YOUR<br><em>AFTERNOON METABOLISM</em></h1>
        <p class="hsub">The Post-Meal Shield: Pair Bao He Wan's rapid enzyme support with our clean Abdomen Slimming blend to completely clear food stagnation, eliminate bloating, and maintain sharp focus after heavy meals.</p>
        <div class="hero-action-row">
          <span class="hero-price-tag">R182.90</span>
          <button class="btnp" onclick="addBundleByNames('BAO HE WAN','ABDOMEN SLIMMING')">
            <i data-lucide="shopping-cart" style="width:15px;height:15px;margin-right:5px"></i> Add to Cart
          </button>
          <button class="btno" onclick="window.location.href='index.html?filter=teas#ga'">Shop Teas</button>
          <button class="btno" onclick="window.location.href='index.html?filter=pills#ga'">Shop Pills</button>
        </div>
      </div>
      <div class="hero-imgs">
        <div class="hero-img-box hero-img-stack-left">
          <img src="assets/images/BAO_HE_WAN_(Digestion_Aid).png" alt="Bao He Wan" onerror="this.style.opacity='.2'">
          <div class="hero-img-desc">Bao He Wan</div>
          <span class="hero-img-label-under">Digestion Aid</span>
        </div>
        <div class="hero-img-box hero-img-stack-right">
          <img src="https://lh3.googleusercontent.com/sitesv/AA5AbUCnDpi6L-ErodxLB8fdtWWc3A8GdHGocrfjH3YkCr5gMHrKQ_s5NgoMAfox43_-pjgFYf0CzOQZzWPuS3VBsoVJUbHQ-fRJsWcs3TV_-z4wp1ZR7AoN_VOdSV_kBXSDmQ7qtoCDy_vgAXtKNuUSArGzjnYaHLkujk-7Ev1T8LOIY4TPFe38qFXwY_X_2ILVlxjW0NoC8p2IAsjRuZi0gvK_YdepStO9sEVaiWM=w1280" alt="Abdomen Slimming Tea" onerror="this.style.opacity='.2'">
          <div class="hero-img-desc">Abdomen Slim</div>
          <span class="hero-img-label-under">Herbal Tea</span>
        </div>
      </div>
    </div>

    <!-- SLIDE 2: Fluid Drainage (Slim Tea + White Gourd Slim Tea) -->
    <div class="hero-slide theme-drainage">
      <div class="hero-text">
        <div class="hero-urgency-clean">Flash Offer &mdash; Expires 15 June 2026</div>
        <h1>IT'S NOT STUBBORN FAT.<br><em>IT'S FLUID STAGNATION.</em></h1>
        <p class="hsub">Stop punishing your system with extreme fasting. Flush out heavy, uncomfortable water weight and clear internal dampness with our targeted Slim &amp; White Gourd dual botanical protocol.</p>
        <div class="hero-action-row">
          <span class="hero-price-tag">R125.00</span>
          <button class="btnp" onclick="addBundleByNames('SLIM TEA','WHITE GOURD')">
            <i data-lucide="shopping-cart" style="width:15px;height:15px;margin-right:5px"></i> Add to Cart
          </button>
          <button class="btno" onclick="window.location.href='index.html?filter=teas#ga'">Shop Teas</button>
        </div>
      </div>
      <div class="hero-imgs">
        <div class="hero-img-box hero-img-stack-left">
          <img src="https://lh3.googleusercontent.com/sitesv/AA5AbUDr4VV4aRkyAIjiI13-hIYox43z5qvePL0XwIsCFEHET8S5z7zVpXFiNL7awi7XJNLSI5g4WdrWbjuZ_NSfkxTRYOyv0iDjjd_AsNpa5VeFn6BYR4h-53DkdZW5DYLFIo05mQAfOGSyGxkEO0i60Qfeff7OlcJAdDgy49ODKwozauXNrl3Vx2vkb-GOoOmOixGSwJrwNNpv4IS4BYuP3DllzoPmGMX2xGNe0Zc=w1280" alt="Slim Tea" onerror="this.style.opacity='.2'">
          <div class="hero-img-desc">Slim Tea</div>
          <span class="hero-img-label-under">Detox Blend</span>
        </div>
        <div class="hero-img-box hero-img-stack-right">
          <img src="https://lh3.googleusercontent.com/sitesv/AA5AbUCBhy491qsK0r_YW7Y1HVhA2ZjgYM12airfn2nhgy3woSlgDqV0iYNEJcLzj6EeMHAgGDOf2ea2AcN0xCJfibVDYS0CZw75uYq0e7lQoDR1QyhQ-F72eFHkGH4d64cYiFg_2M8g7Eaogeq09oDvmnoZTjuek7soOhNOgV5BbZnei8umfXJ4_TjzG7k2lWPzBqhBjDKBjIj9dq7uKpEenLkZhCEAWL0aZv2Y0E0=w1280" alt="White Gourd Slim Tea" onerror="this.style.opacity='.2'">
          <div class="hero-img-desc">White Gourd Slim</div>
          <span class="hero-img-label-under">Herbal Tea</span>
        </div>
      </div>
    </div>

    <!-- SLIDE 3: Cognitive (Gui Pi Wan + Ginseng Date + Kuding Tea) -->
    <div class="hero-slide theme-cognitive">
      <div class="hero-text">
        <div class="hero-badge-clean">Cognitive Performance Stack &nbsp;·&nbsp; Spleen Qi</div>
        <h1>STOP BORROWING STAMINA<br><em>WITH COFFEE JITTERS</em></h1>
        <p class="hsub">Pure Spleen Qi Recovery + Adaptogenic Clarity. Rebuild your baseline nervous system stamina with a structured daily routine that eliminates the afternoon crash entirely.</p>
        <div class="hero-action-row">
          <span class="hero-price-tag">R247.90</span>
          <button class="btnp" onclick="addBundleByNames('GUI PI WAN','GINSENG DATE','KUDING')">
            <i data-lucide="shopping-cart" style="width:15px;height:15px;margin-right:5px"></i> Add to Cart
          </button>
          <button class="btno" onclick="window.location.href='index.html?filter=all#ga'">Shop All Products</button>
        </div>
      </div>
      <div class="hero-imgs">
        <div class="hero-img-box hero-img-stack-left">
          <img src="assets/images/GUI_PI_WAN_(Spleen_Aid).png" alt="Gui Pi Wan" onerror="this.style.opacity='.2'">
          <div class="hero-img-desc">Gui Pi Wan</div>
          <span class="hero-img-label-under">Spleen Aid</span>
        </div>
        <div class="hero-img-box hero-img-stack-center">
          <img src="https://lh3.googleusercontent.com/sitesv/AA5AbUBMTy5lqB2Mqj_bGl745XTU2iP6WuU2Ge6_W126DNqh8xpU1jX_PPi5oOiTw_yNoaIoc3GboFnTVye5pmrxX8OpH_Ubq-8YOd2DPDMPkbWiszm9Fnm8eNYkGS5PPL_VhwsOgSG9HGHSoeSjDXNiKUhOAGgR8kuFl6B6WifAgFaW8NvnoKNjGaD5FTiX1iOC9jCOqp4Sp1lHUA7saJmLKA024iuUfRXHevZw=w1280" alt="Ginseng Date Tea" onerror="this.style.opacity='.2'">
          <div class="hero-img-desc">Ginseng Date</div>
          <span class="hero-img-label-under">Herbal Tea</span>
        </div>
        <div class="hero-img-box hero-img-stack-right">
          <img src="https://lh3.googleusercontent.com/sitesv/AA5AbUAgIMIQRdrUMuoVtmmrN4kIXyN7nFuH4srQCDB2NtPVTAoCF3HxmQ3Zfa8tPC06KjgSM-ZMglcpI3e2oDOsGD4Yt3sCK7SFrmC_mpg2K9hZLMjCkB9VTHR4NbBrmkUX-lJ-G8hKZ6-kcPLLLkYghsxOAJAJ3dPpMrbdZaIJMKAuW_fhAa4Rnh8NO2-RetztTf8qISMT9_n3ojDDRSzsSP_PRuPHUpgjEdftulY=w1280" alt="Kuding Tea" onerror="this.style.opacity='.2'">
          <div class="hero-img-desc">Kuding Tea</div>
          <span class="hero-img-label-under">Clearance Tea</span>
        </div>
      </div>
    </div>

    <!-- SLIDE 4: Hormone Balance (Chai Hu Shu Gan + Ba Zhen) -->
    <div class="hero-slide theme-hormone">
      <div class="hero-text">
        <div class="hero-badge-clean">Women's Hormone Balance Protocol</div>
        <h1>ACHIEVE A STATE OF FLOW.<br><em>NOT MONTHLY BURNOUT.</em></h1>
        <p class="hsub">Nourish deep blood iron reserves while smoothing out internal emotional friction. A powerful twin-pill strategy engineered to eliminate painful cycle stagnation and restore predictable energy.</p>
        <div class="hero-action-row">
          <span class="hero-price-tag">R239.90</span>
          <button class="btnp" onclick="addBundleByNames('CHAI HU SHU GAN','BA ZHEN')">
            <i data-lucide="shopping-cart" style="width:15px;height:15px;margin-right:5px"></i> Add to Cart
          </button>
          <button class="btno" onclick="window.location.href='index.html?filter=pills#ga'">Shop Pills</button>
        </div>
      </div>
      <div class="hero-imgs">
        <div class="hero-img-box hero-img-stack-left">
          <img src="assets/images/CHAI_HU_SHU_GAN_WAN_(Liver_Harmonize).png" alt="Chai Hu Shu Gan Wan" onerror="this.style.opacity='.2'">
          <div class="hero-img-desc">Chai Hu Shu Gan</div>
          <span class="hero-img-label-under">Liver Flow</span>
        </div>
        <div class="hero-img-box hero-img-stack-right">
          <img src="assets/images/BA_ZHEN_WAN_(EIGHT_TONIC_PILLS).png" alt="Ba Zhen Wan" onerror="this.style.opacity='.2'">
          <div class="hero-img-desc">Ba Zhen Wan</div>
          <span class="hero-img-label-under">Eight Tonics</span>
        </div>
      </div>
    </div>

    <!-- SLIDE 5: Spinal Joint (Te Xiao + Du Huo) -->
    <div class="hero-slide theme-spinal">
      <div class="hero-text">
        <div class="hero-badge-clean">Spinal &amp; Joint Relief Protocol</div>
        <h1>ERASE THE PHYSICAL GRIND<br><em>FROM YOUR SPINAL NERVES</em></h1>
        <p class="hsub">Dredge deep channel stagnation caused by prolonged sitting. This specialized combo warms up connective tissues and clears micro-circulation paths to alleviate lumbar and cervical compression.</p>
        <div class="hero-action-row">
          <span class="hero-price-tag">R239.90</span>
          <button class="btnp" onclick="addBundleByNames('TE XIAO','DU HUO')">
            <i data-lucide="shopping-cart" style="width:15px;height:15px;margin-right:5px"></i> Add to Cart
          </button>
          <button class="btno" onclick="window.location.href='index.html?filter=pills#ga'">Shop Pills</button>
        </div>
      </div>
      <div class="hero-imgs">
        <div class="hero-img-box hero-img-stack-left">
          <img src="assets/images/TE_XIAO_JING_ZHUI_TONG_WAN_(Neck_Relief).png" alt="Te Xiao Neck Relief" onerror="this.style.opacity='.2'">
          <div class="hero-img-desc">Te Xiao Neck</div>
          <span class="hero-img-label-under">Neck Relief</span>
        </div>
        <div class="hero-img-box hero-img-stack-right">
          <img src="assets/images/DU_HUO_JI_SHENG_WAN_(Joint_&_Back_Aid).png" alt="Du Huo Ji Sheng Wan" onerror="this.style.opacity='.2'">
          <div class="hero-img-desc">Du Huo Joint</div>
          <span class="hero-img-label-under">Back &amp; Joint</span>
        </div>
      </div>
    </div>

    <!-- SLIDE 6: Seasonal Defense (Anti-Virus Tea + Chuan Xin Lian) -->
    <div class="hero-slide theme-seasonal">
      <div class="hero-text">
        <div class="hero-urgency-clean">Seasonal Defense Stock &mdash; Priority Access Expires 31 July 2026</div>
        <h1>THE INVISIBLE PROTECTION<br><em>SHIELD FOR YOUR HOUSEHOLD</em></h1>
        <p class="hsub">Active Defensive Qi (Wei-Qi) Support + Deep Lung Clearing. Formulate a strong, daily physical baseline that keeps changing seasons, city dust, and airborne bugs out of your system.</p>
        <div class="hero-action-row">
          <span class="hero-price-tag">R179.90</span>
          <button class="btnp" onclick="addBundleByNames('ANTI-VIRUS TEA','CHUAN XIN')">
            <i data-lucide="shopping-cart" style="width:15px;height:15px;margin-right:5px"></i> Add to Cart
          </button>
          <button class="btno" onclick="window.location.href='index.html?filter=teas#ga'">Shop Teas</button>
          <button class="btno" onclick="window.location.href='index.html?filter=pills#ga'">Shop Pills</button>
        </div>
      </div>
      <div class="hero-imgs">
        <div class="hero-img-box hero-img-stack-left">
          <img src="https://lh3.googleusercontent.com/sitesv/AA5AbUD9lYp01SdoUPuGBqHKebS_7QO5ThDNRRuGpBVoQcH9tNZLMh4pHwd5G-QOmj1QWj1t8ier64O6KVBBV1ko-IcYtQmiw6JthKhMnX8R0FuwJvHkelYBRRemc8187jsFYhUEwv75MtqKwh2d1vOeCTHPGXyUsWE32QoQ53QDg6FqGS5vxfkIa56Hs9CMHyeqNzJAhRdvlf-GuHbk7dp8n997fJXRShDJmjUfnsc=w1280" alt="Anti-Virus Tea" onerror="this.style.opacity='.2'">
          <div class="hero-img-desc">Anti-Virus</div>
          <span class="hero-img-label-under">Defensive Tea</span>
        </div>
        <div class="hero-img-box hero-img-stack-right">
          <img src="assets/images/CHUAN_XIN_LIAN_KANG_YAN_WAN_(Anti-Inflammation).png" alt="Chuan Xin Lian" onerror="this.style.opacity='.2'">
          <div class="hero-img-desc">Chuan Xin Lian</div>
          <span class="hero-img-label-under">Defensive Pill</span>
        </div>
      </div>
    </div>

  </div><!-- end .hero-track -->"""

# Replace the HTML content block
html_pattern = r'<!-- ── HERO CAROUSEL ── -->.*?<!-- end \.hero-track -->'
content = re.sub(html_pattern, new_hero_html, content, flags=re.DOTALL)
print("Updated Hero Carousel HTML with product bundles, price tags, creative stack layout, and multi-CTA options.")

# 3. Update the Javascript parameters (set transition timer to 10 seconds / 10000ms)
content = content.replace("setInterval(function(){ heroMove(1); }, 6000)", "setInterval(function(){ heroMove(1); }, 10000)")
content = content.replace("heroGoTo(idx) {\n  _hIdx = (idx + _hTotal) % _hTotal;\n  const track = document.getElementById('hero-track');\n  if (track) track.style.transform = 'translateX(-' + (_hIdx * 100) + '%)';\n  document.querySelectorAll('.hero-dot').forEach(function(d, i){ d.classList.toggle('active', i === _hIdx); });\n  clearInterval(_hAuto);\n  _hAuto = setInterval(function(){ heroMove(1); }, 6000);\n}", "heroGoTo(idx) {\n  _hIdx = (idx + _hTotal) % _hTotal;\n  const track = document.getElementById('hero-track');\n  if (track) track.style.transform = 'translateX(-' + (_hIdx * 100) + '%)';\n  document.querySelectorAll('.hero-dot').forEach(function(d, i){ d.classList.toggle('active', i === _hIdx); });\n  clearInterval(_hAuto);\n  _hAuto = setInterval(function(){ heroMove(1); }, 10000);\n}")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved index.html hero upgrades successfully!")
