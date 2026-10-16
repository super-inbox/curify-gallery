# -*- coding: utf-8 -*-
"""
Three 1:1 English cards for /tools/ai-fashion-model-generator
(spec: curify-frontend/docs/seo-ai-fashion-model-generator-spec-2026-09-21.md).

  en-01-seven-rejection-classes.jpg  — the buyer's own ordering, paraphrased
  en-02-qa-rubric-27.jpg             — the 27 checks, by section
  en-03-three-failures.jpg           — the classes that survive the most revisions

Palette, margins and typography follow the house cards: make_a4_ratio_card.py
and make_apparel_rn_cards.py. Square 1200 to match a4-two-ratio-check.jpg.

⛔ Nothing here is traced from, cropped from or derived from any client or lead
asset. Every mark is drawn by this script. The seven classes and the rubric are
paraphrases; no brand name, style number, counterparty name or filename from any
source record appears. No success-rate or delivered-outcome claim is made —
this is a method rubric, not a track record (axes.json -> provenance_rules).
"""
from PIL import Image, ImageDraw, ImageFont

OUT = "/Users/qqwjq/curify-gallery/smm_daily/2026-09-01-ecommerce/"
W = H = 1200
BG, INK, MUTE, ACC = (250, 248, 242), (26, 26, 26), (122, 118, 108), (192, 82, 30)
CARD, RULE, GOOD = (255, 255, 255), (226, 222, 212), (58, 106, 84)
M = 78

def f(p, s):
    try: return ImageFont.truetype(p, s)
    except Exception: return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", s)
ARB = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
AR  = "/System/Library/Fonts/Supplemental/Arial.ttf"

def head(d, eyebrow, l1, l2=None, l2col=INK):
    d.text((M, 74), eyebrow, font=f(ARB, 24), fill=ACC)
    d.text((M, 126), l1, font=f(ARB, 60), fill=INK)
    if l2: d.text((M, 198), l2, font=f(AR, 60), fill=l2col)

def foot(d, t1, t2, top=H - 176):
    d.rounded_rectangle([M, top, W - M, top + 100], radius=14, fill=INK)
    d.text((M + 26, top + 20), t1, font=f(ARB, 22), fill=(240, 198, 168))
    d.text((M + 26, top + 56), t2, font=f(AR, 20), fill=(196, 192, 184))
    d.text((M, H - 50), "curify-ai.com  ·  /tools/ai-fashion-model-generator",
           font=f(AR, 20), fill=MUTE)

def pill(d, x, y, text, fg=(255, 255, 255), bg=ACC, size=18):
    fo = f(ARB, size); tw = int(d.textlength(text, font=fo))
    a, de = fo.getmetrics()
    d.rounded_rectangle([x, y, x + tw + 24, y + a + de + 10], radius=8, fill=bg)
    d.text((x + 12, y + 5), text, font=fo, fill=fg)

def wrap(d, text, fo, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fo) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

# ═══════════════════════════════ 01 · seven rejection classes
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
head(d, "APPAREL AI IMAGERY  ·  THE BUYER'S OWN LIST", "Seven things", "that get an image rejected.")
rows = [
    ("The garment is not the garment", "A beautiful photo of the wrong product. Returns follow.", True),
    ("Stiff posing", "Arms pinned, feet parallel, expression empty.", False),
    ("Oily skin and hair", "Over-smoothed. The AI tells are visible.", False),
    ("Head too large, reads heavy", "Proportion is judged before anything else.", False),
    ("Colour deviation", "Uneven skin tone, and drift between studio and outdoor.", False),
    ("Season mismatch in styling", "Summer garment, winter accessories.", False),
    ("Images too similar", "Same background, or near-identical pose.", False),
]
y = 306
for i, (title, gloss, flag) in enumerate(rows, 1):
    d.text((M, y - 2), str(i), font=f(ARB, 34), fill=MUTE if i > 1 else ACC)
    d.text((M + 58, y), title, font=f(ARB, 31), fill=INK)
    if flag:
        pill(d, M + 58 + int(d.textlength(title, font=f(ARB, 31))) + 16, y + 2, "TOP PRIORITY")
    d.text((M + 58, y + 40), gloss, font=f(AR, 22), fill=MUTE)
    if i < len(rows):
        d.line([(M, y + 74), (W - M, y + 74)], fill=RULE, width=1)
    y += 88
d.line([(M, y + 2), (M + 96, y + 2)], fill=ACC, width=4)
d.text((M, y + 22), "Note the order. Number one is fidelity, not beauty.",
       font=f(ARB, 23), fill=INK)
d.text((M, y + 56), "It is also the one a generator is most likely to break.",
       font=f(AR, 21), fill=MUTE)
foot(d, "One flat lay in, a full set out",
     "Send one flat lay and we run a set, detail checks included  ·  curify-ai.com")
im.save(OUT + "en-01-seven-rejection-classes.jpg", quality=92)

# ═══════════════════════════════ 02 · the 27 checks
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
head(d, "FASHION E-COMMERCE VISUAL QA  ·  v1", "27 checks.", "Earned over seven rounds.")
fid = ["neckline / collar", "cuffs", "hem & length", "gathers / drape",
       "print & placement", "fabric / texture", "colour deviation", "logo / hardware",
       "countable closures", "inner layer", "silhouette / fit"]
bx, bw = M, W - 2 * M
d.rounded_rectangle([bx, 306, bx + bw, 306 + 188], radius=14, fill=CARD, outline=RULE, width=1)
d.text((bx + 24, 326), "GARMENT FIDELITY", font=f(ARB, 22), fill=ACC)
d.text((bx + bw - 24 - int(d.textlength("11", font=f(ARB, 30))), 321), "11", font=f(ARB, 30), fill=ACC)
for k, it in enumerate(fid):
    cx = bx + 24 + (k // 4) * (bw // 3); cy = 368 + (k % 4) * 27
    d.text((cx, cy), "\u00b7  " + it, font=f(AR, 19), fill=MUTE)

trio = [("MODEL", "5", ["body proportion", "pose", "hands", "face", "hair"], INK),
        ("PHOTOGRAPHY", "5", ["lighting", "colour temperature", "angle / framing",
         "background consistency", "front / back consistency"], INK),
        ("COMMERCE", "6", ["required frames", "front and back", "SKU consistency",
         "listing-readiness", "accessory persistence", "local-edit integrity"], GOOD)]
tw3, gap3, ty3, th3 = (bw - 36) // 3, 18, 516, 236
for i, (name, n, items, col) in enumerate(trio):
    x = bx + i * (tw3 + gap3)
    d.rounded_rectangle([x, ty3, x + tw3, ty3 + th3], radius=14, fill=CARD, outline=RULE, width=1)
    d.text((x + 22, ty3 + 20), name, font=f(ARB, 21), fill=col)
    d.text((x + tw3 - 22 - int(d.textlength(n, font=f(ARB, 28))), ty3 + 16), n, font=f(ARB, 28), fill=col)
    for k, it in enumerate(items):
        d.text((x + 22, ty3 + 62 + k * 26), "\u00b7  " + it, font=f(AR, 18), fill=MUTE)

ty = ty3 + th3 + 30
for k, ln in enumerate(wrap(d, "A single frame can pass every aesthetic judgement and still fail the set.", f(ARB, 27), bw)):
    d.text((M, ty + k * 35), ln, font=f(ARB, 27), fill=INK)
ay = ty + 52
d.line([(M, ay), (M + 96, ay)], fill=ACC, width=4)
for k, ln in enumerate(["Measure by ratio, never by pixels \u00b7 never against the source photo",
                        "Count discrete details \u00b7 detail must survive zoom \u00b7 verify at delivery size"]):
    d.text((M, ay + 18 + k * 28), ln, font=f(AR, 21), fill=MUTE)
foot(d, "The checks are the product",
     "We publish the rubric. Send one flat lay and see it applied  \u00b7  curify-ai.com")
im.save(OUT + "en-02-qa-rubric-27.jpg", quality=92)

# ═══════════════════════════════ 03 · three failures
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
head(d, "WHAT SURVIVES THE MOST REVISIONS", "Three failures.", "None of them is beauty.")
blocks = [
    ("SILHOUETTE DRIFT", "The model reference imposes its own fit on a boxy product — and it moves the two dimensions a buyer actually measures."),
    ("INNER-LAYER BLEED", "An inner garment from the reference survives into the output. Nobody ordered it; it is simply still there."),
    ("COLOUR DRIFT ACROSS A SET", "Brightness may move between frames. Hue may not. This is the single most persistent class."),
]
yy = 324
for name, body in blocks:
    lines = wrap(d, body, f(AR, 24), W - 2 * M - 56)
    bh3 = 72 + len(lines) * 34 + 26
    d.rounded_rectangle([M, yy, W - M, yy + bh3], radius=14, fill=CARD, outline=RULE, width=1)
    d.text((M + 28, yy + 26), name, font=f(ARB, 26), fill=ACC)
    for k, ln in enumerate(lines):
        d.text((M + 28, yy + 72 + k * 34), ln, font=f(AR, 24), fill=INK)
    yy += bh3 + 22
for k, ln in enumerate(wrap(d, "All three are consistency failures. Each passes a single-frame review and fails the set.", f(ARB, 25), W - 2 * M)):
    d.text((M, yy + 16 + k * 33), ln, font=f(ARB, 25), fill=INK)
foot(d, "Check these before you list",
     "Ratios, not pixels. Count the details. Verify at delivery size  ·  curify-ai.com")
im.save(OUT + "en-03-three-failures.jpg", quality=92)

print("wrote 3 cards to", OUT)
