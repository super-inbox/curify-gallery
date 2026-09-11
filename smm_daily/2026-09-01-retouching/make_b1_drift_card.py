from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC = "/Users/qqwjq/curify-studio/dev/jayw/video_pipelines/ecommerce_to_video/products/gen/"
OUT = "/Users/qqwjq/curify-gallery/smm_daily/2026-09-01-retouching/"

W, H = 1200, 1650
BG   = (250, 248, 242)
INK  = (26, 26, 26)
MUTE = (122, 118, 108)
ACC  = (192, 82, 30)
GOOD = (58, 106, 84)
RULE = (226, 222, 212)

def f(p, s):
    try: return ImageFont.truetype(p, s)
    except Exception: return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", s)

ARB = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
AR  = "/System/Library/Fonts/Supplemental/Arial.ttf"

f_eyebrow = f(ARB, 24); f_h1 = f(ARB, 58); f_label = f(ARB, 24)
f_bodyb = f(ARB, 26); f_small = f(AR, 22); f_tiny = f(ARB, 20)

im = Image.new("RGB", (W, H), BG)
d  = ImageDraw.Draw(im)
M  = 78

d.text((M, 66),  "ONE PRODUCT. ONE PIPELINE. TWO RUNS.", font=f_eyebrow, fill=ACC)
d.text((M, 116), "Look at what moved.", font=f_h1, fill=INK)

PW, PH = 484, 500
GAP = 32
x0, x1 = M, M + PW + GAP

def contain(img, pw, ph, ground):
    s = min(pw / img.width, ph / img.height)
    im2 = img.resize((max(1, int(img.width * s)), max(1, int(img.height * s))), Image.LANCZOS)
    panel = Image.new("RGB", (pw, ph), ground)
    panel.paste(im2, ((pw - im2.width) // 2, (ph - im2.height) // 2))
    return panel

# ---------------------------------------------------------------- row 1
r1 = 246
d.text((M, r1 - 36), "GENERATED SEPARATELY  —  the subject drifted", font=f_label, fill=ACC)

shelf  = Image.open(SRC + "serum_scene_shelf.jpg").crop((424, 296, 616, 776))
vanity = Image.open(SRC + "serum_scene_vanity.jpg").crop((414, 224, 622, 782))

for x, crop, tag in ((x0, shelf, "run 1"), (x1, vanity, "run 2")):
    im.paste(contain(crop, PW, PH, (240, 237, 229)), (x, r1))
    d.rectangle([x, r1, x + PW, r1 + PH], outline=RULE, width=2)
    d.rounded_rectangle([x + 14, r1 + 14, x + 112, r1 + 52], radius=8, fill=(26, 26, 26))
    d.text((x + 34, r1 + 22), tag, font=f_tiny, fill=(250, 248, 242))

cy = r1 + PH + 22
for i, (a, b) in enumerate([
        ("Pump collar", "one smooth sleeve  vs.  a stepped collar with a ring"),
        ("Label", "opaque white, hard edge  vs.  translucent grey"),
        ("Shoulder", "narrow and square  vs.  wider and rounded")]):
    d.text((M, cy + i * 34), "•", font=f_bodyb, fill=ACC)
    d.text((M + 26, cy + i * 34), a, font=f_bodyb, fill=INK)
    d.text((M + 26 + d.textlength(a, font=f_bodyb) + 14, cy + i * 34), b,
           font=f_small, fill=MUTE)

# ---------------------------------------------------------------- row 2
r2 = 906
d.text((M, r2 - 36), "COMPOSITED  —  one cutout, two backdrops", font=f_label, fill=GOOD)

cut = Image.open(SRC + "serum.png").convert("RGBA")
ch  = 392
cut = cut.resize((max(1, int(cut.width * ch / cut.height)), ch), Image.LANCZOS)

def sweep(top, mid, bot):
    """A studio paper sweep: vertical gradient with a soft floor line."""
    g = Image.new("RGB", (PW, PH))
    dr = ImageDraw.Draw(g)
    split = int(PH * 0.68)
    for y in range(PH):
        if y < split:
            t = y / split
            c = tuple(int(top[i] + (mid[i] - top[i]) * t) for i in range(3))
        else:
            t = (y - split) / (PH - split)
            c = tuple(int(mid[i] + (bot[i] - mid[i]) * t) for i in range(3))
        dr.line([(0, y), (PW, y)], fill=c)
    return g.filter(ImageFilter.GaussianBlur(1.2))

grounds = [
    ("backdrop A", sweep((38, 52, 84), (92, 108, 138), (232, 232, 236))),
    ("backdrop B", sweep((214, 206, 194), (232, 226, 216), (245, 242, 236))),
]

for x, (tag, ground) in zip((x0, x1), grounds):
    panel = ground.convert("RGBA")
    px = (PW - cut.width) // 2
    py = PH - ch - 46
    # contact shadow so it sits rather than floats
    sh = Image.new("RGBA", (PW, PH), (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse(
        [px - 18, py + ch - 22, px + cut.width + 18, py + ch + 26], fill=(0, 0, 0, 78))
    panel.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
    panel.alpha_composite(cut, (px, py))
    im.paste(panel.convert("RGB"), (x, r2))
    d.rectangle([x, r2, x + PW, r2 + PH], outline=RULE, width=2)
    tw = int(d.textlength(tag, font=f_tiny))
    d.rounded_rectangle([x + 14, r2 + 14, x + 42 + tw, r2 + 52], radius=8, fill=(58, 106, 84))
    d.text((x + 28, r2 + 22), tag, font=f_tiny, fill=(250, 248, 242))

d.text((M, r2 + PH + 24),
       "Byte-identical — not because it was asked for, but because it never entered the model.",
       font=f_bodyb, fill=GOOD)

# ---------------------------------------------------------------- footer
by = H - 158
d.rounded_rectangle([M, by, W - M, by + 96], radius=14, fill=(26, 26, 26))
d.text((M + 28, by + 22), "ON A BOTTLE THIS IS A LABEL REDRAW. ON A FACE IT IS SOMEONE ELSE'S CHILD.",
       font=f_tiny, fill=(240, 198, 168))
d.text((M + 28, by + 52),
       "Both runs are our own output. We are not demonstrating this on a child — see the pinned post.",
       font=f_small, fill=(196, 192, 184))
d.text((M, H - 42), "curify-ai.com", font=f_small, fill=MUTE)

im.save(OUT + "b1-look-at-what-moved.jpg", quality=94)
print("saved", im.size)
