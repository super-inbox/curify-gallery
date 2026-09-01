from PIL import Image, ImageDraw, ImageFont

W = H = 1200
BG   = (250, 248, 242)
INK  = (26, 26, 26)
MUTE = (122, 118, 108)
ACC  = (192, 82, 30)
LINE = (147, 163, 196)
CARD = (255, 255, 255)

def f(p, s):
    try: return ImageFont.truetype(p, s)
    except Exception: return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", s)

ARB = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
AR  = "/System/Library/Fonts/Supplemental/Arial.ttf"
MONO= "/System/Library/Fonts/SFNSMono.ttf"

f_eyebrow=f(ARB,24); f_h1=f(ARB,62); f_h1b=f(AR,62)
f_label=f(ARB,25);   f_body=f(AR,27); f_small=f(AR,23)
f_tiny=f(ARB,20);    f_mono=f(MONO,28); f_monos=f(MONO,22)

im = Image.new("RGB",(W,H),BG); d = ImageDraw.Draw(im)
M = 78

d.text((M,74), "GHOST MANNEQUIN  ·  QC IN UNDER A MINUTE", font=f_eyebrow, fill=ACC)
d.text((M,126), "Two ratios.", font=f_h1, fill=INK)
d.text((M,196), "Neither is a pixel comparison.", font=f_h1b, fill=INK)

# ---- left: schematic figure -------------------------------------------------
fx = M + 62
fw = 246
sh_y, bust_y, hem_y, hip_y = 372, 512, 800, 940
cx = fx + fw/2

# body (behind the garment) — visible between hem_y and hip_y
d.polygon([(fx+30, sh_y+10),(fx+fw-30, sh_y+10),
           (fx+fw-34, hip_y+46),(fx+34, hip_y+46)],
          fill=(232,228,218), outline=(206,201,188), width=2)

# garment body: boxy, straight through the waist
d.polygon([(fx+34, sh_y+4),(fx+fw-34, sh_y+4),
           (fx+fw-16, sh_y+40),(fx+fw-8, bust_y),
           (fx+fw-4, hem_y),(fx+4, hem_y),
           (fx+8, bust_y),(fx+16, sh_y+40)],
          fill=(238,235,226), outline=(184,179,165), width=2)

# short sleeves
d.polygon([(fx+34, sh_y+6),(fx+16, sh_y+40),(fx-26, bust_y+34),
           (fx+16, bust_y+52),(fx+40, bust_y-6)],
          fill=(232,229,219), outline=(184,179,165), width=2)
d.polygon([(fx+fw-34, sh_y+6),(fx+fw-16, sh_y+40),(fx+fw+26, bust_y+34),
           (fx+fw-16, bust_y+52),(fx+fw-40, bust_y-6)],
          fill=(232,229,219), outline=(184,179,165), width=2)

# neck opening sitting ON the shoulder line
d.chord([cx-32, sh_y-10, cx+32, sh_y+34], 0, 180,
        fill=(246,244,237), outline=(184,179,165), width=2)
d.line([(cx-32, sh_y+11),(cx+32, sh_y+11)], fill=(184,179,165), width=2)

# centre placket
d.line([(cx, sh_y+14),(cx, hem_y-6)], fill=(206,201,188), width=2)

def landmark(yy, label, x0, x1):
    x = x0
    while x < x1:
        d.line([(x,yy),(min(x+11,x1),yy)], fill=LINE, width=2); x += 20
    d.text((x1+16, yy-14), label, font=f_monos, fill=MUTE)

for yy, lab in ((sh_y,"shoulder_y"),(bust_y,"bust"),(hem_y,"hem_y"),(hip_y,"hip_y")):
    landmark(yy, lab, fx-56, fx+fw+30)

# garment width callout at bust
wy = bust_y + 66
d.line([(fx+10, wy),(fx+fw-10, wy)], fill=ACC, width=3)
for xx in (fx+10, fx+fw-10):
    d.line([(xx, wy-9),(xx, wy+9)], fill=ACC, width=3)
d.text((fx+14, wy+14), "garment width", font=f_monos, fill=ACC)

# ---- right: the two formulas ------------------------------------------------
rx = 596; cw = W - rx - M

def card(top, tag, num, den):
    h = 182
    d.rounded_rectangle([rx,top,rx+cw,top+h], radius=14, fill=CARD,
                        outline=(226,222,212), width=2)
    d.text((rx+30, top+26), tag, font=f_label, fill=ACC)
    d.text((rx+30, top+74), num, font=f_mono, fill=INK)
    d.line([(rx+30, top+116),(rx+cw-40, top+116)], fill=(212,208,196), width=2)
    d.text((rx+30, top+128), den, font=f_mono, fill=INK)
    return top + h + 28

ny = card(344, "LENGTH",        "hem_y − shoulder_y", "hip_y − shoulder_y")
ny = card(ny,  "WIDTH AT BUST", "garment_width",      "body_width")

d.text((rx+2, ny+10), "Ratios survive crop and", font=f_body, fill=INK)
d.text((rx+2, ny+44), "camera distance.", font=f_body, fill=INK)
d.text((rx+2, ny+82), "Absolute pixel measurements", font=f_body, fill=MUTE)
d.text((rx+2, ny+116), "do not.", font=f_body, fill=MUTE)

# ---- bottom rule band -------------------------------------------------------
by = H - 158
d.rounded_rectangle([M, by, W-M, by+96], radius=14, fill=(26,26,26))
d.text((M+30, by+22), "DO NOT MEASURE THE OUTPUT AGAINST YOUR SOURCE PHOTO.",
       font=f_tiny, fill=(240,198,168))
d.text((M+30, by+52),
       "No shared landmark, no shared scale, no shared pose. Compare to your size chart in cm.",
       font=f_small, fill=(196,192,184))
d.text((M, H-42), "curify-ai.com  ·  /blog/ghost-mannequin-ai-guide", font=f_small, fill=MUTE)

out="/Users/qqwjq/curify-gallery/smm_daily/2026-09-01-fb-retouching-ecommerce/04-two-ratio-check.jpg"
im.save(out, quality=94); print("saved", im.size)
