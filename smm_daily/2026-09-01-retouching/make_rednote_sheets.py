"""Re-lay the wide demo contact sheets into 小红书 3:4 (1080×1440).

The sheets in `demos/*/` are built for a Facebook feed: one row of five panels,
2.9:1 or wider. 小红书 renders 3:4, so a 2.9:1 strip arrives as a sliver with the
faces too small to read — which is the whole content of these images.

Same five frames, re-laid vertically: the source frame across the top (it is the
thing everything else is held against), then the four backdrops 2×2 underneath.

    python3 make_rednote_sheets.py

Writes `rn-W2-kyoto.jpg`, `rn-W3-dubai.jpg`, `rn-P2-portrait.jpg` into this folder.
`retouch-children-demo-09-10` is deliberately NOT built — see "没有 C7" in
posts_fb.md; that sheet contains a synthetic child and never goes to a feed.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

HERE = Path(__file__).parent
W, H = 1080, 1440
GROUND, INK, ACCENT, MUTED = (250, 248, 242), (26, 26, 26), (192, 82, 30), (122, 118, 110)
PAD, GAP = 36, 12


def font(sz, bold=False):
    for p in ("/System/Library/Fonts/STHeiti Medium.ttc" if bold else
              "/System/Library/Fonts/Hiragino Sans GB.ttc",
              "/System/Library/Fonts/STHeiti Light.ttc",
              "/Library/Fonts/Arial Unicode.ttf"):
        try:
            return ImageFont.truetype(p, sz)
        except Exception:
            continue
    return ImageFont.load_default()


def cover(im, bw, bh, anchor=0.0):
    """Crop-to-fill. `anchor` slides the crop down as a fraction of the slack,
    so a wide band off a 3:4 portrait can sit on the face instead of the hairline."""
    s = max(bw / im.width, bh / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = (im.width - bw) // 2
    y = round((im.height - bh) * anchor)
    return im.crop((x, y, x + bw, y + bh))


def label(d, box, text, sub=None):
    x, y, w, h = box
    bar = 34 if not sub else 52
    d.rectangle([x, y + h - bar, x + w, y + h], fill=(0, 0, 0, 255))
    d.text((x + 10, y + h - bar + 7), text, font=font(20, True), fill=(255, 255, 255))
    if sub:
        d.text((x + 10, y + h - bar + 30), sub, font=font(15), fill=(205, 200, 190))


def build(folder, out, title, subtitle, panels):
    src = HERE / "demos" / folder
    im = Image.new("RGB", (W, H), GROUND)
    d = ImageDraw.Draw(im)

    d.text((PAD, 30), title, font=font(46, True), fill=INK)
    d.text((PAD, 92), subtitle, font=font(22), fill=MUTED)
    d.line([(PAD, 128), (PAD + 86, 128)], fill=ACCENT, width=4)

    top_y, top_h = 152, 430
    bw = W - 2 * PAD
    hero = cover(Image.open(src / panels[0][0]), bw, top_h, anchor=0.16)
    im.paste(hero, (PAD, top_y))
    d.rectangle([PAD, top_y, PAD + bw, top_y + top_h], outline=ACCENT, width=3)
    label(d, (PAD, top_y, bw, top_h), panels[0][1], panels[0][2])

    cw = (bw - GAP) // 2
    ch = 392
    gy = top_y + top_h + GAP
    for i, (fn, lab, sub) in enumerate(panels[1:5]):
        gx = PAD + (i % 2) * (cw + GAP)
        yy = gy + (i // 2) * (ch + GAP)
        im.paste(cover(Image.open(src / fn), cw, ch), (gx, yy))
        label(d, (gx, yy, cw, ch), lab, sub)

    fy = gy + 2 * ch + GAP + 14
    d.text((PAD, fy), "AI 生成的修图概念图 · 非客片", font=font(19), fill=MUTED)
    d.text((W - PAD - 118, fy), "curify-ai.com", font=font(19), fill=MUTED)
    im.save(HERE / out, quality=93)
    print("  ✓", out, im.size)


build("retouch-kyoto-demo-09-10", "rn-W2-kyoto.jpg",
      "人物锁死，只换背景", "同一个人 · 同一身和服 · 同一个姿势 —— 只有背景在变",
      [("00-source.png", "原片 · AS SHOT", "棚内，光平"),
       ("01-clean.png", "净底", None), ("02-machiya.png", "町家小巷", None),
       ("03-maple.png", "红叶", None), ("04-bamboo.png", "竹林", None)])

build("retouch-dubai-demo-09-10", "rn-W3-dubai.jpg",
      "一张原片，四个外景", "同一个人 · 同一件长袍 · 同一个姿势 —— 背景是生成的，人不是",
      [("00-source.png", "原片 · AS SHOT", "棚内"),
       ("01-clean.png", "净底", None), ("02-dune.png", "沙丘", None),
       ("03-oldtown.png", "老城", None), ("04-skyline.png", "天际线 · 蓝调", None)])

build("retouch-portrait-demo-09-10", "rn-P2-portrait.jpg",
      "拍一次，四个场景都能交", "同一个人 · 同一套西装 · 同一个姿势 —— 只换背景",
      [("00-source.png", "原片 · AS SHOT", "棚内"),
       ("01-white.png", "白底 · 官网", None), ("02-editorial.png", "水泥墙 · 杂志感", None),
       ("03-street.png", "街拍 · 黄昏", None), ("04-interior.png", "室内 · 自然光", None)])
