# -*- coding: utf-8 -*-
"""
Bold typography covers for the C1-C8 candidate batch.

Form copied from the two highest-performing posts in
`curify-frontend/raw/fashion-viral-09-21/` (5345 and 2507 likes): **no product image
at all** — three or four lines of very large CJK type on a soft gradient, a small
bracketed tag top-right, two or three pills along the bottom. The three posts in that
set that led with finished imagery got 356 / 83 / 45.

Palette stays ours (`#FAF8F2` ground, `#C0521E` accent) rather than copying their
yellow-to-blue; the finding is about the FORM, not their colours.

⛔ Every mark is drawn by this script. No client asset, no template crop, no brand name.

Run:  python3 make_rn_bold_covers.py
"""
from PIL import Image, ImageDraw, ImageFont

OUT = "/Users/qqwjq/curify-gallery/smm_daily/2026-09-01-ecommerce/"

W, H = 1080, 1440                      # RedNote 3:4
INK  = (26, 26, 26)
MUTE = (120, 116, 106)
ACC  = (192, 82, 30)
RULE = (214, 209, 198)

HEI  = "/System/Library/Fonts/STHeiti Medium.ttc"
HIRA = "/System/Library/Fonts/Hiragino Sans GB.ttc"

def fb(s): return ImageFont.truetype(HEI, s)
def fr(s): return ImageFont.truetype(HIRA, s)

M = 76


def gradient(top, bottom):
    """Vertical wash. Soft, low-contrast — the type has to stay the loudest thing."""
    im = Image.new("RGB", (W, H), top)
    d = ImageDraw.Draw(im)
    for y in range(H):
        t = y / (H - 1)
        d.line([(0, y), (W, y)],
               fill=tuple(round(top[i] + (bottom[i] - top[i]) * t) for i in range(3)))
    return im


def cover(fname, tag, lines, pills, sub=None,
          top=(250, 248, 242), bottom=(226, 232, 238)):
    """lines: list of (text, colour). Sized down until the longest line fits."""
    im = gradient(top, bottom)
    d = ImageDraw.Draw(im)

    # bracketed tag, top right — viral post 1 used （设计师必看）
    tf = fb(27)
    d.text((W - M - d.textlength(tag, font=tf), 86), tag, font=tf, fill=ACC)

    # top and bottom bars, as in the reference covers
    d.line([(M, 150), (W - M, 150)], fill=INK, width=6)
    d.line([(M, H - 208), (W - M, H - 208)], fill=INK, width=6)

    # largest size at which every line fits the column
    size = 132
    while size > 60:
        f = fb(size)
        if max(d.textlength(t, font=f) for t, _ in lines) <= W - 2 * M:
            break
        size -= 4
    f = fb(size)
    lh = int(size * 1.30)

    block = lh * len(lines) + (46 if sub else 0)
    y = 150 + ((H - 208) - 150 - block) // 2 - 8

    for i, (text, col) in enumerate(lines):
        d.text((M, y), text, font=f, fill=col)
        if i < len(lines) - 1:
            ry = y + lh - 14
            d.line([(M, ry), (M + int(d.textlength(text, font=f)), ry)],
                   fill=RULE, width=3)
        y += lh

    if sub:
        d.text((M, y + 6), sub, font=fr(31), fill=MUTE)

    # pills
    px, py = M, H - 176
    pf = fb(25)
    for p in pills:
        pw = int(d.textlength(p, font=pf))
        d.rounded_rectangle([px, py, px + pw + 46, py + 60], radius=30,
                            fill=(255, 255, 255), outline=RULE, width=2)
        d.text((px + 23, py + 15), p, font=pf, fill=ACC)
        px += pw + 62

    d.text((M, H - 74), "curify-ai.com", font=fr(24), fill=MUTE)
    im.save(OUT + fname, quality=94)
    print("wrote", fname, f"(type {size}px)")


COVERS = [
    ("rn-C1-五张主图.jpg", "（服装电商必看）",
     [("服装五张主图", INK), ("到底放", INK), ("哪五张？", ACC)],
     ["收藏对照用", "一张答一个问题"], None,
     (250, 248, 242), (198, 217, 233)),

    ("rn-C2-白底图.jpg", "（拍之前看）",
     [("白底图", INK), ("拍成什么样", INK), ("AI 才不会", INK), ("把领口画崩", ACC)],
     ["七个部位", "拍完就省一轮"], None,
     (250, 248, 242), (230, 216, 190)),

    ("rn-C3-提示词.jpg", "（可直接抄）",
     [("4 句提示词", INK), ("＋1 句", INK), ("关键提醒", ACC)],
     ["白底图转模特图", "收藏备用"], "衣服的属性只能来自平铺图",
     (250, 248, 242), (203, 224, 209)),

    ("rn-C4-像两次拍的.jpg", "（发之前自查）",
     [("为什么你那", INK), ("五张图", INK), ("像两次拍的", ACC)],
     ["衣服全对也会翻", "自检清单"], None,
     (250, 248, 242), (232, 209, 226)),

    ("rn-C5-放大就崩.jpg", "（买家会这么验）",
     [("放大就崩", ACC), ("买家验收", INK), ("就这一下", INK)],
     ["数扣子", "一秒钟的事"], None,
     (250, 248, 242), (213, 205, 235)),

    ("rn-C6-一个SKU几张图.jpg", "（电商美工必备）",
     [("一个 SKU", INK), ("到底要", INK), ("几张图？", ACC)],
     ["白底图", "卖点图", "场景图", "详情页"], None,
     (250, 248, 242), (238, 220, 183)),

    ("rn-C7-预览图是干净的.jpg", "（交付前必看）",
     [("预览图", INK), ("是干净的", INK), ("原图多了", INK), ("一条开衩", ACC)],
     ["不是瑕疵", "是货不对版"], None,
     (250, 248, 242), (200, 219, 224)),

    ("rn-C8-七个验收点.jpg", "（电商美工必备）",
     [("服装 AI 出图", INK), ("7 个验收点", ACC), ("买家排的序", INK)],
     ["提升审美", "收藏学习", "对照验收"], None,
     (250, 248, 242), (235, 222, 196)),
]

for args in COVERS:
    cover(*args)
print("done —", len(COVERS), "covers")
