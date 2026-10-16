"""Voice R (real estate / property media) cards — 1200×1200, FB feed.

These are diagram cards, not before/afters, and that is deliberate.

We have **no real-estate before/after we are entitled to show**: per
`curify-studio/docs/reddit-demand-mining-retouching-2026-09-15.md` §F1 we have never
quoted, delivered or been paid for a real-estate edit. The two template sets that look
like candidates are worse than nothing:

  · `template-home-organization-before-after-*` — the "after" is a DIFFERENT staged
    scene with product callouts, not the same frame edited. That is precisely the
    failure the buyer complains about in the lane's top thread ("aren't the photos
    being completely recreated... you zoom in and you can tell it's just slop").
    Posting it would demonstrate the objection, not the answer.
  · `template-interior-design-mood-board-generator-*` — a design deliverable
    (render + material palette), not an edit of anyone's property photo.

So the R posts argue the *method*, which is what this buyer is actually shopping for,
and the honest claim we can make is about our own pipeline rather than about a
delivered listing. Palette matches make_c_cards.py.

    python3 make_r_cards.py
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1200
BG, INK, MUTE = (250, 248, 242), (26, 26, 26), (122, 118, 108)
ACC, GOOD, CARD, RULE = (192, 82, 30), (58, 106, 84), (255, 255, 255), (226, 222, 212)
OUT = "/Users/qqwjq/curify-gallery/smm_daily/2026-09-01-retouching/"
M = 84


def f(p, s):
    try:
        return ImageFont.truetype(p, s)
    except Exception:
        return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", s)


ARB = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
AR = "/System/Library/Fonts/Supplemental/Arial.ttf"
MONO = "/System/Library/Fonts/SFNSMono.ttf"


def head(d, eyebrow, l1, l2=None, accent2=False):
    d.text((M, 78), eyebrow, font=f(ARB, 24), fill=ACC)
    d.text((M, 122), l1, font=f(ARB, 56), fill=INK)
    if l2:
        d.text((M, 190), l2, font=f(ARB, 56), fill=ACC if accent2 else INK)


def foot(d, line1, line2):
    by = H - 172
    d.rounded_rectangle([M, by, W - M, by + 108], radius=16, fill=(26, 26, 26))
    d.text((M + 28, by + 24), line1, font=f(ARB, 26), fill=(240, 198, 168))
    d.text((M + 28, by + 62), line2, font=f(AR, 22), fill=(196, 192, 184))
    d.text((M, H - 48), "curify-ai.com", font=f(AR, 21), fill=MUTE)


def wrap(d, text, font, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


# ══════════════════════════ R1 — edit it, don't recreate it ══════════════════
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
head(d, "THE QUESTION AGENTS ARE ASKING", "Edit the photo.", "Don't recreate it.", True)

y = 300
for tag, col, steps, note in [
    ("REGENERATE", ACC, ["whole frame in", "whole frame out"],
     "Every pixel is rewritten. The worktop, the window frame, the floor grain —\nall re-drawn. Zoom in and it reads as slop."),
    ("EDIT IN PLACE", GOOD, ["mask the object", "fill only that", "rest untouched"],
     "The pixels you did not point at never enter the model.\nNot a promise in a prompt — a property of the method."),
]:
    d.rounded_rectangle([M, y, W - M, y + 230], radius=16, fill=CARD, outline=RULE, width=2)
    d.text((M + 28, y + 24), tag, font=f(ARB, 26), fill=col)
    x, yy = M + 28, y + 76
    for i, s in enumerate(steps):
        wdt = d.textlength(s, font=f(AR, 23)) + 30
        d.rounded_rectangle([x, yy, x + wdt, yy + 46], radius=8,
                            fill=(246, 244, 237), outline=RULE, width=2)
        d.text((x + 15, yy + 11), s, font=f(AR, 23), fill=INK)
        x += wdt
        if i < len(steps) - 1:
            d.text((x + 8, yy + 9), "→", font=f(AR, 24), fill=MUTE); x += 40
    for i, ln in enumerate(note.split("\n")):
        d.text((M + 28, y + 148 + i * 32), ln, font=f(AR, 22), fill=MUTE)
    y += 258

d.text((M, y + 6), "We tested whole-frame regeneration and abandoned it.",
       font=f(ARB, 27), fill=INK)
d.text((M, y + 42), "Detail correlation against the input measured 0.007.",
       font=f(MONO, 24), fill=ACC)

foot(d, "Nothing moves but what you asked for.",
     "Send one frame and the thing you want gone — I'll send it back and you zoom in.")
im.save(OUT + "r1-edit-not-recreate.jpg", quality=94)

# ══════════════════════════ R2 — item removal, checkable ═════════════════════
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
head(d, "ITEM REMOVAL · THE MOST-ASKED JOB IN THE LANE", "How to check it", "in ten seconds.", True)

items = [
    ("Open the original and the edit at 100%", "Not the MLS preview. Compression hides exactly what you are checking for."),
    ("Look at the edge where the object was", "A fill that guessed leaves a soft smear. A fill that copied leaves grain."),
    ("Check the floor and worktop pattern", "Tile grout and wood grain must continue. A repeat means the model invented it."),
    ("Check one thing you did NOT ask about", "The window frame, a switch plate, the skirting. If that moved, the whole frame was rewritten."),
]
y = 316
for i, (t, sub) in enumerate(items):
    d.rounded_rectangle([M, y, W - M, y + 128], radius=14, fill=CARD, outline=RULE, width=2)
    d.ellipse([M + 26, y + 50, M + 44, y + 68], fill=ACC)
    d.text((M + 64, y + 26), t, font=f(ARB, 28), fill=INK)
    for j, ln in enumerate(wrap(d, sub, f(AR, 22), W - 2 * M - 100)):
        d.text((M + 64, y + 68 + j * 28), ln, font=f(AR, 22), fill=MUTE)
    y += 146

foot(d, "The fourth one is the real test.",
     "Anything that changed without being asked to means the room was regenerated.")
im.save(OUT + "r2-item-removal-check.jpg", quality=94)

# ══════════════════════════ R3 — interior colour ═════════════════════════════
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
head(d, "INTERIOR COLOUR", "Not overly HDR.", "Keep some warmth.", True)

d.text((M, 292), "The brief nobody writes down, and every agent notices.",
       font=f(AR, 27), fill=MUTE)

sw = [((238, 228, 210), "as shot", "mixed light, windows blown"),
      ((246, 240, 228), "window pull", "exterior recovered, interior warm"),
      ((228, 234, 238), "over-processed", "grey, flat, every shadow lifted")]
y, bw = 360, (W - 2 * M - 48) // 3
for i, (c, lab, sub) in enumerate(sw):
    x = M + i * (bw + 24)
    d.rounded_rectangle([x, y, x + bw, y + 172], radius=14, fill=c,
                        outline=ACC if i == 2 else RULE, width=3 if i == 2 else 2)
    d.text((x + 16, y + 186), lab, font=f(ARB, 25), fill=ACC if i == 2 else INK)
    for j, ln in enumerate(wrap(d, sub, f(AR, 20), bw - 10)):
        d.text((x + 16, y + 218 + j * 26), ln, font=f(AR, 20), fill=MUTE)

y = 660
d.line([(M, y), (W - M, y)], fill=RULE, width=2)
for i, (t, sub) in enumerate([
    ("Consistency beats any single frame", "Thirty photos of one property must read as one afternoon, one white balance, one sky."),
    ("The look is briefed by reference, not by parameter", "Send the gallery whose colour you want matched — that is a look-lock job, and it is checkable."),
]):
    yy = y + 34 + i * 116
    d.text((M, yy), t, font=f(ARB, 28), fill=INK)
    for j, ln in enumerate(wrap(d, sub, f(AR, 22), W - 2 * M)):
        d.text((M, yy + 40 + j * 28), ln, font=f(AR, 22), fill=MUTE)

foot(d, "Send three frames and the gallery you want to match.",
     "I'll grade them to it and send them back, so you can put them side by side.")
im.save(OUT + "r3-interior-colour.jpg", quality=94)

print("done — r1, r2, r3")
