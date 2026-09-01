from PIL import Image, ImageDraw, ImageFont

W = H = 1200
BG   = (250, 248, 242)
INK  = (26, 26, 26)
MUTE = (122, 118, 108)
ACC  = (192, 82, 30)
GOOD = (58, 106, 84)
LINE = (147, 163, 196)
CARD = (255, 255, 255)
RULE = (226, 222, 212)

def f(p, s):
    try: return ImageFont.truetype(p, s)
    except Exception: return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", s)

ARB  = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
AR   = "/System/Library/Fonts/Supplemental/Arial.ttf"
MONO = "/System/Library/Fonts/SFNSMono.ttf"

f_eyebrow = f(ARB, 24)
f_h1      = f(ARB, 58)
f_h1b     = f(AR,  58)
f_h2      = f(ARB, 34)
f_label   = f(ARB, 25)
f_body    = f(AR,  27)
f_bodyb   = f(ARB, 27)
f_small   = f(AR,  23)
f_tiny    = f(ARB, 20)
f_mono    = f(MONO, 24)

OUT = "/Users/qqwjq/curify-gallery/smm_daily/2026-09-01-fb-child-photography/"

def base(eyebrow, l1, l2):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.text((78, 74), eyebrow, font=f_eyebrow, fill=ACC)
    d.text((78, 124), l1, font=f_h1, fill=INK)
    if l2:
        d.text((78, 190), l2, font=f_h1b, fill=INK)
    return im, d

def footer(d, band_title, band_sub):
    by = H - 158
    d.rounded_rectangle([78, by, W - 78, by + 96], radius=14, fill=(26, 26, 26))
    d.text((108, by + 22), band_title, font=f_tiny, fill=(240, 198, 168))
    d.text((108, by + 52), band_sub, font=f_small, fill=(196, 192, 184))
    d.text((78, H - 42), "curify-ai.com", font=f_small, fill=MUTE)


# ---------------------------------------------------------------- card 01
im, d = base("LOCKED-SUBJECT BACKGROUND WORK",
             "Two pipelines.",
             "Only one can leave a face alone.")

def pipeline(top, tag, tagcol, steps, notes, notecol):
    h = 210 + (len(notes) - 1) * 30
    d.rounded_rectangle([78, top, W - 78, top + h], radius=14,
                        fill=CARD, outline=RULE, width=2)
    d.text((108, top + 24), tag, font=f_label, fill=tagcol)
    x = 108
    y = top + 76
    for i, st in enumerate(steps):
        w = d.textlength(st, font=f_mono) + 34
        d.rounded_rectangle([x, y, x + w, y + 46], radius=8,
                            fill=(246, 244, 237), outline=RULE, width=2)
        d.text((x + 17, y + 12), st, font=f_mono, fill=INK)
        x += w
        if i < len(steps) - 1:
            d.text((x + 8, y + 10), "\u2192", font=f_body, fill=MUTE)
            x += 40
    ny = top + 144
    for ln in notes:
        d.text((108, ny), ln, font=f_small, fill=notecol)
        ny += 30
    return top + h + 28

y = pipeline(300, "FULL-FRAME DIFFUSION", ACC,
             ["whole photo in", "model", "whole photo out"],
             ["Every pixel is perturbed by construction.",
              "The face comes back changed \u2014 even when it looks like it didn't."],
             ACC)

y = pipeline(y, "SEGMENT \u2192 GENERATE \u2192 COMPOSITE", GOOD,
             ["cut subject", "make background", "paste back"],
             ["Subject pixels are carried through untouched by definition.",
              "Not by instruction, and not by luck."],
             GOOD)

d.text((78, y + 20), "This is why \u201cdon't change the child\u201d in a prompt is not a control.",
       font=f_bodyb, fill=INK)
d.text((78, y + 60), "A prompt is a request. Compositing is a guarantee.",
       font=f_body, fill=MUTE)
d.text((78, y + 112), "Note: this is our reading of the problem, not a tested result \u2014",
       font=f_small, fill=MUTE)
d.text((78, y + 142), "we have not run this brief.", font=f_small, fill=MUTE)

footer(d, "ASK YOUR EDITOR WHICH ONE THEY RUN.",
       "It is a fair question, and the answer changes what you are buying.")
im.save(OUT + "02-two-pipelines.jpg", quality=94)


# ---------------------------------------------------------------- card 03
im, d = base("QC IN ONE MINUTE",
             "Five places to look",
             "before you send it to the parent.")

items = [
    ("1", "Eyelashes and flyaway hair",
     "Zoom to 100%. If a single hair moved, the subject was regenerated."),
    ("2", "Skin at 100%",
     "Pores should still be there. Smooth skin is the tell, not the goal."),
    ("3", "The hair–background edge",
     "Look for a halo, a hard cut, or hair that ends too cleanly."),
    ("4", "Fabric weave and print",
     "Knit texture and any pattern on the clothing must be pixel-identical."),
    ("5", "The catchlight in the eyes",
     "On a small face this is the fastest tell \u2014 a regenerated eye moves it."),
]
y = 306
for num, title, sub in items:
    d.rounded_rectangle([78, y, W - 78, y + 118], radius=14,
                        fill=CARD, outline=RULE, width=2)
    d.ellipse([106, y + 35, 106 + 48, y + 83], fill=(246, 240, 232))
    tw = d.textlength(num, font=f_label)
    d.text((106 + 24 - tw / 2, y + 48), num, font=f_label, fill=ACC)
    d.text((178, y + 28), title, font=f_h2, fill=INK)
    d.text((178, y + 72), sub, font=f_small, fill=MUTE)
    y += 130

footer(d, "COMPARE AGAINST THE ORIGINAL FILE, NOT THE PREVIEW.",
       "A compressed preview hides exactly the detail you are checking for.")
im.save(OUT + "04-five-places-to-look.jpg", quality=94)


# ---------------------------------------------------------------- card 04
im, d = base("BEFORE YOU QUOTE A VOLUME JOB",
             "Read the pictures first.",
             "Use the words to check them.")

d.rounded_rectangle([78, 300, W - 78, 470], radius=14, fill=CARD,
                    outline=RULE, width=2)
d.text((108, 326), "WHY", font=f_label, fill=ACC)
for i, ln in enumerate([
        "A brief we read carried a 37-line written spec and two reference",
        "image pairs. Identical child, identical pose, identical crop, different",
        "background. One glance fixed a constraint the prose spent a paragraph on."]):
    d.text((108, 372 + i * 32), ln, font=f_body, fill=INK)

d.rounded_rectangle([78, 496, W - 78, 884], radius=14, fill=CARD,
                    outline=RULE, width=2)
d.text((108, 522), "THEN CHECK THE WORDS FOR THESE TWO THINGS", font=f_label, fill=ACC)

blocks = [
    ("Contradictions.", [
        "That same brief banned any overlay of the arms and hands in one",
        "section, and appeared to allow props to occlude the limbs in another —",
        "in a sentence missing its verb. Props behind the child or crossing in",
        "front is a visible decision on every single frame."]),
    ("Deliverables the template does not cover.", [
        "It named three framings — full body, half body, close-up — and supplied",
        "one template. The close-up crop excludes nearly every element that",
        "template describes. Find the uncovered variant before agreeing a count."]),
]
y = 570
for title, lines in blocks:
    d.text((108, y), title, font=f_bodyb, fill=INK)
    y += 34
    for ln in lines:
        d.text((108, y), ln, font=f_small, fill=MUTE)
        y += 28
    y += 12

footer(d, "FIND THE GAP BEFORE YOU AGREE THE PRICE.",
       "Afterwards it is a change request you already sold at the old rate.")
im.save(OUT + "05-read-the-pictures-first.jpg", quality=94)


# ---------------------------------------------------------------- card 05
im = Image.new("RGB", (W, H), (26, 26, 26))
d = ImageDraw.Draw(im)
d.text((78, 108), "OUR RULE", font=f_eyebrow, fill=(240, 198, 168))
for i, ln in enumerate(["We do not publish", "photographs of children.", "Anyone's."]):
    d.text((78, 168 + i * 76), ln, font=f_h1, fill=(250, 248, 242))

d.line([(78, 424), (330, 424)], fill=(192, 82, 30), width=4)

lines = [
    ("Not our clients'.", "Consent for a shoot is not consent for a portfolio."),
    ("Not our own.", "A studio's marketing feed is not where a child's face belongs."),
    ("Not generated ones.", "A synthetic child is still a child-shaped image, posted"),
    ("", "into a group full of parents. We are not doing that either."),
]
y = 476
for a, b in lines:
    if a:
        d.text((78, y), a, font=f_bodyb, fill=(250, 248, 242))
        d.text((78 + d.textlength(a, font=f_bodyb) + 14, y), b, font=f_body,
               fill=(178, 174, 166))
    else:
        d.text((78, y), b, font=f_body, fill=(178, 174, 166))
    y += 46

d.rounded_rectangle([78, 726, W - 78, 906], radius=14, fill=(38, 38, 38))
d.text((108, 754), "SO WHAT DO WE SHOW?", font=f_label, fill=(240, 198, 168))
for i, ln in enumerate([
        "The method. Diagrams, checklists, and the two or three things that",
        "actually go wrong — which is the part worth reading anyway. A",
        "before-and-after proves one edit. A checklist travels."]):
    d.text((108, 800 + i * 34), ln, font=f_body, fill=(214, 210, 202))

d.text((78, 962), "If an editor's portfolio is full of other people's children,",
       font=f_small, fill=(178, 174, 166))
d.text((78, 992), "ask them who signed off on that.", font=f_small, fill=(178, 174, 166))
d.text((78, H - 42), "curify-ai.com", font=f_small, fill=(122, 118, 108))
im.save(OUT + "06-we-do-not-publish-children.jpg", quality=94)

print("done")
