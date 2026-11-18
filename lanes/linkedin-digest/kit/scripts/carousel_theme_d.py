#!/usr/bin/env python3
"""Theme D 'Aurora Gradient' LinkedIn carousel builder — the owner's standing carousel style.
Usage: python3 carousel_theme_d.py spec.json out.pdf
Spec: {kicker, title, cover_sub, slides:[{heading, bullets:[...]}], cta:[...], }
Renders 1080x1350 PDF: cover + content slides + closing. Avatar lockup on every slide."""
import json, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1350
FD = "/usr/share/fonts/truetype/dejavu"
PHOTO = os.path.expanduser("~/workspace/linkedin-digest/brand/avatar.jpg")  # SETUP: point this at YOUR avatar image (see brand/README.md)

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

def aurora_bg():
    top, mid, bot = (72, 32, 130), (12, 110, 150), (16, 24, 64)
    img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
    for y in range(H):
        t = y/(H-1)
        if t < 0.5:
            u = t*2; c = tuple(int(top[i]+(mid[i]-top[i])*u) for i in range(3))
        else:
            u = (t-0.5)*2; c = tuple(int(mid[i]+(bot[i]-mid[i])*u) for i in range(3))
        d.line((0, y, W, y), fill=c)
    ov = Image.new("RGBA", (W, H), (0,0,0,0))
    for (cx, cy, r, col) in [(880, 260, 420, (255,120,180,70)), (180, 1080, 460, (255,150,60,55))]:
        m = Image.new("L", (W, H), 0)
        ImageDraw.Draw(m).ellipse((cx-r, cy-r, cx+r, cy+r), fill=255)
        m = m.filter(ImageFilter.GaussianBlur(120))
        ov = Image.alpha_composite(ov, Image.composite(Image.new("RGBA",(W,H),col), Image.new("RGBA",(W,H),(0,0,0,0)), m))
    return Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")

def circle_photo(d):
    im = Image.open(PHOTO).convert("RGB")
    w, h = im.size
    # Tight headshot: face fills the frame — center square crop fits it exactly.
    side = min(w, h)
    face = im.crop(((w-side)//2, (h-side)//2, (w-side)//2+side, (h-side)//2+side))
    # Slight inset so the circle edge never clips hairline/chin.
    inner = int(d * 0.96)
    face = face.resize((inner, inner), Image.LANCZOS)
    canvas = Image.new("RGBA", (d, d), (0,0,0,0))
    canvas.paste(face, ((d-inner)//2, (d-inner)//2))
    mask = Image.new("L", (d, d), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, d, d), fill=255)
    out = Image.new("RGBA", (d, d), (0,0,0,0)); out.paste(canvas, (0,0), mask)
    return out

def avatar_lockup(base, total_n):
    d = ImageDraw.Draw(base); s = 150
    x, y = W-80-s, H-80-s
    f = font("DejaVuSans-Bold", 30)
    tw = d.textbbox((0,0), "[YOUR NAME]", font=f)[2]
    d.text((x-tw-24, y+s//2-20), "[YOUR NAME]", font=f, fill=(255,255,255))
    d.ellipse((x-6, y-6, x+s+6, y+s+6), outline=(255,255,255), width=5)
    ph = circle_photo(s); base.paste(ph, (x, y), ph)
    d.text((80, H-110), f"{total_n[0]:02d} / {total_n[1]:02d}", font=font("DejaVuSans", 26), fill=(255,255,255))
    total_n[0] += 1

def glass_card(base, x, y, w, h):
    card = Image.new("RGBA", (w, h), (255,255,255,34))
    base.paste(card, (x, y), card)

def build(spec, out_pdf):
    bg = aurora_bg()
    pages, n = [], [1]
    total = 2 + len(spec["slides"])
    kick = spec["kicker"]

    # COVER
    img = bg.copy(); d = ImageDraw.Draw(img)
    kick_txt = " ".join(kick.upper())
    d.text((80, 100), kick_txt, font=fit(d, kick_txt, "DejaVuSansMono-Bold", W-160, 34, min_s=16), fill=(255,255,255))
    # Title: wrap at a large fixed size (never single-line shrink) — pick the
    # largest size that wraps to <=4 lines.
    tf, tlines = None, None
    for sz in (84, 76, 68, 60, 54):
        cand = font("DejaVuSans-Bold", sz)
        ls = wrap(d, spec["title"], cand, W-160)
        if len(ls) <= 4:
            tf, tlines = cand, ls; break
    if tf is None:
        tf = font("DejaVuSans-Bold", 54); tlines = wrap(d, spec["title"], tf, W-160)
    ty = 210; tlh = int(tf.size * 1.22)
    for ln in tlines:
        d.text((80, ty), ln, font=tf, fill=(255,255,255)); ty += tlh
    glass_card(img, 80, 640, W-160, 190); d = ImageDraw.Draw(img)
    sf = font("DejaVuSans", 40)
    slines = wrap(d, spec["cover_sub"], sf, W-220)
    sy = 640 + (190 - len(slines)*52)//2
    for ln in slines:
        d.text((110, sy), ln, font=sf, fill=(255,255,255)); sy += 52
    d.text((80, 920), "swipe  →", font=font("DejaVuSans-Bold", 38), fill=(255,255,255))
    avatar_lockup(img, [1, total]); pages.append(img)

    # CONTENT
    for sl in spec["slides"]:
        img = bg.copy(); d = ImageDraw.Draw(img)
        d.text((80, 100), kick_txt, font=fit(d, kick_txt, "DejaVuSansMono-Bold", W-160, 30, min_s=16), fill=(255,255,255))
        d.text((80, 175), sl["heading"], font=fit(d, sl["heading"], "DejaVuSans-Bold", W-160, 68), fill=(255,255,255))
        bullets, nb = sl["bullets"], len(sl["bullets"])
        top, bottom, gap = 360, 1080, 24
        ch = (bottom - top - (nb-1)*gap)//nb
        y = top
        for b in bullets:
            glass_card(img, 80, y, W-160, ch); d = ImageDraw.Draw(img)
            bf = font("DejaVuSans-Bold", 40 if nb <= 3 else 36)
            lines = wrap(d, b, bf, W-260)
            lh = 56 if nb <= 3 else 50
            ty = y + (ch - len(lines)*lh)//2 + 6
            for ln in lines:
                d.text((115, ty), ln, font=bf, fill=(255,255,255)); ty += lh
            y += ch + gap
        avatar_lockup(img, [n[0]+1 if False else len(pages)+1, total]); pages.append(img)

    # CLOSING
    img = bg.copy(); d = ImageDraw.Draw(img)
    d.text((80, 100), " ".join(kick.upper()), font=font("DejaVuSansMono-Bold", 34), fill=(255,255,255))
    cta = "\n".join(spec["cta"])
    d.text((80, 300), cta, font=fit(d, cta, "DejaVuSans-Bold", W-160, 96), fill=(255,255,255))
    d.text((80, 700), "Full breakdown in the post caption. ↓", font=font("DejaVuSans", 40), fill=(235,235,245))
    avatar_lockup(img, [len(pages)+1, total]); pages.append(img)

    pages[0].save(out_pdf, save_all=True, append_images=pages[1:])
    print(f"wrote {out_pdf} ({len(pages)} pages)")

if __name__ == "__main__":
    build(json.load(open(sys.argv[1])), sys.argv[2])
