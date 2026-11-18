#!/usr/bin/env python3
"""Digest sister-theme sampler — 4 variants of the Theme D layout for the AI Dev Digest.
Usage: python3 carousel_digest_themes.py <theme-key> <out.pdf>
Keys: night-signal, ember, daylight, blueprint"""
import json, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1350
FD = "/usr/share/fonts/truetype/dejavu"
PHOTO = os.path.expanduser("~/workspace/linkedin-digest/brand/avatar.jpg")  # SETUP: point this at YOUR avatar image (see brand/README.md)

THEMES = {
    "night-signal": {  # my pick: evening teal/navy + amber
        "bg": [(6, 58, 72), (5, 36, 58), (3, 14, 30)],
        "glows": [(880, 260, 420, (255, 170, 60, 60)), (180, 1080, 460, (40, 200, 190, 55))],
        "text": (255, 255, 255), "sub": (225, 235, 240),
        "kicker": (255, 190, 90), "card": (255, 255, 255, 34), "ring": (255, 255, 255),
    },
    "ember": {  # near-black charcoal + ember orange
        "bg": [(26, 18, 16), (52, 22, 14), (10, 8, 8)],
        "glows": [(860, 300, 430, (255, 92, 40, 70)), (200, 1060, 440, (255, 170, 70, 50))],
        "text": (255, 255, 255), "sub": (235, 225, 215),
        "kicker": (255, 150, 80), "card": (255, 255, 255, 30), "ring": (255, 255, 255),
    },
    "daylight": {  # warm paper editorial, ink text
        "bg": [(246, 241, 231), (238, 230, 214), (226, 214, 192)],
        "glows": [(880, 260, 420, (255, 255, 255, 90)), (180, 1080, 460, (210, 150, 90, 40))],
        "text": (28, 28, 34), "sub": (70, 66, 60),
        "kicker": (196, 92, 32), "card": (255, 255, 255, 110), "ring": (28, 28, 34),
    },
    "blueprint": {  # deep navy blueprint + cyan grid
        "bg": [(10, 32, 74), (8, 24, 58), (5, 14, 36)],
        "glows": [(880, 260, 420, (70, 200, 255, 45)), (180, 1080, 460, (40, 120, 220, 55))],
        "text": (255, 255, 255), "sub": (210, 228, 245),
        "kicker": (110, 220, 255), "card": (255, 255, 255, 30), "ring": (255, 255, 255),
        "grid": True,
    },
    # ---- Round 2: break from the aurora mold ----
    "evening-edition": {  # light paper, serif headlines, newspaper "evening edition"
        "bg": [(250, 246, 238), (244, 236, 220), (232, 220, 198)],
        "glows": [],
        "text": (24, 24, 30), "sub": (90, 84, 76),
        "kicker": (178, 34, 34), "card": (255, 255, 255, 130), "ring": (24, 24, 30),
        "serif": True, "rule": True,
    },
    "after-hours": {  # true black terminal, amber mono, outlined cards
        "bg": [(10, 10, 12), (10, 10, 12), (10, 10, 12)],
        "glows": [],
        "text": (240, 238, 232), "sub": (170, 165, 155),
        "kicker": (255, 176, 32), "card": (255, 176, 32, 26), "ring": (255, 176, 32),
        "outline": True, "flat": True,
    },
    "sunset": {  # warm dusk gradient — literally evening, warm vs morning cool
        "bg": [(66, 22, 50), (148, 54, 38), (28, 15, 26)],
        "glows": [(540, 420, 480, (255, 150, 70, 70))],
        "text": (255, 244, 230), "sub": (240, 214, 190),
        "kicker": (255, 200, 110), "card": (255, 255, 255, 30), "ring": (255, 244, 230),
    },
    "signal": {  # flat ink, coral accent bar, Swiss poster — no glows at all
        "bg": [(17, 21, 36), (17, 21, 36), (17, 21, 36)],
        "glows": [],
        "text": (255, 255, 255), "sub": (200, 206, 224),
        "kicker": (255, 110, 110), "card": (255, 255, 255, 24), "ring": (255, 110, 110),
        "flat": True, "bar": True, "frame": True,
    },
    # ---- Round 3 (2026-10-14): rotation set — each has its own layout engine ----
    "terminal": {  # dev console: near-black, phosphor green, mono everything, log layout
        "bg": [(7, 10, 7), (7, 10, 7), (7, 10, 7)],
        "glows": [],
        "text": (232, 255, 238), "sub": (158, 190, 165),
        "kicker": (74, 246, 128), "card": (74, 246, 128, 18), "ring": (74, 246, 128),
        "flat": True, "layout": "terminal",
        "dim": (96, 140, 105), "rule_c": (34, 58, 40), "chrome": (17, 22, 17),
    },
    "editorial": {  # broadsheet: warm paper, ink serif display, one red accent, column rules
        "bg": [(248, 244, 234), (248, 244, 234), (248, 244, 234)],
        "glows": [],
        "text": (22, 22, 26), "sub": (96, 90, 80),
        "kicker": (178, 30, 30), "card": (255, 255, 255, 0), "ring": (22, 22, 26),
        "flat": True, "layout": "editorial", "serif": True,
        "hair": (186, 178, 162),
    },
    "neon-grid": {  # violet-black, cyan->magenta gradient accents, blueprint grid, glass panels
        "bg": [(16, 7, 34), (22, 9, 48), (8, 4, 20)],
        "glows": [(905, 235, 400, (0, 229, 255, 42)), (165, 1120, 430, (255, 0, 190, 38)), (540, 690, 330, (130, 70, 255, 30))],
        "text": (255, 255, 255), "sub": (206, 198, 235),
        "kicker": (0, 229, 255), "card": (255, 255, 255, 22), "ring": (0, 229, 255),
        "layout": "neon", "accent2": (255, 0, 190), "panel_line": (140, 120, 255),
    },
    "poster": {  # Swiss/brutalist: off-white, black type, loud per-slot accent block, giant numerals
        "bg": [(246, 245, 240), (246, 245, 240), (246, 245, 240)],
        "glows": [],
        "text": (14, 14, 16), "sub": (70, 70, 74),
        "kicker": (255, 62, 0), "card": (255, 255, 255, 0), "ring": (14, 14, 16),
        "flat": True, "layout": "poster",
        "slot_accents": {"PRODUCT": (255, 62, 0), "FRAMEWORKS": (0, 64, 255), "REPO": (0, 158, 79), "RESEARCH": (138, 0, 255), "ECOSYSTEM": (232, 145, 0)},
    },
    "aurora": {  # gradient mesh + frosted rounded glass cards, calm premium
        "bg": [(19, 15, 56), (11, 27, 54), (6, 10, 30)],
        "glows": [(885, 255, 430, (45, 220, 200, 52)), (175, 1085, 470, (150, 90, 255, 48)), (545, 700, 360, (255, 90, 160, 28))],
        "text": (255, 255, 255), "sub": (214, 222, 240),
        "kicker": (150, 240, 214), "card": (255, 255, 255, 36), "ring": (150, 240, 214),
        "layout": "aurora",
    },
    # ---- Round 4 (2026-10-14): research archetypes — see research report §1/§5 ----
    "frontpage": {  # Archetype C: Rundown/Superhuman news front page — paper, ink, red accent
        "bg": [(250, 249, 245), (250, 249, 245), (250, 249, 245)],
        "glows": [],
        "text": (18, 18, 22), "sub": (92, 88, 82),
        "kicker": (178, 30, 30), "card": (255, 255, 255, 0), "ring": (18, 18, 22),
        "flat": True, "layout": "frontpage",
        "hair": (203, 198, 188),
    },
    "explainer": {  # Archetype B: Hassid how-to — light, black bold sans, blue step system
        "bg": [(252, 252, 250), (252, 252, 250), (252, 252, 250)],
        "glows": [],
        "text": (14, 14, 18), "sub": (78, 78, 86),
        "kicker": (0, 82, 204), "card": (240, 242, 245, 255), "ring": (0, 82, 204),
        "flat": True, "layout": "explainer",
        "hair": (214, 216, 220), "panel_bar": (226, 229, 233),
        "ok": (0, 150, 80), "panel_bg": (240, 242, 245),
    },
    "minimalist": {  # Archetype A: Welsh — pure white, near-black grotesque, no imagery
        "bg": [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
        "glows": [],
        "text": (10, 10, 12), "sub": (94, 94, 100),
        "kicker": (10, 10, 12), "card": (255, 255, 255, 0), "ring": (10, 10, 12),
        "flat": True, "layout": "minimalist",
        "hair": (224, 224, 226),
    },
    "statdeck": {  # Archetype F: van der Blom-style stat deck — light, one giant blue number
        "bg": [(247, 248, 250), (247, 248, 250), (247, 248, 250)],
        "glows": [],
        "text": (16, 20, 30), "sub": (86, 92, 104),
        "kicker": (10, 80, 200), "card": (255, 255, 255, 0), "ring": (10, 80, 200),
        "flat": True, "layout": "statdeck",
        "hair": (206, 211, 220),
    },
}

def font(name, size):
    return ImageFont.truetype(f"{FD}/{name}.ttf", size)

def fit(draw, text, name, max_w, start, min_s=24):
    s = start
    while s > min_s:
        f = font(name, s)
        if max(draw.textbbox((0,0), ln, font=f)[2] for ln in text.split("\n")) <= max_w:
            return f
        s -= 4
    return font(name, min_s)

def wrap(draw, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if draw.textbbox((0,0), t, font=f)[2] <= max_w:
            cur = t
        else:
            lines.append(cur); cur = w_
    if cur: lines.append(cur)
    return lines

def bg_for(t):
    if t.get("flat"):
        return Image.new("RGB", (W, H), t["bg"][1])
    top, mid, bot = t["bg"]
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    for y in range(H):
        tt = y/(H-1)
        if tt < 0.5:
            u = tt*2; c = tuple(int(top[i]+(mid[i]-top[i])*u) for i in range(3))
        else:
            u = (tt-0.5)*2; c = tuple(int(mid[i]+(bot[i]-mid[i])*u) for i in range(3))
        d.line((0, y, W, y), fill=c)
    if t.get("grid"):
        gd = ImageDraw.Draw(img)
        for gx in range(0, W, 72):
            gd.line((gx, 0, gx, H), fill=(120, 200, 255, 22))
        for gy in range(0, H, 72):
            gd.line((0, gy, W, gy), fill=(120, 200, 255, 22))
    ov = Image.new("RGBA", (W, H), (0,0,0,0))
    for (cx, cy, r, col) in t["glows"]:
        m = Image.new("L", (W, H), 0)
        ImageDraw.Draw(m).ellipse((cx-r, cy-r, cx+r, cy+r), fill=255)
        m = m.filter(ImageFilter.GaussianBlur(120))
        ov = Image.alpha_composite(ov, Image.composite(Image.new("RGBA",(W,H),col), Image.new("RGBA",(W,H),(0,0,0,0)), m))
    return Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")

def circle_photo(d):
    im = Image.open(PHOTO).convert("RGB")
    w, h = im.size
    side = min(w, h)
    face = im.crop(((w-side)//2, (h-side)//2, (w-side)//2+side, (h-side)//2+side))
    inner = int(d * 0.96)
    face = face.resize((inner, inner), Image.LANCZOS)
    canvas = Image.new("RGBA", (d, d), (0,0,0,0))
    canvas.paste(face, ((d-inner)//2, (d-inner)//2))
    mask = Image.new("L", (d, d), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, d, d), fill=255)
    out = Image.new("RGBA", (d, d), (0,0,0,0)); out.paste(canvas, (0,0), mask)
    return out

def avatar_lockup(base, t, total_n):
    d = ImageDraw.Draw(base); s = 150
    x, y = W-80-s, H-80-s
    f = font("DejaVuSans-Bold", 30)
    tw = d.textbbox((0,0), "[YOUR NAME]", font=f)[2]
    d.text((x-tw-24, y+s//2-20), "[YOUR NAME]", font=f, fill=t["text"])
    d.ellipse((x-6, y-6, x+s+6, y+s+6), outline=t["ring"], width=5)
    ph = circle_photo(s); base.paste(ph, (x, y), ph)
    d.text((80, H-110), f"{total_n[0]:02d} / {total_n[1]:02d}", font=font("DejaVuSans", 26), fill=t["text"])
    total_n[0] += 1

def glass_card(base, t, x, y, w, h):
    if t.get("outline"):
        d = ImageDraw.Draw(base)
        d.rounded_rectangle((x, y, x+w, y+h), radius=18, outline=t["kicker"], width=4)
        return
    card = Image.new("RGBA", (w, h), t["card"])
    base.paste(card, (x, y), card)

def title_font(t):
    return "DejaVuSerif-Bold" if t.get("serif") else "DejaVuSans-Bold"

def frame(img, t):
    if not t.get("frame"):
        return
    d = ImageDraw.Draw(img)
    m = 26
    d.rounded_rectangle((m, m, W-m, H-m), radius=26, outline=t["kicker"], width=5)

def tag_pill(img, t, tag):
    d = ImageDraw.Draw(img)
    f = font("DejaVuSansMono-Bold", 26)
    tw = d.textbbox((0,0), tag, font=f)[2]
    pw, ph = tw + 48, 52
    x1, y1 = W-80-pw, 92
    d.rounded_rectangle((x1, y1, x1+pw, y1+ph), radius=ph//2, fill=t["kicker"])
    d.text((x1+24, y1+10), tag, font=f, fill=(17, 21, 36))

def _lum(im):
    """Mean perceived luminance 0-255 of an RGB image."""
    import numpy as np
    a = np.asarray(im.convert("RGB"), dtype=float)
    return float((0.299*a[..., 0] + 0.587*a[..., 1] + 0.114*a[..., 2]).mean())

def broll_bg(path, t, blur=20, base_alpha=90, max_alpha=225, lum_cap=80):
    """Blurred topical background with ADAPTIVE darkening.

    Light source images (e.g. light-UI screenshots) get pushed much darker so
    the slide keeps the theme's deep-navy read; dark photos keep the standard
    35% treatment. Returns None when even max darkening leaves the background
    too light — caller falls back to the flat theme background.
    """
    im = Image.open(path).convert("RGB")
    sw, sh = im.size
    scale = max(W/sw, H/sh)
    im = im.resize((int(sw*scale)+1, int(sh*scale)+1), Image.LANCZOS)
    x = (im.width - W)//2; y = (im.height - H)//2
    im = im.crop((x, y, x+W, y+H))
    im = im.filter(ImageFilter.GaussianBlur(blur))
    lum = _lum(im)
    alpha = min(max_alpha, max(base_alpha, int((lum - 30) * 1.15)))
    dark = Image.new("RGBA", (W, H), (8, 10, 20, alpha))
    out = Image.alpha_composite(im.convert("RGBA"), dark).convert("RGB")
    if _lum(out) > lum_cap:
        return None
    return out

def build(theme_key, spec, out_pdf):
    t = THEMES[theme_key]
    if t.get("layout"):
        return build_v2(theme_key, spec, out_pdf)
    bg = bg_for(t)
    pages, n = [], [1]
    kick = spec["kicker"]
    total = 2 + len(spec["slides"])

    # COVER
    img = bg.copy(); d = ImageDraw.Draw(img)
    d.text((80, 100), kick, font=font("DejaVuSansMono-Bold", 32), fill=t["kicker"])
    if t.get("bar"):
        d.rectangle((80, 148, 320, 160), fill=t["kicker"])
    if t.get("rule"):
        d.line((80, 150, W-80, 150), fill=t["kicker"], width=4)
    d.text((80, 200), spec["title"], font=fit(d, spec["title"], title_font(t), W-160, 128), fill=t["text"])
    glass_card(img, t, 80, 620, W-160, 200); d = ImageDraw.Draw(img)
    d.text((110, 660), spec["cover_sub"], font=fit(d, spec["cover_sub"], "DejaVuSans", W-220, 48), fill=t["text"])
    d.text((110, 740), "For builders, by a builder.", font=font("DejaVuSans", 40), fill=t["sub"])
    d.text((80, 920), "swipe  →", font=font("DejaVuSans-Bold", 38), fill=t["text"])
    avatar_lockup(img, t, [1, total]); frame(img, t); pages.append(img)

    # STORY SLIDES
    for sl in spec["slides"]:
        bbg = broll_bg(sl["broll"], t) if sl.get("broll") else None
        slide_bg = bbg if bbg is not None else bg
        img = slide_bg.copy(); d = ImageDraw.Draw(img)
        d.text((80, 100), kick, font=font("DejaVuSansMono-Bold", 28), fill=t["kicker"])
        if t.get("bar"):
            d.rectangle((80, 142, 280, 152), fill=t["kicker"])
        if t.get("rule"):
            d.line((80, 142, W-80, 142), fill=t["kicker"], width=3)
        # Heading: uniform 68pt bold on every slide (the owner 2026-10-11 — no auto-shrink).
        # Long headings wrap to 2 lines at full size; shrink only if 2 lines still overflow.
        _hs, _hf = 68, font(title_font(t), 68)
        _hlines = wrap(d, sl["heading"], _hf, W-160)
        while len(_hlines) > 2 and _hs > 28:
            _hs -= 4; _hf = font(title_font(t), _hs)
            _hlines = wrap(d, sl["heading"], _hf, W-160)
        _hy = 170
        for _ln in _hlines[:2]:
            d.text((80, _hy), _ln, font=_hf, fill=t["text"]); _hy += int(_hs * 1.18)
        bullets = sl["bullets"]
        nb = len(bullets)
        top, bottom, gap = 360, 1080, 24
        ch = (bottom - top - (nb-1)*gap)//nb
        y = top
        for b in bullets:
            glass_card(img, t, 80, y, W-160, ch); d = ImageDraw.Draw(img)
            bf = font("DejaVuSans-Bold", 40 if nb <= 3 else 36)
            lines = wrap(d, b, bf, W-260)
            lh = 56 if nb <= 3 else 50
            ty = y + (ch - len(lines)*lh)//2 + 6
            for ln in lines:
                d.text((115, ty), ln, font=bf, fill=t["text"]); ty += lh
            y += ch + gap
        if sl.get("tag"):
            tag_pill(img, t, sl["tag"])
        avatar_lockup(img, t, [len(pages)+1, total]); frame(img, t); pages.append(img)

    # CTA
    img = bg.copy(); d = ImageDraw.Draw(img)
    d.text((80, 100), kick, font=font("DejaVuSansMono-Bold", 32), fill=t["kicker"])
    if t.get("bar"):
        d.rectangle((80, 148, 320, 160), fill=t["kicker"])
    if t.get("rule"):
        d.line((80, 150, W-80, 150), fill=t["kicker"], width=4)
    cta = "\n".join(spec["cta"])
    d.text((80, 300), cta, font=fit(d, cta, title_font(t), W-160, 92), fill=t["text"])
    d.text((80, 640), "Follow so you don't miss it.", font=font("DejaVuSans-Bold", 52), fill=t["kicker"])
    avatar_lockup(img, t, [len(pages)+1, total]); frame(img, t); pages.append(img)

    pages[0].save(out_pdf, save_all=True, append_images=pages[1:])
    print(f"wrote {out_pdf} ({theme_key}, {len(pages)} pages)")

# ================= Round 3 layout engines (2026-10-14 rotation) =================
# Each layout below renders cover / story / CTA with its OWN geometry.
# Locked elements preserved everywhere: kicker, title, slot pills, 3 bullets,
# cover_sub, swipe cue, CTA lines, page numbers, [YOUR NAME] avatar lockup,
# uniform heading size (wrap to 2 lines, shrink only if still overflowing).

def _rgba(t):
    return bg_for(t).convert("RGBA")

def _finish(img):
    return img.convert("RGB")

def _lockup2(base, t, idx, total, name_fill, ring, num_fill, name_font=None, num_font=None, num_xy=(80, H-118)):
    d = ImageDraw.Draw(base); s = 150
    x, y = W-80-s, H-80-s
    f = name_font or font("DejaVuSans-Bold", 30)
    tw = d.textbbox((0, 0), "[YOUR NAME]", font=f)[2]
    d.text((x-tw-24, y+s//2-20), "[YOUR NAME]", font=f, fill=name_fill)
    d.ellipse((x-6, y-6, x+s+6, y+s+6), outline=ring, width=5)
    ph = circle_photo(s); base.paste(ph, (x, y), ph)
    d = ImageDraw.Draw(base)
    d.text(num_xy, f"{idx:02d} / {total:02d}", font=num_font or font("DejaVuSans", 26), fill=num_fill)

def _heading(d, text, fname, size, max_w, fill, x, y, min_s=30):
    """Uniform-size heading: wraps to 2 lines at full size; shrinks only if >2 lines."""
    s, f = size, font(fname, size)
    lines = wrap(d, text, f, max_w)
    while len(lines) > 2 and s > min_s:
        s -= 4; f = font(fname, s); lines = wrap(d, text, f, max_w)
    for ln in lines[:2]:
        d.text((x, y), ln, font=f, fill=fill); y += int(s * 1.18)
    return y

def _glass_r(base, x, y, w, h, fill, outline=None, radius=26, width=2):
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(ov).rounded_rectangle((x, y, x+w, y+h), radius=radius, fill=fill, outline=outline, width=width)
    base.alpha_composite(ov)

def _hgrad(w, h, c1, c2, vertical=False):
    g = Image.new("RGB", (w, h)); gd = ImageDraw.Draw(g)
    n = h if vertical else w
    for i in range(n):
        u = i / max(n-1, 1)
        c = tuple(int(c1[k] + (c2[k]-c1[k]) * u) for k in range(3))
        if vertical: gd.line((0, i, w, i), fill=c)
        else: gd.line((i, 0, i, h), fill=c)
    return g

def _blend(c, bgc, f):
    """f=0 -> bgc, f=1 -> c."""
    return tuple(int(c[i]*f + bgc[i]*(1-f)) for i in range(3))

MB, M, SB, S, SRFB, SRF = "DejaVuSansMono-Bold", "DejaVuSansMono", "DejaVuSans-Bold", "DejaVuSans", "DejaVuSerif-Bold", "DejaVuSerif"

# ---------------- TERMINAL ----------------
def _term_chrome(base, t):
    d = ImageDraw.Draw(base)
    d.rectangle((0, 0, W, 66), fill=t["chrome"])
    for i, c in enumerate([(206, 84, 72), (214, 164, 62), (64, 186, 94)]):
        cx = 42 + i*38
        d.ellipse((cx-11, 22, cx+11, 44), fill=c)
    d.text((160, 20), "you@digest: ~/ai-dev-digest", font=font(M, 24), fill=t["sub"])
    d.line((0, 66, W, 66), fill=t["rule_c"], width=2)

def _term_cover(t, spec, total):
    img = _rgba(t); _term_chrome(img, t); d = ImageDraw.Draw(img)
    d.text((80, 150), "$ cat ai_dev_digest.md", font=font(MB, 30), fill=t["dim"])
    d.text((80, 225), "# " + spec["kicker"], font=font(MB, 36), fill=t["kicker"])
    d.text((80, 300), spec["title"], font=fit(d, spec["title"], MB, W-160, 104), fill=t["text"])
    d.line((80, 480, W-80, 480), fill=t["rule_c"], width=2)
    d.text((80, 530), "> " + spec["cover_sub"], font=font(MB, 42), fill=t["text"])
    d.text((80, 600), "> For builders, by a builder.", font=font(M, 38), fill=t["sub"])
    idx_line = "index: " + " / ".join(s["tag"] for s in spec["slides"]) if spec.get("slides") else ""
    if idx_line:
        d.text((80, 720), idx_line, font=font(M, 25), fill=t["dim"])
    d.text((80, 930), "> swipe ->", font=font(MB, 36), fill=t["kicker"])
    _lockup2(img, t, 1, total, t["text"], t["ring"], t["dim"], name_font=font(MB, 28), num_font=font(M, 26))
    return _finish(img)

def _term_story(t, spec, sl, entry, idx, total):
    img = _rgba(t); _term_chrome(img, t); d = ImageDraw.Draw(img)
    d.text((80, 104), f"[18:00:{entry:02d}] :: DAILY DIGEST :: ENTRY {entry:02d}", font=font(M, 25), fill=t["dim"])
    tag = sl.get("tag", "")
    tf = font(MB, 30); tw = d.textbbox((0, 0), f"[ {tag} ]", font=tf)[2]
    d.rectangle((80, 148, 80+tw+28, 148+54), outline=t["kicker"], width=2)
    d.text((94, 158), f"[ {tag} ]", font=tf, fill=t["kicker"])
    d.text((80, 238), ">", font=font(MB, 56), fill=t["kicker"])
    _heading(d, sl["heading"], MB, 56, W-160-52, t["text"], 132, 238, min_s=38)
    y = 500
    bf = font(M, 33)
    for b in sl["bullets"]:
        d.line((80, y, W-80, y), fill=t["rule_c"], width=2)
        lines = wrap(d, b, bf, W-160-56)
        ty = y + 22
        d.text((80, ty), "+", font=font(MB, 33), fill=t["kicker"])
        for ln in lines:
            d.text((124, ty), ln, font=bf, fill=t["text"]); ty += 46
        y = ty + 26
    d.line((80, y, W-80, y), fill=t["rule_c"], width=2)
    _lockup2(img, t, idx, total, t["text"], t["ring"], t["dim"], name_font=font(MB, 28), num_font=font(M, 26))
    return _finish(img)

def _term_cta(t, spec, total, npages):
    img = _rgba(t); _term_chrome(img, t); d = ImageDraw.Draw(img)
    d.text((80, 170), "$ ./tomorrow.sh", font=font(MB, 30), fill=t["dim"])
    y = 280
    for i, ln in enumerate(spec["cta"]):
        col = t["kicker"] if i == len(spec["cta"]) - 1 else t["text"]
        d.text((80, y), ln, font=fit(d, ln, MB, W-160, 62), fill=col); y += 92
    d.text((80, y+40), "# EOF — exit 0", font=font(M, 28), fill=t["dim"])
    _lockup2(img, t, npages, total, t["text"], t["ring"], t["dim"], name_font=font(MB, 28), num_font=font(M, 26))
    return _finish(img)

# ---------------- EDITORIAL ----------------
def _ed_head(base, t, spec):
    d = ImageDraw.Draw(base)
    d.text((W//2, 66), "FOR BUILDERS, BY A BUILDER", font=font(MB, 23), fill=t["sub"], anchor="ma")
    d.line((80, 112, W-80, 112), fill=t["text"], width=2)
    d.line((80, 122, W-80, 122), fill=t["text"], width=7)

def _ed_cover(t, spec, total):
    img = _rgba(t); _ed_head(img, t, spec); d = ImageDraw.Draw(img)
    d.text((W//2, 168), spec["kicker"], font=font(MB, 30), fill=t["kicker"], anchor="ma")
    d.text((W//2, 232), spec["title"], font=fit(d, spec["title"], SRFB, W-120, 124), fill=t["text"], anchor="ma")
    d.line((80, 420, W-80, 420), fill=t["text"], width=2)
    d.text((W//2, 470), spec["cover_sub"], font=fit(d, spec["cover_sub"], SRF, W-200, 44), fill=t["text"], anchor="ma")
    d.text((W//2, 545), "Five stories, read before your first coffee refill.", font=font(SRF, 33), fill=t["sub"], anchor="ma")
    d.rectangle((W//2-30, 660, W//2+30, 666), fill=t["kicker"])
    d.text((W//2, 720), "swipe  ->", font=font(SRFB, 36), fill=t["text"], anchor="ma")
    _lockup2(img, t, 1, total, t["text"], t["ring"], t["sub"], name_font=font(SRFB, 28), num_font=font(M, 24))
    return _finish(img)

def _ed_story(t, spec, sl, entry, idx, total):
    img = _rgba(t); _ed_head(img, t, spec); d = ImageDraw.Draw(img)
    d.text((80, 158), spec["kicker"], font=font(MB, 24), fill=t["kicker"])
    d.text((W-80, 150), f"No. {entry}", font=font(SRF, 42), fill=t["sub"], anchor="ra")
    tag = sl.get("tag", "")
    d.text((80, 218), " · ".join(list(tag)), font=font(MB, 27), fill=t["kicker"])
    y = _heading(d, sl["heading"], SRFB, 60, W-160, t["text"], 80, 268)
    d.rectangle((80, y+6, 200, y+13), fill=t["kicker"])
    # left rail with hairlines between paragraph-style bullets
    rail_x, tx = 150, 196
    y += 70
    d.line((rail_x, y, rail_x, 1120), fill=t["hair"], width=2)
    bf = font(SRF, 35)
    for b in sl["bullets"]:
        d.rectangle((tx, y+13, tx+13, y+26), fill=t["kicker"])
        lines = wrap(d, b, bf, W-tx-60-80)
        for ln in lines:
            d.text((tx+34, y), ln, font=bf, fill=t["text"]); y += 49
        y += 30
        d.line((tx, y, W-80, y), fill=t["hair"], width=1)
        y += 30
    d.text((80, H-190), "BY [YOUR NAME]", font=font(MB, 22), fill=t["sub"])
    _lockup2(img, t, idx, total, t["text"], t["ring"], t["sub"], name_font=font(SRFB, 28), num_font=font(M, 24))
    return _finish(img)

def _ed_cta(t, spec, total, npages):
    img = _rgba(t); _ed_head(img, t, spec); d = ImageDraw.Draw(img)
    y = 330
    for i, ln in enumerate(spec["cta"]):
        col = t["kicker"] if i == len(spec["cta"]) - 1 else t["text"]
        d.text((W//2, y), ln, font=fit(d, ln, SRFB, W-160, 80), fill=col, anchor="ma"); y += 118
    d.line((80, y+30, W-80, y+30), fill=t["text"], width=2)
    d.line((80, y+40, W-80, y+40), fill=t["text"], width=7)
    _lockup2(img, t, npages, total, t["text"], t["ring"], t["sub"], name_font=font(SRFB, 28), num_font=font(M, 24))
    return _finish(img)

# ---------------- NEON GRID ----------------
def _neon_bg(t, spec):
    img = _rgba(t)
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(ov)
    for gx in range(0, W, 72):
        gd.line((gx, 0, gx, H), fill=(120, 80, 255, 30 if gx % 360 else 52))
    for gy in range(0, H, 72):
        gd.line((0, gy, W, gy), fill=(120, 80, 255, 30 if gy % 360 else 52))
    img.alpha_composite(ov)
    return img

def _neon_pill(base, t, tag):
    d = ImageDraw.Draw(base)
    f = font(MB, 26); tw = d.textbbox((0, 0), tag, font=f)[2]
    pw, ph = tw + 48, 52
    x1, y1 = W-80-pw, 92
    grad = _hgrad(pw, ph, t["kicker"], t["accent2"]).convert("RGBA")
    mask = Image.new("L", (pw, ph), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, pw, ph), radius=ph//2, fill=255)
    base.paste(grad, (x1, y1), mask)
    d = ImageDraw.Draw(base)
    d.text((x1+24, y1+10), tag, font=f, fill=(10, 4, 24))

def _neon_panel(base, t, x, y, w, h):
    _glass_r(base, x, y, w, h, t["card"], outline=tuple(list(t["panel_line"]) + [130]), radius=22, width=2)
    strip = _hgrad(8, h, t["kicker"], t["accent2"], vertical=True).convert("RGBA")
    mask = Image.new("L", (8, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, 8, h), radius=4, fill=255)
    base.paste(strip, (x, y), mask)

def _neon_cover(t, spec, total):
    img = _neon_bg(t, spec); d = ImageDraw.Draw(img)
    d.text((80, 100), spec["kicker"], font=font(MB, 32), fill=t["kicker"])
    bar = _hgrad(260, 10, t["kicker"], t["accent2"]).convert("RGBA"); img.paste(bar, (80, 150), bar)
    d = ImageDraw.Draw(img)
    d.text((80, 195), spec["title"], font=fit(d, spec["title"], SB, W-160, 128), fill=t["text"])
    _glass_r(img, 80, 610, W-160, 215, t["card"], outline=tuple(list(t["kicker"]) + [160]), radius=28, width=2)
    d = ImageDraw.Draw(img)
    d.text((112, 652), spec["cover_sub"], font=fit(d, spec["cover_sub"], S, W-224, 48), fill=t["text"])
    d.text((112, 738), "For builders, by a builder.", font=font(S, 40), fill=t["sub"])
    d.text((80, 930), "swipe  ->", font=font(SB, 38), fill=t["text"])
    _lockup2(img, t, 1, total, t["text"], t["ring"], t["kicker"], num_font=font(M, 26))
    return _finish(img)

def _neon_story(t, spec, sl, entry, idx, total):
    bbg = broll_bg(sl["broll"], t) if sl.get("broll") else None
    if bbg is not None:
        img = bbg.convert("RGBA")
        img.alpha_composite(Image.new("RGBA", (W, H), (6, 4, 20, 35)))
    else:
        img = _neon_bg(t, spec)
    d = ImageDraw.Draw(img)
    d.text((80, 100), spec["kicker"], font=font(MB, 28), fill=t["kicker"])
    _heading(d, sl["heading"], SB, 66, W-160, t["text"], 80, 170)
    bullets = sl["bullets"]; nb = len(bullets)
    top, bottom, gap = 360, 1080, 24
    ch = (bottom - top - (nb-1)*gap)//nb
    y = top
    for b in bullets:
        _neon_panel(img, t, 80, y, W-160, ch); d = ImageDraw.Draw(img)
        bf = font(SB, 40)
        lines = wrap(d, b, bf, W-280)
        ty = y + (ch - len(lines)*56)//2 + 6
        for ln in lines:
            d.text((128, ty), ln, font=bf, fill=t["text"]); ty += 56
        y += ch + gap
    if sl.get("tag"):
        _neon_pill(img, t, sl["tag"])
    _lockup2(img, t, idx, total, t["text"], t["ring"], t["kicker"], num_font=font(M, 26))
    return _finish(img)

def _neon_cta(t, spec, total, npages):
    img = _neon_bg(t, spec); d = ImageDraw.Draw(img)
    d.text((80, 100), spec["kicker"], font=font(MB, 32), fill=t["kicker"])
    bar = _hgrad(260, 10, t["kicker"], t["accent2"]).convert("RGBA"); img.paste(bar, (80, 150), bar)
    d = ImageDraw.Draw(img)
    y = 300
    for i, ln in enumerate(spec["cta"]):
        col = t["accent2"] if i == len(spec["cta"]) - 1 else t["text"]
        d.text((80, y), ln, font=fit(d, ln, SB, W-160, 88), fill=col); y += 122
    _lockup2(img, t, npages, total, t["text"], t["ring"], t["kicker"], num_font=font(M, 26))
    return _finish(img)

# ---------------- BOLD POSTER ----------------
def _poster_accent(t, tag):
    return t["slot_accents"].get(tag, t["kicker"])

def _poster_cover(t, spec, total):
    img = _rgba(t); d = ImageDraw.Draw(img)
    acc = t["kicker"]
    import re as _re
    m = _re.search(r"#(\d+)", spec["kicker"])
    ed = f"{int(m.group(1)):02d}" if m else "01"
    ghost = _blend(acc, t["bg"][0], 0.16)
    d.text((W-430, 110), ed, font=font(SB, 290), fill=ghost)
    d.rectangle((80, 108, 100, 128), fill=acc)
    d.text((116, 100), spec["kicker"], font=font(MB, 28), fill=t["text"])
    d.text((74, 190), "AI Dev", font=font(SB, 196), fill=t["text"])
    d.text((74, 396), "Digest", font=font(SB, 196), fill=t["text"])
    d.rectangle((80, 640, 470, 668), fill=acc)
    d.text((80, 720), spec["cover_sub"], font=fit(d, spec["cover_sub"], SB, W-160, 50), fill=t["text"])
    d.text((80, 800), "For builders, by a builder.", font=font(S, 38), fill=t["sub"])
    d.text((80, 950), "SWIPE ", font=font(MB, 36), fill=t["text"])
    sw = d.textbbox((0, 0), "SWIPE ", font=font(MB, 36))[2]
    d.text((80+sw, 950), "->", font=font(MB, 36), fill=acc)
    _lockup2(img, t, 1, total, t["text"], t["ring"], t["text"], num_font=font(SB, 32), num_xy=(80, H-124))
    return _finish(img)

def _poster_story(t, spec, sl, entry, idx, total):
    img = _rgba(t); d = ImageDraw.Draw(img)
    acc = _poster_accent(t, sl.get("tag", ""))
    d.rectangle((0, 0, 110, H), fill=acc)
    ghost = _blend(acc, t["bg"][0], 0.12)
    d.text((W-430, 16), f"{entry:02d}", font=font(SB, 370), fill=ghost)
    d.text((W-80, 84), spec["kicker"], font=font(MB, 22), fill=t["sub"], anchor="ra")
    tag = sl.get("tag", "")
    tf = font(MB, 26); tw = d.textbbox((0, 0), tag, font=tf)[2]
    d.rectangle((190, 96, 190+tw+44, 96+58), fill=acc)
    d.text((212, 110), tag, font=tf, fill=(255, 255, 255))
    y = _heading(d, sl["heading"], SB, 64, W-190-70, t["text"], 190, 210)
    y += 56
    bf = font(SB, 38)
    for b in sl["bullets"]:
        lines = wrap(d, b, bf, W-190-70-52)
        d.rectangle((190, y+14, 206, y+30), fill=acc)
        for ln in lines:
            d.text((242, y), ln, font=bf, fill=t["text"]); y += 53
        y += 26
        d.line((190, y, W-70, y), fill=t["text"], width=2)
        y += 30
    _lockup2(img, t, idx, total, t["text"], t["ring"], t["text"], num_font=font(SB, 32), num_xy=(190, H-124))
    return _finish(img)

def _poster_cta(t, spec, total, npages):
    img = _rgba(t); d = ImageDraw.Draw(img)
    acc = t["kicker"]
    d.rectangle((0, 0, 110, H), fill=acc)
    d.text((190, 96), spec["kicker"], font=font(MB, 26), fill=t["text"])
    y = 300
    for i, ln in enumerate(spec["cta"]):
        col = acc if i == len(spec["cta"]) - 1 else t["text"]
        d.text((190, y), ln, font=fit(d, ln, SB, W-190-70, 84), fill=col); y += 122
    ay = y + 56
    d.rectangle((190, ay, 360, ay+26), fill=acc)
    d.polygon([(360, ay-20), (360, ay+46), (436, ay+13)], fill=acc)
    _lockup2(img, t, npages, total, t["text"], t["ring"], t["text"], num_font=font(SB, 32), num_xy=(190, H-124))
    return _finish(img)

# ---------------- AURORA ----------------
def _aurora_pill(base, t, tag):
    d = ImageDraw.Draw(base)
    f = font(MB, 26); tw = d.textbbox((0, 0), tag, font=f)[2]
    pw, ph = tw + 48, 52
    x1, y1 = W-80-pw, 92
    _glass_r(base, x1, y1, pw, ph, (255, 255, 255, 44), outline=tuple(list(t["kicker"]) + [220]), radius=ph//2, width=2)
    d = ImageDraw.Draw(base)
    d.text((x1+24, y1+10), tag, font=f, fill=(255, 255, 255))

def _aurora_cover(t, spec, total):
    img = _rgba(t); d = ImageDraw.Draw(img)
    d.text((80, 100), spec["kicker"], font=font(MB, 32), fill=t["kicker"])
    d.text((80, 195), spec["title"], font=fit(d, spec["title"], SB, W-160, 128), fill=t["text"])
    _glass_r(img, 80, 610, W-160, 215, t["card"], outline=(255, 255, 255, 110), radius=30, width=2)
    d = ImageDraw.Draw(img)
    d.text((112, 652), spec["cover_sub"], font=fit(d, spec["cover_sub"], S, W-224, 48), fill=t["text"])
    d.text((112, 738), "For builders, by a builder.", font=font(S, 40), fill=t["sub"])
    d.text((80, 930), "swipe  ->", font=font(SB, 38), fill=t["text"])
    _lockup2(img, t, 1, total, t["text"], t["ring"], t["sub"], num_font=font(M, 26))
    return _finish(img)

def _aurora_story(t, spec, sl, entry, idx, total):
    bbg = broll_bg(sl["broll"], t) if sl.get("broll") else None
    if bbg is not None:
        img = bbg.convert("RGBA")
        img.alpha_composite(Image.new("RGBA", (W, H), (4, 6, 18, 60)))
    else:
        img = _rgba(t)
    d = ImageDraw.Draw(img)
    d.text((80, 100), spec["kicker"], font=font(MB, 28), fill=t["kicker"])
    _heading(d, sl["heading"], SB, 66, W-160, t["text"], 80, 170)
    bullets = sl["bullets"]; nb = len(bullets)
    top, bottom, gap = 360, 1080, 24
    ch = (bottom - top - (nb-1)*gap)//nb
    y = top
    for b in bullets:
        _glass_r(img, 80, y, W-160, ch, t["card"], outline=(255, 255, 255, 80), radius=24, width=2)
        d = ImageDraw.Draw(img)
        bf = font(SB, 40)
        lines = wrap(d, b, bf, W-260)
        ty = y + (ch - len(lines)*56)//2 + 6
        for ln in lines:
            d.text((115, ty), ln, font=bf, fill=t["text"]); ty += 56
        y += ch + gap
    if sl.get("tag"):
        _aurora_pill(img, t, sl["tag"])
    _lockup2(img, t, idx, total, t["text"], t["ring"], t["sub"], num_font=font(M, 26))
    return _finish(img)

def _aurora_cta(t, spec, total, npages):
    img = _rgba(t); d = ImageDraw.Draw(img)
    d.text((80, 100), spec["kicker"], font=font(MB, 32), fill=t["kicker"])
    y = 300
    for i, ln in enumerate(spec["cta"]):
        col = t["kicker"] if i == len(spec["cta"]) - 1 else t["text"]
        d.text((80, y), ln, font=fit(d, ln, SB, W-160, 88), fill=col); y += 122
    _lockup2(img, t, npages, total, t["text"], t["ring"], t["sub"], num_font=font(M, 26))
    return _finish(img)

_LAYOUTS = {
    "terminal": (_term_cover, _term_story, _term_cta),
    "editorial": (_ed_cover, _ed_story, _ed_cta),
    "neon": (_neon_cover, _neon_story, _neon_cta),
    "poster": (_poster_cover, _poster_story, _poster_cta),
    "aurora": (_aurora_cover, _aurora_story, _aurora_cta),
}

def build_v2(theme_key, spec, out_pdf):
    t = THEMES[theme_key]
    lay = _LAYOUTS[t["layout"]]
    cover_f, story_f, cta_f = lay[0], lay[1], lay[-1]
    recap_f = lay[2] if len(lay) > 3 else None
    has_recap = recap_f is not None and bool(spec.get("recap"))
    total = spec.get("total_pages", 2 + len(spec["slides"]) + (1 if has_recap else 0))
    pages = [cover_f(t, spec, total)]
    for i, sl in enumerate(spec["slides"]):
        pages.append(story_f(t, spec, sl, i + 1, i + 2, total))
    if has_recap:
        pages.append(recap_f(t, spec, len(pages) + 1, total))
    pages.append(cta_f(t, spec, total, len(pages) + 1))
    pages[0].save(out_pdf, save_all=True, append_images=pages[1:])
    print(f"wrote {out_pdf} ({theme_key}, {len(pages)} pages)")

# ================= Round 4 layout engines (2026-10-14 research archetypes) =================
# Built from the LinkedIn carousel design research (report §1 archetypes, §5 synthesis).
# frontpage = Archetype C (Rundown/Superhuman) + recap slide; explainer = Archetype B
# (Hassid); minimalist = Archetype A (Welsh); statdeck = Archetype F (stat deck).

def _rich_para(d, text, x, y, max_w, f_body, fill, lh, accent, f_label, label_max=18):
    """Render 'Label: rest...' with the label as a small mono accent line above the body."""
    if ": " in text and len(text.split(": ", 1)[0]) <= label_max:
        lab, rest = text.split(": ", 1)
        d.text((x, y), lab.upper(), font=f_label, fill=accent)
        y += int(lh * 0.84)
        text = rest[:1].upper() + rest[1:]
    for ln in wrap(d, text, f_body, max_w):
        d.text((x, y), ln, font=f_body, fill=fill); y += lh
    return y

# ---------------- FRONTPAGE (Archetype C) ----------------
def _fp_cover(t, spec, total):
    img = _rgba(t); d = ImageDraw.Draw(img)
    # masthead
    d.text((W//2, 58), spec["title"], font=fit(d, spec["title"], SRFB, W-140, 116), fill=t["text"], anchor="ma")
    d.line((80, 208, W-80, 208), fill=t["text"], width=7)
    d.line((80, 222, W-80, 222), fill=t["text"], width=2)
    d.text((W//2, 238), spec["date_line"], font=font(MB, 24), fill=t["sub"], anchor="ma")
    # lead story
    lead = spec["lead"]
    d.text((80, 306), "LEAD STORY", font=font(MB, 27), fill=t["kicker"])
    lt = lead["tag"]; ltf = font(MB, 27)
    d.text((W-80, 306), lt, font=ltf, fill=t["sub"], anchor="ra")
    y = _heading(d, lead["heading"], SB, 78, W-160, t["text"], 80, 350)
    y += 8
    for ln in wrap(d, lead["deck"], font(S, 34), W-160):
        d.text((80, y), ln, font=font(S, 34), fill=t["sub"]); y += 45
    y += 14
    d.line((80, y, W-80, y), fill=t["text"], width=3); y += 30
    d.text((80, y), "ALSO IN TODAY'S DIGEST", font=font(MB, 27), fill=t["kicker"]); y += 46
    for i, c in enumerate(spec["contents"]):
        d.text((80, y), f"{c['n']:02d}", font=font(SB, 38), fill=t["kicker"])
        d.text((168, y+2), c["head"], font=fit(d, c["head"], SB, W-168-80, 35, min_s=28), fill=t["text"])
        d.text((168, y+46), c["tease"], font=fit(d, c["tease"], S, W-168-80, 28, min_s=21), fill=t["sub"])
        y += 88
        if i < len(spec["contents"]) - 1:
            d.line((80, y-12, W-80, y-12), fill=t["hair"], width=1)
    d.text((80, 1140), "SWIPE ->", font=font(MB, 27), fill=t["kicker"])
    _lockup2(img, t, 1, total, t["text"], t["ring"], t["sub"], name_font=font(SB, 28), num_font=font(M, 24))
    return _finish(img)

def _fp_story(t, spec, sl, entry, idx, total):
    img = _rgba(t); d = ImageDraw.Draw(img)
    d.text((80, 92), spec["kicker"], font=font(MB, 24), fill=t["sub"])
    d.text((W-80, 92), sl.get("tag", ""), font=font(MB, 26), fill=t["kicker"], anchor="ra")
    d.line((80, 140, W-80, 140), fill=t["text"], width=3)
    y = _heading(d, sl["heading"], SB, 60, W-160, t["text"], 80, 176)
    d.rectangle((80, y+8, 200, y+15), fill=t["kicker"])
    y += 84
    bf = font(S, 36)
    for i, b in enumerate(sl["bullets"]):
        y = _rich_para(d, b, 80, y, W-160, bf, t["text"], 51, t["kicker"], font(MB, 24))
        y += 26
        if i < len(sl["bullets"]) - 1:
            d.line((80, y, W-80, y), fill=t["hair"], width=1); y += 30
    _lockup2(img, t, idx, total, t["text"], t["ring"], t["sub"], name_font=font(SB, 28), num_font=font(M, 24))
    return _finish(img)

def _fp_recap(t, spec, idx, total):
    img = _rgba(t); d = ImageDraw.Draw(img)
    rec = spec["recap"]
    d.text((80, 84), "AI DEV DIGEST", font=font(SB, 34), fill=t["text"])
    d.text((W-80, 92), spec["kicker"], font=font(MB, 22), fill=t["sub"], anchor="ra")
    d.line((80, 140, W-80, 140), fill=t["text"], width=3)
    d.text((80, 168), "Today in one screen", font=font(SB, 56), fill=t["text"])
    d.text((80, 248), "All five stories, one verdict each — save this screen.", font=font(S, 29), fill=t["sub"])
    y = 322
    for i, (head, verdict) in enumerate(rec["rows"]):
        d.text((80, y), f"{i+1:02d}", font=font(SB, 40), fill=t["kicker"])
        hy = y
        for ln in wrap(d, head, font(SB, 33), W-160-92):
            d.text((172, hy), ln, font=font(SB, 33), fill=t["text"]); hy += 44
        vy = hy + 2
        d.text((172, vy), verdict, font=font(S, 28), fill=t["sub"])
        if i < len(rec["rows"]) - 1:
            d.line((80, vy+50, W-80, vy+50), fill=t["hair"], width=1)
        y = vy + 64
    # quotable take block (dark, so the slide survives being forwarded alone)
    d.rounded_rectangle((80, 936, W-80, 1060), radius=18, fill=t["text"])
    d.text((116, 960), rec["take"], font=fit(d, rec["take"], SRFB, W-232, 37), fill=(255, 255, 255))
    d.text((116, 1010), rec["take_sub"], font=font(S, 25), fill=(198, 200, 208))
    _lockup2(img, t, idx, total, t["text"], t["ring"], t["sub"], name_font=font(SB, 28), num_font=font(M, 24))
    return _finish(img)

def _fp_cta(t, spec, total, npages):
    img = _rgba(t); d = ImageDraw.Draw(img)
    d.text((W//2, 92), spec["kicker"], font=font(MB, 26), fill=t["kicker"], anchor="ma")
    d.line((80, 148, W-80, 148), fill=t["text"], width=3)
    ph = circle_photo(250); img.paste(ph, ((W-250)//2, 250), ph)
    d = ImageDraw.Draw(img)
    d.ellipse(((W-250)//2-7, 243, (W+250)//2+7, 507), outline=t["ring"], width=5)
    d.text((W//2, 548), "[YOUR NAME]", font=font(SB, 48), fill=t["text"], anchor="ma")
    _pos = "AI architect — I read the firehose so you don't have to."
    d.text((W//2, 616), _pos, font=fit(d, _pos, S, W-160, 31), fill=t["sub"], anchor="ma")
    y = 730
    for ln in spec["cta"]:
        d.text((W//2, y), ln, font=fit(d, ln, SB, W-160, 60), fill=t["text"], anchor="ma"); y += 84
    _lockup2(img, t, npages, total, t["text"], t["ring"], t["sub"], name_font=font(SB, 28), num_font=font(M, 24))
    return _finish(img)

# ---------------- EXPLAINER (Archetype B) ----------------
def _check_chip(d, x, y, t, size=42):
    d.rounded_rectangle((x, y, x+size, y+size), radius=9, fill=t["kicker"])
    cf = font(SB, int(size*0.72))
    d.text((x+size//2, y+size//2-2), "✓", font=cf, fill=(255, 255, 255), anchor="mm")

def _panel(d, t, panel, x, y, w, h):
    d.rounded_rectangle((x, y, x+w, y+h), radius=16, fill=t["panel_bg"], outline=t["hair"], width=2)
    d.rounded_rectangle((x, y, x+w, y+56), radius=16, fill=t["panel_bar"])
    d.rectangle((x, y+28, x+w, y+56), fill=t["panel_bar"])
    for i, c in enumerate([(206, 84, 72), (214, 164, 62), (64, 186, 94)]):
        cx = x + 30 + i*34
        d.ellipse((cx-9, y+19, cx+9, y+37), fill=c)
    d.text((x+150, y+14), panel["title"], font=font(M, 24), fill=t["sub"])
    kinds = {"cmd": (font(MB, 29), t["text"]), "ok": (font(M, 29), t["ok"]),
             "dim": (font(M, 29), t["sub"]), "plain": (font(M, 29), t["text"])}
    ly = y + 88
    for text, kind in panel["lines"]:
        f, col = kinds.get(kind, kinds["plain"])
        d.text((x+36, ly), text, font=f, fill=col); ly += 54
    return y + h

def _ex_cover(t, spec, total):
    img = _rgba(t); d = ImageDraw.Draw(img)
    d.text((80, 96), "HOW-TO · AI TOOL OF THE DAY", font=font(MB, 27), fill=t["kicker"])
    y = _heading(d, spec["hook"], SB, 80, W-160, t["text"], 80, 176)
    y += 26
    for ln in wrap(d, spec["hook_sub"], font(S, 37), W-160):
        d.text((80, y), ln, font=font(S, 37), fill=t["sub"]); y += 52
    y += 44
    cx = 80
    for chip in spec["chips"]:
        cf = font(MB, 26); tw = d.textbbox((0, 0), chip, font=cf)[2]
        d.rounded_rectangle((cx, y, cx+tw+44, y+58), radius=29, outline=t["kicker"], width=3)
        d.text((cx+22, y+13), chip, font=cf, fill=t["kicker"])
        cx += tw + 44 + 22
    d.text((80, 1010), "swipe  ->", font=font(SB, 36), fill=t["text"])
    _lockup2(img, t, 1, total, t["text"], t["ring"], t["sub"], num_font=font(M, 24))
    return _finish(img)

def _ex_story(t, spec, sl, entry, idx, total):
    img = _rgba(t); d = ImageDraw.Draw(img)
    chip = f"STEP {entry}"
    cf = font(MB, 28); tw = d.textbbox((0, 0), chip, font=cf)[2]
    d.rounded_rectangle((80, 88, 80+tw+44, 88+58), radius=12, fill=t["kicker"])
    d.text((102, 102), chip, font=cf, fill=(255, 255, 255))
    d.text((W-80, 102), sl.get("kicker2", ""), font=font(MB, 24), fill=t["sub"], anchor="ra")
    y = _heading(d, sl["heading"], SB, 56, W-160, t["text"], 80, 182)
    y += 22
    y = _panel(d, t, sl["panel"], 80, y, W-160, 96 + 54*len(sl["panel"]["lines"]))
    y += 52
    for b in sl["bullets"]:
        _check_chip(d, 80, y+4, t, 40)
        for ln in wrap(d, b, font(S, 35), W-160-70):
            d.text((150, y), ln, font=font(S, 35), fill=t["text"]); y += 49
        y += 28
    _lockup2(img, t, idx, total, t["text"], t["ring"], t["sub"], num_font=font(M, 24))
    return _finish(img)

def _ex_cta(t, spec, total, npages):
    img = _rgba(t); d = ImageDraw.Draw(img)
    fin = spec["final"]
    chip = "STEP 3"
    cf = font(MB, 28); tw = d.textbbox((0, 0), chip, font=cf)[2]
    d.rounded_rectangle((80, 88, 80+tw+44, 88+58), radius=12, fill=t["kicker"])
    d.text((102, 102), chip, font=cf, fill=(255, 255, 255))
    y = _heading(d, fin["heading"], SB, 56, W-160, t["text"], 80, 182)
    y += 30
    for item in fin["checklist"]:
        _check_chip(d, 80, y+2, t, 46)
        for ln in wrap(d, item, font(SB, 37), W-160-76):
            d.text((156, y), ln, font=font(SB, 37), fill=t["text"]); y += 52
        y += 30
    y += 26
    d.line((80, y, W-80, y), fill=t["text"], width=3); y += 40
    d.text((80, y), "P.S.", font=font(SB, 40), fill=t["kicker"]); y += 62
    for ln in wrap(d, fin["ps"], font(S, 34), W-160):
        d.text((80, y), ln, font=font(S, 34), fill=t["text"]); y += 48
    _lockup2(img, t, npages, total, t["text"], t["ring"], t["sub"], num_font=font(M, 24))
    return _finish(img)

# ---------------- MINIMALIST (Archetype A) ----------------
def _big(d, text, x, y, max_w, size, fill, max_lines=4, min_s=44):
    """Welsh-style huge type: wrap at full size, shrink only past max_lines."""
    s, f = size, font(SB, size)
    lines = wrap(d, text, f, max_w)
    while len(lines) > max_lines and s > min_s:
        s -= 6; f = font(SB, s); lines = wrap(d, text, f, max_w)
    for ln in lines:
        d.text((x, y), ln, font=f, fill=fill); y += int(s * 1.16)
    return y

def _mn_cover(t, spec, total):
    img = _rgba(t); d = ImageDraw.Draw(img)
    d.text((90, 110), spec["kicker"], font=font(S, 27), fill=t["sub"])
    y = _big(d, spec["big"], 90, 300, W-180, 104, t["text"])
    d.rectangle((90, y+36, 190, y+44), fill=t["text"])
    d.text((90, y+84), spec["small"], font=font(S, 33), fill=t["sub"])
    _lockup2(img, t, 1, total, t["text"], t["ring"], t["sub"], name_font=font(SB, 28), num_font=font(S, 25), num_xy=(90, H-118))
    return _finish(img)

def _mn_story(t, spec, sl, entry, idx, total):
    img = _rgba(t); d = ImageDraw.Draw(img)
    d.text((90, 110), sl.get("tag", ""), font=font(S, 27), fill=t["sub"])
    y = _big(d, sl["heading"], 90, 260, W-180, 88, t["text"], max_lines=4)
    y += 30
    for ln in wrap(d, sl["bullets"][0], font(S, 34), W-180):
        d.text((90, y), ln, font=font(S, 34), fill=t["sub"]); y += 48
    _lockup2(img, t, idx, total, t["text"], t["ring"], t["sub"], name_font=font(SB, 28), num_font=font(S, 25), num_xy=(90, H-118))
    return _finish(img)

def _mn_cta(t, spec, total, npages):
    img = _rgba(t); d = ImageDraw.Draw(img)
    d.text((90, 110), "THE TAKE", font=font(S, 27), fill=t["sub"])
    y = 300
    for ln in spec["cta"]:
        d.text((90, y), ln, font=fit(d, ln, SB, W-180, 96), fill=t["text"]); y += 112
    d.text((90, y+50), "— AI Dev Digest #6 · Oct 13", font=font(S, 31), fill=t["sub"])
    d.text((90, y+104), "Follow for tomorrow's five stories.", font=font(S, 31), fill=t["sub"])
    _lockup2(img, t, npages, total, t["text"], t["ring"], t["sub"], name_font=font(SB, 28), num_font=font(S, 25), num_xy=(90, H-118))
    return _finish(img)

# ---------------- STATDECK (Archetype F) ----------------
def _stat_slide(t, sd, idx, total, cta_lines=None):
    img = _rgba(t); d = ImageDraw.Draw(img)
    d.text((80, 92), sd.get("tag", ""), font=font(MB, 27), fill=t["kicker"])
    d.text((W-80, 92), "AI DEV DIGEST #6", font=font(MB, 22), fill=t["sub"], anchor="ra")
    d.line((80, 144, W-80, 144), fill=t["hair"], width=2)
    sf = fit(d, sd["stat"], SB, W-160, 300, min_s=110)
    _bb = d.textbbox((80, 190), sd["stat"], font=sf)
    d.text((80, 190), sd["stat"], font=sf, fill=t["kicker"])
    y = _bb[3] + 30  # true glyph bottom — "$" strokes descend past size*1.04
    y = _heading(d, sd["heading"], SB, 43, W-160, t["text"], 80, y)
    y += 30
    d.line((80, y, W-80, y), fill=t["hair"], width=2); y += 36
    for b in sd["bullets"]:
        for ln in wrap(d, b, font(S, 33), W-160):
            d.text((80, y), ln, font=font(S, 33), fill=t["sub"]); y += 47
        y += 10
    d.text((80, 1130), "SOURCE — " + sd["source"], font=font(M, 23), fill=t["sub"])
    if cta_lines:
        cy = 950
        d.line((80, cy, W-80, cy), fill=t["kicker"], width=4); cy += 30
        for i, ln in enumerate(cta_lines):
            d.text((80, cy), ln, font=font(SB if i == 0 else S, 36 if i == 0 else 31),
                   fill=t["text"] if i == 0 else t["sub"]); cy += 52
    _lockup2(img, t, idx, total, t["text"], t["ring"], t["sub"], num_font=font(M, 24))
    return _finish(img)

def _sd_cover(t, spec, total):
    img = _rgba(t); d = ImageDraw.Draw(img)
    d.text((80, 96), spec["kicker"], font=font(MB, 27), fill=t["text"])
    d.line((80, 148, W-80, 148), fill=t["text"], width=3)
    d.text((80, 196), "THE NUMBERS ISSUE", font=font(MB, 28), fill=t["kicker"])
    sf = fit(d, spec["cover_stat"], SB, W-160, 380, min_s=140)
    _bb = d.textbbox((80, 250), spec["cover_stat"], font=sf)
    d.text((80, 250), spec["cover_stat"], font=sf, fill=t["kicker"])
    y = _bb[3] + 34
    d.text((80, y), spec["cover_label"], font=font(SB, 48), fill=t["text"]); y += 74
    for ln in wrap(d, spec["cover_sub2"], font(S, 33), W-160):
        d.text((80, y), ln, font=font(S, 33), fill=t["sub"]); y += 47
    d.text((80, 1010), "swipe  ->", font=font(SB, 36), fill=t["text"])
    _lockup2(img, t, 1, total, t["text"], t["ring"], t["sub"], num_font=font(M, 24))
    return _finish(img)

def _sd_story(t, spec, sl, entry, idx, total):
    return _stat_slide(t, sl, idx, total)

def _sd_cta(t, spec, total, npages):
    return _stat_slide(t, spec["final_stat"], npages, total,
                       cta_lines=["One number that matters, every weekday.",
                                  "Follow for the AI Dev Digest."])

_LAYOUTS.update({
    "frontpage": (_fp_cover, _fp_story, _fp_recap, _fp_cta),
    "explainer": (_ex_cover, _ex_story, _ex_cta),
    "minimalist": (_mn_cover, _mn_story, _mn_cta),
    "statdeck": (_sd_cover, _sd_story, _sd_cta),
})

# ================= Round 5 (2026-10-14): Front Page structure ported into the rotation skins =================
# the owner approved frontpage (Archetype C) as the digest's fixed STRUCTURE:
# masthead-style cover with lead story + "ALSO IN TODAY'S DIGEST" contents,
# story slides, "Today in one screen" recap, person-led CTA. The skins below
# keep their visual identity but render that full structure from the same
# extended spec (lead / contents / recap fields). Story renderers are reused
# unchanged; cover / recap / CTA are new per skin.

_POS_LINE = "AI architect — I read the firehose so you don't have to."

def _big_avatar(img, t, cx, y, ring):
    """Centered 250px person-led avatar with ring; returns bottom y."""
    ph = circle_photo(250); img.paste(ph, (cx - 125, y), ph)
    d = ImageDraw.Draw(img)
    d.ellipse((cx - 132, y - 7, cx + 132, y + 257), outline=ring, width=5)
    return y + 250

# ---------------- TERMINAL x FRONTPAGE ----------------
def _term_cover2(t, spec, total):
    img = _rgba(t); _term_chrome(img, t); d = ImageDraw.Draw(img)
    d.text((80, 118), "$ cat ai_dev_digest.md", font=font(M, 27), fill=t["dim"])
    d.text((80, 178), "# " + spec["kicker"], font=font(MB, 33), fill=t["kicker"])
    d.text((80, 238), spec["title"], font=fit(d, spec["title"], MB, W-160, 100), fill=t["text"])
    d.line((80, 378, W-80, 378), fill=t["rule_c"], width=2)
    lead = spec["lead"]
    d.text((80, 408), "> LEAD STORY", font=font(MB, 27), fill=t["kicker"])
    d.text((W-80, 408), lead["tag"], font=font(M, 24), fill=t["sub"], anchor="ra")
    y = _heading(d, lead["heading"], MB, 52, W-160, t["text"], 80, 452, min_s=36)
    y += 14
    for ln in wrap(d, lead["deck"], font(M, 26), W-160):
        d.text((80, y), ln, font=font(M, 26), fill=t["sub"]); y += 37
    y += 12
    d.line((80, y, W-80, y), fill=t["rule_c"], width=2); y += 28
    d.text((80, y), "> ALSO IN TODAY'S DIGEST", font=font(MB, 27), fill=t["kicker"]); y += 46
    for c in spec["contents"]:
        d.text((80, y), f"{c['n']:02d}", font=font(MB, 27), fill=t["kicker"])
        d.text((158, y), c["head"], font=fit(d, c["head"], MB, W-158-80, 27, min_s=21), fill=t["text"])
        d.text((158, y+38), c["tease"], font=fit(d, c["tease"], M, W-158-80, 22, min_s=18), fill=t["dim"])
        y += 74
    d.text((80, 1150), "> swipe ->", font=font(MB, 30), fill=t["kicker"])
    _lockup2(img, t, 1, total, t["text"], t["ring"], t["dim"], name_font=font(MB, 28), num_font=font(M, 26))
    return _finish(img)

def _term_recap(t, spec, idx, total):
    img = _rgba(t); _term_chrome(img, t); d = ImageDraw.Draw(img)
    rec = spec["recap"]
    d.text((80, 118), "$ ./recap.sh --today", font=font(M, 27), fill=t["dim"])
    d.text((80, 178), "> Today in one screen", font=font(MB, 46), fill=t["text"])
    d.text((80, 250), "All five stories, one verdict each — save this screen.", font=font(M, 25), fill=t["sub"])
    y = 332
    for i, (head, verdict) in enumerate(rec["rows"]):
        d.text((80, y), f"[{i+1:02d}]", font=font(MB, 28), fill=t["kicker"])
        d.text((212, y), head, font=fit(d, head, MB, W-212-80, 28, min_s=21), fill=t["text"])
        d.text((212, y+42), verdict, font=fit(d, verdict, M, W-212-80, 24, min_s=19), fill=t["sub"])
        y += 94
        if i < len(rec["rows"]) - 1:
            d.line((80, y-15, W-80, y-15), fill=t["rule_c"], width=1)
    d.rectangle((80, 830, W-80, 1002), outline=t["kicker"], width=2)
    d.text((116, 862), rec["take"], font=fit(d, rec["take"], MB, W-232, 34), fill=t["text"])
    d.text((116, 924), rec["take_sub"], font=fit(d, rec["take_sub"], M, W-232, 24, min_s=19), fill=t["sub"])
    d.text((80, 1044), "# EOF — recap complete", font=font(M, 24), fill=t["dim"])
    _lockup2(img, t, idx, total, t["text"], t["ring"], t["dim"], name_font=font(MB, 28), num_font=font(M, 26))
    return _finish(img)

def _term_cta2(t, spec, total, npages):
    img = _rgba(t); _term_chrome(img, t); d = ImageDraw.Draw(img)
    d.text((80, 130), "$ whoami", font=font(M, 28), fill=t["dim"])
    _big_avatar(img, t, W//2, 210, t["ring"])
    d = ImageDraw.Draw(img)
    d.text((W//2, 512), "[YOUR NAME]", font=font(MB, 44), fill=t["text"], anchor="ma")
    d.text((W//2, 580), _POS_LINE, font=fit(d, _POS_LINE, M, W-160, 26, min_s=20), fill=t["sub"], anchor="ma")
    y = 692
    for i, ln in enumerate(spec["cta"]):
        col = t["kicker"] if i == len(spec["cta"]) - 1 else t["text"]
        d.text((W//2, y), ln, font=fit(d, ln, MB, W-200, 56), fill=col, anchor="ma"); y += 84
    d.text((W//2, y+28), "# EOF — exit 0", font=font(M, 26), fill=t["dim"], anchor="ma")
    _lockup2(img, t, npages, total, t["text"], t["ring"], t["dim"], name_font=font(MB, 28), num_font=font(M, 26))
    return _finish(img)

# ---------------- NEON GRID x FRONTPAGE ----------------
def _neon_cover2(t, spec, total):
    img = _neon_bg(t, spec); d = ImageDraw.Draw(img)
    d.text((80, 90), spec["kicker"], font=font(MB, 32), fill=t["kicker"])
    bar = _hgrad(260, 10, t["kicker"], t["accent2"]).convert("RGBA"); img.paste(bar, (80, 140), bar)
    d = ImageDraw.Draw(img)
    d.text((80, 180), spec["title"], font=fit(d, spec["title"], SB, W-160, 118), fill=t["text"])
    lead = spec["lead"]
    _neon_panel(img, t, 80, 350, W-160, 372)
    d = ImageDraw.Draw(img)
    d.text((112, 382), "LEAD STORY", font=font(MB, 26), fill=t["kicker"])
    d.text((W-112, 382), lead["tag"], font=font(MB, 24), fill=t["accent2"], anchor="ra")
    y = _heading(d, lead["heading"], SB, 54, W-224, t["text"], 112, 428)
    y += 10
    for ln in wrap(d, lead["deck"], font(S, 29), W-224):
        d.text((112, y), ln, font=font(S, 29), fill=t["sub"]); y += 40
    d.text((80, 772), "ALSO IN TODAY'S DIGEST", font=font(MB, 26), fill=t["kicker"])
    y = 820
    for c in spec["contents"]:
        d.text((80, y), f"{c['n']:02d}", font=font(SB, 32), fill=t["accent2"])
        d.text((158, y+1), c["head"], font=fit(d, c["head"], SB, W-158-80, 31, min_s=25), fill=t["text"])
        d.text((158, y+42), c["tease"], font=fit(d, c["tease"], S, W-158-80, 25, min_s=20), fill=t["sub"])
        y += 74
    d.text((80, 1150), "swipe  ->", font=font(SB, 32), fill=t["text"])
    _lockup2(img, t, 1, total, t["text"], t["ring"], t["kicker"], num_font=font(M, 26))
    return _finish(img)

def _neon_recap(t, spec, idx, total):
    img = _neon_bg(t, spec); d = ImageDraw.Draw(img)
    rec = spec["recap"]
    d.text((80, 88), spec["kicker"], font=font(MB, 26), fill=t["kicker"])
    d.text((80, 140), "Today in one screen", font=font(SB, 56), fill=t["text"])
    d.text((80, 222), "All five stories, one verdict each — save this screen.", font=font(S, 27), fill=t["sub"])
    y = 300
    for i, (head, verdict) in enumerate(rec["rows"]):
        _neon_panel(img, t, 80, y, W-160, 100)
        d = ImageDraw.Draw(img)
        d.text((112, y+30), f"{i+1:02d}", font=font(SB, 32), fill=t["accent2"])
        d.text((196, y+16), head, font=fit(d, head, SB, W-196-96, 30, min_s=24), fill=t["text"])
        d.text((196, y+56), verdict, font=fit(d, verdict, S, W-196-96, 24, min_s=19), fill=t["sub"])
        y += 116
    _glass_r(img, 80, 896, W-160, 150, t["card"], outline=tuple(list(t["accent2"]) + [200]), radius=24, width=2)
    d = ImageDraw.Draw(img)
    d.text((112, 924), rec["take"], font=fit(d, rec["take"], SB, W-224, 36), fill=t["text"])
    d.text((112, 978), rec["take_sub"], font=fit(d, rec["take_sub"], S, W-224, 25, min_s=20), fill=t["sub"])
    _lockup2(img, t, idx, total, t["text"], t["ring"], t["kicker"], num_font=font(M, 26))
    return _finish(img)

def _neon_cta2(t, spec, total, npages):
    img = _neon_bg(t, spec); d = ImageDraw.Draw(img)
    d.text((80, 90), spec["kicker"], font=font(MB, 30), fill=t["kicker"])
    bar = _hgrad(260, 10, t["kicker"], t["accent2"]).convert("RGBA"); img.paste(bar, (80, 138), bar)
    _big_avatar(img, t, W//2, 215, t["ring"])
    d = ImageDraw.Draw(img)
    d.text((W//2, 517), "[YOUR NAME]", font=font(SB, 48), fill=t["text"], anchor="ma")
    d.text((W//2, 585), _POS_LINE, font=fit(d, _POS_LINE, S, W-160, 29, min_s=22), fill=t["sub"], anchor="ma")
    y = 722
    for i, ln in enumerate(spec["cta"]):
        col = t["accent2"] if i == len(spec["cta"]) - 1 else t["text"]
        d.text((80, y), ln, font=fit(d, ln, SB, W-160, 80), fill=col); y += 116
    _lockup2(img, t, npages, total, t["text"], t["ring"], t["kicker"], num_font=font(M, 26))
    return _finish(img)

# ---------------- BOLD POSTER x FRONTPAGE ----------------
def _poster_cover2(t, spec, total):
    img = _rgba(t); d = ImageDraw.Draw(img)
    acc = t["kicker"]
    import re as _re
    m = _re.search(r"#(\d+)", spec["kicker"])
    ed = f"{int(m.group(1)):02d}" if m else "01"
    ghost = _blend(acc, t["bg"][0], 0.14)
    d.text((W-370, 56), ed, font=font(SB, 240), fill=ghost)
    d.rectangle((80, 104, 100, 124), fill=acc)
    d.text((116, 96), spec["kicker"], font=font(MB, 28), fill=t["text"])
    d.text((74, 168), spec["title"], font=fit(d, spec["title"], SB, W-148, 148), fill=t["text"])
    d.rectangle((80, 352, 470, 380), fill=acc)
    lead = spec["lead"]
    d.text((80, 408), "LEAD STORY", font=font(MB, 26), fill=acc)
    d.text((W-80, 408), lead["tag"], font=font(MB, 24), fill=t["sub"], anchor="ra")
    y = _heading(d, lead["heading"], SB, 54, W-160, t["text"], 80, 452)
    y += 12
    for ln in wrap(d, lead["deck"], font(S, 29), W-160):
        d.text((80, y), ln, font=font(S, 29), fill=t["sub"]); y += 40
    y += 8
    d.line((80, y, W-80, y), fill=t["text"], width=3); y += 28
    d.text((80, y), "ALSO IN TODAY'S DIGEST", font=font(MB, 26), fill=acc); y += 44
    for c in spec["contents"]:
        d.text((80, y), f"{c['n']:02d}", font=font(SB, 30), fill=acc)
        d.text((158, y+1), c["head"], font=fit(d, c["head"], SB, W-158-80, 30, min_s=24), fill=t["text"])
        d.text((158, y+40), c["tease"], font=fit(d, c["tease"], S, W-158-80, 24, min_s=19), fill=t["sub"])
        y += 72
    d.text((80, 1150), "SWIPE ->", font=font(MB, 30), fill=t["text"])
    _lockup2(img, t, 1, total, t["text"], t["ring"], t["text"], num_font=font(SB, 32), num_xy=(80, H-124))
    return _finish(img)

def _poster_recap(t, spec, idx, total):
    img = _rgba(t); d = ImageDraw.Draw(img)
    acc = t["kicker"]
    rec = spec["recap"]
    d.rectangle((0, 0, 110, H), fill=acc)
    d.text((W-80, 84), spec["kicker"], font=font(MB, 22), fill=t["sub"], anchor="ra")
    d.text((190, 104), "AI DEV DIGEST — RECAP", font=font(MB, 26), fill=acc)
    _heading(d, "Today in one screen", SB, 68, W-190-70, t["text"], 190, 148)
    d.text((190, 256), "All five stories, one verdict each — save this screen.",
           font=fit(d, "All five stories, one verdict each — save this screen.", S, W-190-70, 27, min_s=21), fill=t["sub"])
    accents = [t["slot_accents"].get(k, acc) for k in ("PRODUCT", "FRAMEWORKS", "REPO", "RESEARCH", "ECOSYSTEM")]
    y = 330
    for i, (head, verdict) in enumerate(rec["rows"]):
        a = accents[i % len(accents)]
        d.text((190, y), f"{i+1:02d}", font=font(SB, 58), fill=a)
        d.text((330, y+4), head, font=fit(d, head, SB, W-330-70, 32, min_s=25), fill=t["text"])
        d.text((330, y+48), verdict, font=fit(d, verdict, S, W-330-70, 25, min_s=20), fill=t["sub"])
        y += 104
        if i < len(rec["rows"]) - 1:
            d.line((190, y-22, W-70, y-22), fill=t["text"], width=1)
    d.rectangle((190, 872, W-70, 1010), fill=t["text"])
    d.text((226, 900), rec["take"], font=fit(d, rec["take"], SB, W-70-190-72, 36), fill=(255, 255, 255))
    d.text((226, 954), rec["take_sub"], font=fit(d, rec["take_sub"], S, W-70-190-72, 24, min_s=19), fill=(198, 200, 208))
    _lockup2(img, t, idx, total, t["text"], t["ring"], t["text"], num_font=font(SB, 32), num_xy=(190, H-124))
    return _finish(img)

def _poster_cta2(t, spec, total, npages):
    img = _rgba(t); d = ImageDraw.Draw(img)
    acc = t["kicker"]
    d.rectangle((0, 0, 110, H), fill=acc)
    d.text((190, 96), spec["kicker"], font=font(MB, 26), fill=t["text"])
    ph = circle_photo(250); img.paste(ph, (190, 190), ph)
    d = ImageDraw.Draw(img)
    d.ellipse((183, 183, 447, 447), outline=t["ring"], width=5)
    d.text((190, 486), "[YOUR NAME]", font=font(SB, 52), fill=t["text"])
    d.text((190, 556), _POS_LINE, font=fit(d, _POS_LINE, S, W-190-70, 29, min_s=22), fill=t["sub"])
    y = 680
    for i, ln in enumerate(spec["cta"]):
        col = acc if i == len(spec["cta"]) - 1 else t["text"]
        d.text((190, y), ln, font=fit(d, ln, SB, W-190-70, 80), fill=col); y += 116
    ay = y + 24
    d.rectangle((190, ay, 360, ay+26), fill=acc)
    d.polygon([(360, ay-20), (360, ay+46), (436, ay+13)], fill=acc)
    _lockup2(img, t, npages, total, t["text"], t["ring"], t["text"], num_font=font(SB, 32), num_xy=(190, H-124))
    return _finish(img)

# ---------------- AURORA x FRONTPAGE ----------------
def _aurora_cover2(t, spec, total):
    img = _rgba(t); d = ImageDraw.Draw(img)
    d.text((80, 96), spec["kicker"], font=font(MB, 32), fill=t["kicker"])
    d.text((80, 178), spec["title"], font=fit(d, spec["title"], SB, W-160, 118), fill=t["text"])
    lead = spec["lead"]
    _glass_r(img, 80, 348, W-160, 374, t["card"], outline=(255, 255, 255, 110), radius=30, width=2)
    d = ImageDraw.Draw(img)
    d.text((112, 380), "LEAD STORY", font=font(MB, 26), fill=t["kicker"])
    d.text((W-112, 380), lead["tag"], font=font(MB, 24), fill=t["sub"], anchor="ra")
    y = _heading(d, lead["heading"], SB, 54, W-224, t["text"], 112, 426)
    y += 10
    for ln in wrap(d, lead["deck"], font(S, 29), W-224):
        d.text((112, y), ln, font=font(S, 29), fill=t["sub"]); y += 40
    d.text((80, 770), "ALSO IN TODAY'S DIGEST", font=font(MB, 26), fill=t["kicker"])
    y = 818
    for c in spec["contents"]:
        d.text((80, y), f"{c['n']:02d}", font=font(SB, 32), fill=t["kicker"])
        d.text((158, y+1), c["head"], font=fit(d, c["head"], SB, W-158-80, 31, min_s=25), fill=t["text"])
        d.text((158, y+40), c["tease"], font=fit(d, c["tease"], S, W-158-80, 25, min_s=20), fill=t["sub"])
        y += 74
    d.text((80, 1150), "swipe  ->", font=font(SB, 32), fill=t["text"])
    _lockup2(img, t, 1, total, t["text"], t["ring"], t["sub"], num_font=font(M, 26))
    return _finish(img)

def _aurora_recap(t, spec, idx, total):
    img = _rgba(t); d = ImageDraw.Draw(img)
    rec = spec["recap"]
    d.text((80, 88), spec["kicker"], font=font(MB, 26), fill=t["kicker"])
    d.text((80, 140), "Today in one screen", font=font(SB, 56), fill=t["text"])
    d.text((80, 222), "All five stories, one verdict each — save this screen.", font=font(S, 27), fill=t["sub"])
    y = 300
    for i, (head, verdict) in enumerate(rec["rows"]):
        _glass_r(img, 80, y, W-160, 100, t["card"], outline=(255, 255, 255, 80), radius=24, width=2)
        d = ImageDraw.Draw(img)
        d.text((112, y+30), f"{i+1:02d}", font=font(SB, 32), fill=t["kicker"])
        d.text((196, y+16), head, font=fit(d, head, SB, W-196-96, 30, min_s=24), fill=t["text"])
        d.text((196, y+56), verdict, font=fit(d, verdict, S, W-196-96, 24, min_s=19), fill=t["sub"])
        y += 116
    _glass_r(img, 80, 896, W-160, 150, t["card"], outline=tuple(list(t["kicker"]) + [200]), radius=24, width=2)
    d = ImageDraw.Draw(img)
    d.text((112, 924), rec["take"], font=fit(d, rec["take"], SB, W-224, 36), fill=t["text"])
    d.text((112, 978), rec["take_sub"], font=fit(d, rec["take_sub"], S, W-224, 25, min_s=20), fill=t["sub"])
    _lockup2(img, t, idx, total, t["text"], t["ring"], t["sub"], num_font=font(M, 26))
    return _finish(img)

def _aurora_cta2(t, spec, total, npages):
    img = _rgba(t); d = ImageDraw.Draw(img)
    d.text((80, 96), spec["kicker"], font=font(MB, 30), fill=t["kicker"])
    _big_avatar(img, t, W//2, 215, t["ring"])
    d = ImageDraw.Draw(img)
    d.text((W//2, 517), "[YOUR NAME]", font=font(SB, 48), fill=t["text"], anchor="ma")
    d.text((W//2, 585), _POS_LINE, font=fit(d, _POS_LINE, S, W-160, 29, min_s=22), fill=t["sub"], anchor="ma")
    y = 722
    for i, ln in enumerate(spec["cta"]):
        col = t["kicker"] if i == len(spec["cta"]) - 1 else t["text"]
        d.text((80, y), ln, font=fit(d, ln, SB, W-160, 80), fill=col); y += 116
    _lockup2(img, t, npages, total, t["text"], t["ring"], t["sub"], num_font=font(M, 26))
    return _finish(img)

_LAYOUTS.update({
    "terminal": (_term_cover2, _term_story, _term_recap, _term_cta2),
    "neon": (_neon_cover2, _neon_story, _neon_recap, _neon_cta2),
    "poster": (_poster_cover2, _poster_story, _poster_recap, _poster_cta2),
    "aurora": (_aurora_cover2, _aurora_story, _aurora_recap, _aurora_cta2),
})

if __name__ == "__main__":
    key, spec_path, out = sys.argv[1], sys.argv[2], sys.argv[3]
    build(key, json.load(open(spec_path)), out)
