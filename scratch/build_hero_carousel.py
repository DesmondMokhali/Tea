import os
import re

base_dir = r"C:\Users\Mokhali\Desktop\Data scapping\Tangren Pharmaceutical Group - Herbal Teas_files\teastore"
filepath = os.path.join(base_dir, "index.html")

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# ── 1. NEW HERO CSS ──────────────────────────────────────────────────────────
new_hero_css = """/* ── HERO CAROUSEL ── */
.hero-carousel {
  position: relative;
  overflow: hidden;
  background: linear-gradient(140deg,#0e2018 0%,var(--f) 55%,var(--fm) 100%);
  min-height: 420px;
}
.hero-track {
  display: flex;
  transition: transform 0.65s cubic-bezier(0.4,0,0.2,1);
  will-change: transform;
}
.hero-slide {
  min-width: 100%;
  padding: clamp(36px,5vw,70px) clamp(16px,5vw,80px);
  display: grid;
  grid-template-columns: 1fr 420px;
  gap: 48px;
  align-items: center;
  position: relative;
  overflow: hidden;
}
.hero-slide::after {
  content:'';position:absolute;top:-120px;right:-80px;
  width:480px;height:480px;
  background:radial-gradient(circle,rgba(200,160,110,.1) 0%,transparent 70%);
  pointer-events:none;
}
.hero-text { position: relative; z-index: 1; }
.hero-badge {
  display: inline-flex;align-items:center;gap:8px;
  background:rgba(200,160,110,.13);border:1px solid rgba(200,160,110,.28);
  border-radius:20px;padding:5px 14px;
  font-size:11px;color:var(--gl);letter-spacing:.09em;text-transform:uppercase;
  margin-bottom:14px;
}
.hero-badge svg { width:12px;height:12px;stroke:currentColor;stroke-width:2;fill:none;flex-shrink:0; }
.hero-urgency-badge {
  display:inline-flex;align-items:center;gap:8px;
  background:rgba(220,50,50,.18);border:1px solid rgba(220,80,80,.35);
  border-radius:20px;padding:5px 14px;
  font-size:11px;color:#f87171;letter-spacing:.09em;text-transform:uppercase;
  margin-bottom:14px;
  animation: pulse-urg 2s ease-in-out infinite;
}
.hero-urgency-badge svg { width:12px;height:12px;stroke:currentColor;stroke-width:2;fill:none;flex-shrink:0; }
@keyframes pulse-urg {
  0%,100%{box-shadow:0 0 0 0 rgba(220,50,50,0)}
  50%{box-shadow:0 0 0 6px rgba(220,50,50,0.08)}
}
.hero-slide h1 {
  font-family:'Playfair Display',serif;
  font-size:clamp(24px,3.4vw,46px);
  font-weight:700;color:#fff;line-height:1.15;
  margin-bottom:10px;letter-spacing:-.01em;
}
.hero-slide h1 em { color:var(--gl);font-style:italic; }
.hero-slide .hsub {
  font-size:clamp(13px,1.3vw,15.5px);color:rgba(255,255,255,.65);
  margin-bottom:24px;max-width:500px;line-height:1.75;
}
.hero-slide .hbtns { display:flex;gap:10px;flex-wrap:wrap; }
.hero-slide .btnp {
  background:var(--g);color:var(--f);border:none;border-radius:8px;
  padding:13px 26px;font-family:'DM Sans',sans-serif;
  font-size:14px;font-weight:700;cursor:pointer;
  transition:all var(--tr);letter-spacing:.02em;
  display:inline-flex;align-items:center;gap:8px;
}
.hero-slide .btnp svg { width:15px;height:15px;stroke:currentColor;stroke-width:2;fill:none;flex-shrink:0; }
.hero-slide .btnp:hover { background:var(--gl);transform:translateY(-2px);box-shadow:0 8px 24px rgba(200,160,110,.4); }
.hero-slide .btno {
  background:transparent;color:#fff;border:1.5px solid rgba(255,255,255,.28);
  border-radius:8px;padding:12px 20px;font-family:'DM Sans',sans-serif;
  font-size:13.5px;font-weight:500;cursor:pointer;transition:all var(--tr);
}
.hero-slide .btno:hover { border-color:rgba(255,255,255,.65);background:rgba(255,255,255,.05); }

/* Slide images */
.hero-imgs { position:relative;z-index:1;display:flex;align-items:center;justify-content:center;gap:16px; }
.hero-img-frame {
  flex:1;max-width:190px;aspect-ratio:4/5;
  border-radius:16px;overflow:hidden;
  background:rgba(255,255,255,.06);border:1.5px solid rgba(200,160,110,.25);
  display:flex;align-items:center;justify-content:center;position:relative;
}
.hero-img-frame img { width:88%;height:88%;object-fit:contain;display:block;position:relative;z-index:1; }
.hero-img-frame .img-label {
  position:absolute;bottom:0;left:0;right:0;
  background:linear-gradient(to top,rgba(0,0,0,.6),transparent);
  padding:8px 10px 7px;
  font-size:9.5px;font-weight:700;color:rgba(255,255,255,.85);
  letter-spacing:.05em;text-transform:uppercase;line-height:1.3;
}
.hero-img-plus {
  font-size:26px;color:var(--g);font-weight:300;opacity:.8;flex-shrink:0;
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

@media(max-width:780px){
  .hero-slide { grid-template-columns:1fr;padding:32px 20px 28px; }
  .hero-imgs { margin-top:12px; }
  .hero-img-frame { max-width:130px; }
  .hero-slide h1 { font-size:clamp(22px,6vw,32px); }
}
@media(max-width:460px){
  .hero-img-frame { max-width:105px; }
  .hero-img-plus { font-size:18px; }
}
"""

# ── 2. NEW HERO HTML ─────────────────────────────────────────────────────────
new_hero_html = """<!-- ── HERO CAROUSEL ── -->
<section class="hero-carousel" id="hero-carousel">
  <div class="hero-track" id="hero-track">

    <!-- SLIDE 1: Post-Meal Metabolic Shield -->
    <div class="hero-slide">
      <div class="hero-text">
        <div class="hero-badge">
          <svg viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
          Metabolic Bundle · Digestive System
        </div>
        <h1>RE-ENGINEER YOUR<br><em>AFTERNOON METABOLISM</em></h1>
        <p class="hsub">The Post-Meal Shield: Pair Bao He Wan's rapid enzyme support with our clean Abdomen Slimming blend to completely clear food stagnation, eliminate bloating, and maintain sharp focus after heavy meals.</p>
        <div class="hbtns">
          <button class="btnp" onclick="addBundleByNames('BAO HE WAN','ABDOMEN SLIMMING')">
            <svg viewBox="0 0 24 24"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
            Bundle Both — Free SA Delivery Over R600
          </button>
          <button class="btno" onclick="document.getElementById('ga').scrollIntoView({behavior:'smooth'})">Browse All Products</button>
        </div>
      </div>
      <div class="hero-imgs">
        <div class="hero-img-frame">
          <img src="assets/images/BAO_HE_WAN_(Digestion_Aid).png" alt="Bao He Wan" onerror="this.src='';this.style.opacity='.2'">
          <div class="img-label">Bao He Wan · Digestion Aid</div>
        </div>
        <span class="hero-img-plus">+</span>
        <div class="hero-img-frame">
          <img src="https://lh3.googleusercontent.com/sitesv/AA5AbUCnDpi6L-ErodxLB8fdtWWc3A8GdHGocrfjH3YkCr5gMHrKQ_s5NgoMAfox43_-pjgFYf0CzOQZzWPuS3VBsoVJUbHQ-fRJsWcs3TV_-z4wp1ZR7AoN_VOdSV_kBXSDmQ7qtoCDy_vgAXtKNuUSArGzjnYaHLkujk-7Ev1T8LOIY4TPFe38qFXwY_X_2ILVlxjW0NoC8p2IAsjRuZi0gvK_YdepStO9sEVaiWM=w1280" alt="Abdomen Slimming Tea" onerror="this.src='';this.style.opacity='.2'">
          <div class="img-label">Abdomen Slimming Tea</div>
        </div>
      </div>
    </div>

    <!-- SLIDE 2: Fluid Drainage Protocol (URGENCY) -->
    <div class="hero-slide">
      <div class="hero-text">
        <div class="hero-urgency-badge">
          <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          Flash Offer — Expires 15 June 2026
        </div>
        <h1>IT'S NOT STUBBORN FAT.<br><em>IT'S FLUID STAGNATION.</em></h1>
        <p class="hsub">Stop punishing your system with extreme fasting. Flush out heavy, uncomfortable water weight and clear internal dampness with our targeted Slim & White Gourd dual botanical protocol.</p>
        <div class="hbtns">
          <button class="btnp" onclick="addBundleByNames('SLIM TEA','WHITE GOURD')">
            <svg viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
            Flash Bundle — Tap to Add to Basket
          </button>
          <button class="btno" onclick="document.getElementById('ga').scrollIntoView({behavior:'smooth'})">Browse All Teas</button>
        </div>
      </div>
      <div class="hero-imgs">
        <div class="hero-img-frame">
          <img src="https://lh3.googleusercontent.com/sitesv/AA5AbUDr4VV4aRkyAIjiI13-hIYox43z5qvePL0XwIsCFEHET8S5z7zVpXFiNL7awi7XJNLSI5g4WdrWbjuZ_NSfkxTRYOyv0iDjjd_AsNpa5VeFn6BYR4h-53DkdZW5DYLFIo05mQAfOGSyGxkEO0i60Qfeff7OlcJAdDgy49ODKwozauXNrl3Vx2vkb-GOoOmOixGSwJrwNNpv4IS4BYuP3DllzoPmGMX2xGNe0Zc=w1280" alt="Slim Tea" onerror="this.src='';this.style.opacity='.2'">
          <div class="img-label">Slim Tea</div>
        </div>
        <span class="hero-img-plus">+</span>
        <div class="hero-img-frame">
          <img src="https://lh3.googleusercontent.com/sitesv/AA5AbUCBhy491qsK0r_YW7Y1HVhA2ZjgYM12airfn2nhgy3woSlgDqV0iYNEJcLzj6EeMHAgGDOf2ea2AcN0xCJfibVDYS0CZw75uYq0e7lQoDR1QyhQ-F72eFHkGH4d64cYiFg_2M8g7Eaogeq09oDvmnoZTjuek7soOhNOgV5BbZnei8umfXJ4_TjzG7k2lWPzBqhBjDKBjIj9dq7uKpEenLkZhCEAWL0aZv2Y0E0=w1280" alt="White Gourd Slim Tea" onerror="this.src='';this.style.opacity='.2'">
          <div class="img-label">White Gourd Slim Tea</div>
        </div>
      </div>
    </div>

    <!-- SLIDE 3: Sustained Cognitive Battery -->
    <div class="hero-slide">
      <div class="hero-text">
        <div class="hero-badge">
          <svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 10 10"/><path d="M12 6v6l4 2"/></svg>
          Cognitive Performance Stack
        </div>
        <h1>STOP BORROWING STAMINA<br><em>WITH COFFEE JITTERS</em></h1>
        <p class="hsub">Pure Spleen Qi Recovery + Adaptogenic Clarity. Rebuild your baseline nervous system stamina with a structured daily routine that eliminates the afternoon crash entirely.</p>
        <div class="hbtns">
          <button class="btnp" onclick="addBundleByNames('GUI PI WAN','GINSENG DATE')">
            <svg viewBox="0 0 24 24"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
            Retool Your System — Instant Checkout
          </button>
          <button class="btno" onclick="document.getElementById('ga').scrollIntoView({behavior:'smooth'})">Browse All</button>
        </div>
      </div>
      <div class="hero-imgs">
        <div class="hero-img-frame">
          <img src="assets/images/GUI_PI_WAN_(Spleen_Aid).png" alt="Gui Pi Wan" onerror="this.src='';this.style.opacity='.2'">
          <div class="img-label">Gui Pi Wan</div>
        </div>
        <span class="hero-img-plus">+</span>
        <div class="hero-img-frame">
          <img src="https://lh3.googleusercontent.com/sitesv/AA5AbUBMTy5lqB2Mqj_bGl745XTU2iP6WuU2Ge6_W126DNqh8xpU1jX_PPi5oOiTw_yNoaIoc3GboFnTVye5pmrxX8OpH_Ubq-8YOd2DPDMPkbWiszm9Fnm8eNYkGS5PPL_VhwsOgSG9HGHSoeSjDXNiKUhOAGgR8kuFl6B6WifAgFaW8NvnoKNjGaD5FTiX1iOC9jCOqp4Sp1lHUA7saJmLKA024iuUfRXHevZw=w1280" alt="Ginseng Date Tea" onerror="this.src='';this.style.opacity='.2'">
          <div class="img-label">Ginseng Date Tea</div>
        </div>
        <span class="hero-img-plus">+</span>
        <div class="hero-img-frame">
          <img src="https://lh3.googleusercontent.com/sitesv/AA5AbUAgIMIQRdrUMuoVtmmrN4kIXyN7nFuH4srQCDB2NtPVTAoCF3HxmQ3Zfa8tPC06KjgSM-ZMglcpI3e2oDOsGD4Yt3sCK7SFrmC_mpg2K9hZLMjCkB9VTHR4NbBrmkUX-lJ-G8hKZ6-kcPLLLkYghsxOAJAJ3dPpMrbdZaIJMKAuW_fhAa4Rnh8NO2-RetztTf8qISMT9_n3ojDDRSzsSP_PRuPHUpgjEdftulY=w1280" alt="Kuding Tea" onerror="this.src='';this.style.opacity='.2'">
          <div class="img-label">Kuding Tea</div>
        </div>
      </div>
    </div>

    <!-- SLIDE 4: 28-Day Internal Flow Alignment -->
    <div class="hero-slide">
      <div class="hero-text">
        <div class="hero-badge">
          <svg viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
          Women's Hormone Balance Protocol
        </div>
        <h1>ACHIEVE A STATE OF FLOW.<br><em>NOT MONTHLY BURNOUT.</em></h1>
        <p class="hsub">Nourish deep blood iron reserves while smoothing out internal emotional friction. A powerful twin-pill strategy engineered to eliminate painful cycle stagnation and restore predictable energy.</p>
        <div class="hbtns">
          <button class="btnp" onclick="addBundleByNames('CHAI HU SHU GAN','BA ZHEN')">
            <svg viewBox="0 0 24 24"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
            Harmonize Your System — Free Shipping
          </button>
          <button class="btno" onclick="document.getElementById('ga').scrollIntoView({behavior:'smooth'})">Browse Herbal Pills</button>
        </div>
      </div>
      <div class="hero-imgs">
        <div class="hero-img-frame">
          <img src="assets/images/CHAI_HU_SHU_GAN_WAN_(Liver_Harmonize).png" alt="Chai Hu Shu Gan Wan" onerror="this.src='';this.style.opacity='.2'">
          <div class="img-label">Chai Hu Shu Gan Wan</div>
        </div>
        <span class="hero-img-plus">+</span>
        <div class="hero-img-frame">
          <img src="assets/images/BA_ZHEN_WAN_(EIGHT_TONIC_PILLS).png" alt="Ba Zhen Wan" onerror="this.src='';this.style.opacity='.2'">
          <div class="img-label">Ba Zhen Wan</div>
        </div>
      </div>
    </div>

    <!-- SLIDE 5: Lumbar & Desk Compression Eraser -->
    <div class="hero-slide">
      <div class="hero-text">
        <div class="hero-badge">
          <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 8v4M12 16h.01"/></svg>
          Spinal & Joint Relief Protocol
        </div>
        <h1>ERASE THE PHYSICAL GRIND<br><em>FROM YOUR SPINAL NERVES</em></h1>
        <p class="hsub">Dredge deep channel stagnation caused by prolonged sitting. This specialized combo warms up connective tissues and clears micro-circulation paths to alleviate lumbar and cervical compression.</p>
        <div class="hbtns">
          <button class="btnp" onclick="addBundleByNames('TE XIAO','DU HUO')">
            <svg viewBox="0 0 24 24"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>
            Restore Fluid Movement — Free Courier
          </button>
          <button class="btno" onclick="document.getElementById('ga').scrollIntoView({behavior:'smooth'})">Browse Herbal Pills</button>
        </div>
      </div>
      <div class="hero-imgs">
        <div class="hero-img-frame">
          <img src="assets/images/TE_XIAO_JING_ZHUI_TONG_WAN_(Neck_Relief).png" alt="Te Xiao Jing Zhui Tong Wan" onerror="this.src='';this.style.opacity='.2'">
          <div class="img-label">Te Xiao · Neck Relief</div>
        </div>
        <span class="hero-img-plus">+</span>
        <div class="hero-img-frame">
          <img src="assets/images/DU_HUO_JI_SHENG_WAN_(Joint_&_Back_Aid).png" alt="Du Huo Ji Sheng Wan" onerror="this.src='';this.style.opacity='.2'">
          <div class="img-label">Du Huo · Joint & Back Aid</div>
        </div>
      </div>
    </div>

    <!-- SLIDE 6: Seasonal Airborne Defense Grid (URGENCY) -->
    <div class="hero-slide">
      <div class="hero-text">
        <div class="hero-urgency-badge">
          <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          Seasonal Stock — Priority Access Expires 31 July 2026
        </div>
        <h1>THE INVISIBLE PROTECTION<br><em>SHIELD FOR YOUR HOUSEHOLD</em></h1>
        <p class="hsub">Active Defensive Qi (Wei-Qi) Support + Deep Lung Clearing. Formulate a strong, daily physical baseline that keeps changing seasons, city dust, and airborne bugs out of your system.</p>
        <div class="hbtns">
          <button class="btnp" onclick="addBundleByNames('ANTI-VIRUS TEA','CHUAN XIN')">
            <svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            Lock In Your Grid — Free SA Courier
          </button>
          <button class="btno" onclick="document.getElementById('ga').scrollIntoView({behavior:'smooth'})">Browse All Products</button>
        </div>
      </div>
      <div class="hero-imgs">
        <div class="hero-img-frame">
          <img src="https://lh3.googleusercontent.com/sitesv/AA5AbUD9lYp01SdoUPuGBqHKebS_7QO5ThDNRRuGpBVoQcH9tNZLMh4pHwd5G-QOmj1QWj1t8ier64O6KVBBV1ko-IcYtQmiw6JthKhMnX8R0FuwJvHkelYBRRemc8187jsFYhUEwv75MtqKwh2d1vOeCTHPGXyUsWE32QoQ53QDg6FqGS5vxfkIa56Hs9CMHyeqNzJAhRdvlf-GuHbk7dp8n997fJXRShDJmjUfnsc=w1280" alt="Anti-Virus Tea" onerror="this.src='';this.style.opacity='.2'">
          <div class="img-label">Anti-Virus Tea</div>
        </div>
        <span class="hero-img-plus">+</span>
        <div class="hero-img-frame">
          <img src="assets/images/CHUAN_XIN_LIAN_KANG_YAN_WAN_(Anti-Inflammation).png" alt="Chuan Xin Lian" onerror="this.src='';this.style.opacity='.2'">
          <div class="img-label">Chuan Xin Lian · Anti-Inflammation</div>
        </div>
      </div>
    </div>

  </div><!-- end .hero-track -->

  <!-- Navigation arrows -->
  <button class="hero-arrow hero-prev" onclick="heroMove(-1)" aria-label="Previous">
    <svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg>
  </button>
  <button class="hero-arrow hero-next" onclick="heroMove(1)" aria-label="Next">
    <svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg>
  </button>

  <!-- Dot indicators -->
  <div class="hero-dots" id="hero-dots">
    <button class="hero-dot active" onclick="heroGoTo(0)" aria-label="Slide 1"></button>
    <button class="hero-dot" onclick="heroGoTo(1)" aria-label="Slide 2"></button>
    <button class="hero-dot" onclick="heroGoTo(2)" aria-label="Slide 3"></button>
    <button class="hero-dot" onclick="heroGoTo(3)" aria-label="Slide 4"></button>
    <button class="hero-dot" onclick="heroGoTo(4)" aria-label="Slide 5"></button>
    <button class="hero-dot" onclick="heroGoTo(5)" aria-label="Slide 6"></button>
  </div>
</section>"""

# ── 3. NEW HERO JS ────────────────────────────────────────────────────────────
new_hero_js = """
// ── HERO CAROUSEL ──
let _hIdx = 0;
const _hTotal = 6;
let _hAuto;

function heroGoTo(idx) {
  _hIdx = (idx + _hTotal) % _hTotal;
  const track = document.getElementById('hero-track');
  if (track) track.style.transform = `translateX(-${_hIdx * 100}%)`;
  document.querySelectorAll('.hero-dot').forEach((d, i) => d.classList.toggle('active', i === _hIdx));
  clearInterval(_hAuto);
  _hAuto = setInterval(() => heroMove(1), 6000);
}
function heroMove(dir) { heroGoTo(_hIdx + dir); }

document.addEventListener('DOMContentLoaded', () => {
  _hAuto = setInterval(() => heroMove(1), 6000);
  // Swipe support
  const carousel = document.getElementById('hero-carousel');
  if (carousel) {
    let _sx = 0;
    carousel.addEventListener('touchstart', e => { _sx = e.touches[0].clientX; }, { passive: true });
    carousel.addEventListener('touchend', e => {
      const dx = e.changedTouches[0].clientX - _sx;
      if (Math.abs(dx) > 50) heroMove(dx < 0 ? 1 : -1);
    }, { passive: true });
  }
});

// ── BUNDLE ADD HELPER ──
function addBundleByNames(...names) {
  if (typeof P === 'undefined') { window.location.href = 'index.html'; return; }
  let added = 0;
  names.forEach(name => {
    const idx = P.findIndex(p => p && p.n && p.n.toUpperCase().includes(name.toUpperCase()));
    if (idx > -1) { addToCart(idx); added++; }
  });
  if (added > 0) {
    showToast(`Bundle added to cart!`);
    setTimeout(() => showCart(), 500);
  } else {
    showToast('Opening store — bundle ready to add!');
  }
}
"""

# ── 4. REPLACE OLD HERO CSS ────────────────────────────────────────────────────────────
# Replace the old hero block in CSS (between the hbadge-dot keyframes and /* ── TRUST BAR ── */)
old_hero_css_pattern = r'/\* ── HERO ── \*/.*?(?=/\* ── TRUST BAR ── \*/)'
content = re.sub(old_hero_css_pattern, new_hero_css + '\n', content, flags=re.DOTALL)
print("Replaced hero CSS ✓")

# ── 5. REPLACE OLD HERO HTML ──────────────────────────────────────────────────────────
old_hero_html_pattern = r'<!-- HERO -->.*?</section>'
content = re.sub(old_hero_html_pattern, new_hero_html, content, flags=re.DOTALL)
print("Replaced hero HTML ✓")

# ── 6. INJECT HERO JS before </script> ───────────────────────────────────────────────
if "_hIdx" not in content:
    # find last </script> but before </body>
    parts = content.rsplit("</script>", 1)
    content = parts[0] + new_hero_js + "\n</script>" + parts[1]
    print("Injected hero JS ✓")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Hero carousel built successfully!")
