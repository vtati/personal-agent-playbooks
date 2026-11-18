#!/usr/bin/env python3
"""
LinkedIn carousel (document post) generator for the owner's LinkedIn pipeline.

Takes a JSON spec and renders a 1080x1350-per-page PDF:
  - cover slide: kicker + big hook headline
  - content slides: heading + short bullets
  - closing slide: CTA + handle

Usage:
    python3 linkedin_carousel.py spec.json out.pdf

Spec JSON shape:
{
  "kicker": "BUILD IN PUBLIC · WEEK 1",
  "title": "The hook headline for the cover",
  "slides": [
    {"heading": "Slide heading", "bullets": ["point one", "point two"]},
    ...
  ],
  "cta": ["Follow for the unfiltered version.", "New build every week."],
  "handle": "[YOUR NAME] · [YOUR BRAND]"
}

Design: premium dark theme (deep navy, teal accent). Text auto-fits every
slide — nothing may clip at the edges.
"""
import json
import sys
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
BG = (11, 18, 32)          # deep navy-black
ACCENT = (45, 212, 191)    # teal
WHITE = (255, 255, 255)
MUTED = (148, 163, 184)
CARD = (17, 28, 48)        # slightly lighter panel

def font(name, size):
    # DejaVu ships with most Linux distros; fall back to default bitmap font.
    try:
        if name == "bold":
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
    except OSError:
        return ImageFont.load_default()

def fit_font(draw, text, weight, max_width, start_size, min_size=20):
    """Shrink font until the longest line fits max_width."""
    size = start_size
    while size > min_size:
        f = font(weight, size)
        lines = text.split("\n")
        widest = max(draw.textbbox((0, 0), ln, font=f)[2] for ln in lines) if lines else 0
        if widest <= max_width:
            return f
        size -= 4
    return font(weight, min_size)

def wrap(draw, text, f, max_width):
    """Word-wrap text to fit max_width, returns list of lines."""
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textbbox((0, 0), trial, font=f)[2] <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines or [""]

def fit_block(draw, text, weight, max_width, max_height, start_size, min_size=28):
    """Wrap first, then shrink until the longest wrapped line fits max_width
    and the whole block fits max_height. Returns (font, lines, line_height)."""
    size = start_size
    while size >= min_size:
        f = font(weight, size)
        lines = []
        for para in text.split("\n"):
            lines.extend(wrap(draw, para, f, max_width))
        ascent, descent = f.getmetrics()
        lh = int((ascent + descent) * 1.22)
        widest = max((draw.textbbox((0, 0), ln, font=f)[2] for ln in lines), default=0)
        if widest <= max_width and lh * len(lines) <= max_height:
            return f, lines, lh
        size -= 4
    f = font(weight, min_size)
    lines = []
    for para in text.split("\n"):
        lines.extend(wrap(draw, para, f, max_width))
    ascent, descent = f.getmetrics()
    return f, lines, int((ascent + descent) * 1.22)

def draw_footer(draw, handle, page_no, total):
    f = font("regular", 30)
    draw.text((72, H - 110), handle, font=f, fill=MUTED)
    tag = f"{page_no:02d} / {total:02d}"
    bbox = draw.textbbox((0, 0), tag, font=f)
    draw.text(((W - 72 - (bbox[2] - bbox[0])), H - 110), tag, font=f, fill=MUTED)
    # thin accent rule above footer
    draw.line([(72, H - 160), (W - 72, H - 160)], fill=(30, 45, 70), width=2)

def cover_slide(spec):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # accent bar top
    d.rectangle([(0, 0), (W, 14)], fill=ACCENT)
    # kicker
    kf = fit_font(d, spec.get("kicker", ""), "bold", W - 144, 40)
    d.text((72, 120), spec.get("kicker", ""), font=kf, fill=ACCENT)
    # title (wrap first, then auto-fit the block)
    tf, lines, lh = fit_block(d, spec.get("title", ""), "bold", W - 144, H - 720, 110)
    y = 230
    for ln in lines:
        d.text((72, y), ln, font=tf, fill=WHITE)
        y += lh
    # sub-line
    if spec.get("subtitle"):
        sf = fit_font(d, spec["subtitle"], "regular", W - 144, 44)
        d.text((72, y + 30), spec["subtitle"], font=sf, fill=MUTED)
    draw_footer(d, spec.get("handle", ""), 1, spec["_total"])
    return img

def content_slide(spec, idx, slide):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    n = idx + 2  # cover is 1
    # slide counter
    cf = font("bold", 36)
    d.text((72, 100), f"{n:02d}", font=cf, fill=ACCENT)
    # heading (wrap first, then auto-fit the block)
    hf, lines, lh = fit_block(d, slide.get("heading", ""), "bold", W - 144, 320, 72)
    y = 170
    for ln in lines[:3]:
        d.text((72, y), ln, font=hf, fill=WHITE)
        y += lh
    y += 30
    # bullets
    bf = font("regular", 44)
    for b in slide.get("bullets", [])[:6]:
        blines = wrap(d, b, bf, W - 200)
        # re-fit bullet block if too tall
        while y + len(blines) * 68 > H - 220 and bf.size > 28:
            bf = font("regular", bf.size - 4)
            blines = wrap(d, b, bf, W - 200)
        d.text((72, y + 8), "—", font=font("bold", bf.size), fill=ACCENT)
        by = y
        for bl in blines[:3]:
            d.text((140, by), bl, font=bf, fill=(226, 232, 240))
            by += 68
        y = by + 26
        if y > H - 240:
            break
    draw_footer(d, spec.get("handle", ""), n, spec["_total"])
    return img

def closing_slide(spec):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([(0, 0), (W, 14)], fill=ACCENT)
    kf = fit_font(d, "FOLLOW ALONG", "bold", W - 144, 40)
    d.text((72, 140), "FOLLOW ALONG", font=kf, fill=ACCENT)
    lines = []
    cta_text = "\n".join(spec.get("cta", []))
    cf = fit_font(d, cta_text, "bold", W - 144, 76)
    for para in spec.get("cta", []):
        lines.extend(wrap(d, para, cf, W - 144))
    y = 240
    lh = cf.getbbox("Ag")[3] + 26
    for ln in lines:
        d.text((72, y), ln, font=cf, fill=WHITE)
        y += lh
    # handle card
    d.rounded_rectangle([(72, H - 420), (W - 72, H - 220)], radius=24, fill=CARD)
    hf = fit_font(d, spec.get("handle", ""), "bold", W - 240, 52)
    d.text((120, H - 350), spec.get("handle", ""), font=hf, fill=WHITE)
    sf = font("regular", 34)
    d.text((120, H - 290), "[YOUR HEADLINE]", font=sf, fill=MUTED)  # SETUP: your role · venture line
    draw_footer(d, spec.get("handle", ""), spec["_total"], spec["_total"])
    return img

def main():
    if len(sys.argv) != 3:
        print("usage: linkedin_carousel.py spec.json out.pdf", file=sys.stderr)
        sys.exit(1)
    spec = json.load(open(sys.argv[1]))
    total = 2 + len(spec.get("slides", []))
    spec["_total"] = total
    pages = [cover_slide(spec)]
    for i, s in enumerate(spec.get("slides", [])):
        pages.append(content_slide(spec, i, s))
    pages.append(closing_slide(spec))
    pages[0].save(sys.argv[2], save_all=True, append_images=pages[1:])
    print(f"wrote {sys.argv[2]} ({total} pages)")

if __name__ == "__main__":
    main()
