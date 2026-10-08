"""Women's shoe restoration sheet → an English FB version and a Chinese RedNote version.

The master, womens-shoe-restoration-contact-sheet.png, is an AI-generated demo
(see womens-shoe-generation-prompt.txt) with its Chinese text baked in by the
image model. Regenerating it would produce different shoes, so this script keeps
all twelve photographs pixel-for-pixel and only re-typesets the text:

  - the title, subtitle, six captions and footer are painted out with the paper
    colour (flat RGB 251,249,246, measured) and redrawn;
  - each 修复前 / 修复后 tag is covered by a black label pill;
  - the footer keeps the disclosure: AI-generated demo, not client work.

Redrawing the Chinese too means no model-drawn glyph survives in either version.

Usage:  python make_shoe_sheets.py
Writes: womens-shoe-restoration-en.jpg (FB) and womens-shoe-restoration-zh.jpg (RedNote)
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC = HERE / "womens-shoe-restoration-contact-sheet.png"
BG = (251, 249, 246)
INK = (24, 24, 24)
GREY = (110, 110, 110)
RULE = (185, 180, 172)

HEI = "/System/Library/Fonts/STHeiti Medium.ttc"
HIRA = "/System/Library/Fonts/Hiragino Sans GB.ttc"
TIMES = "/System/Library/Fonts/Times.ttc"

# Measured on the 1086×1448 master.
ROWS = [170, 553, 945]                    # photo tops
BEFORE_X = [30, 566]                      # left / right card, "before" photo left edge
AFTER_X = [279, 812]                      # left / right card, "after" photo left edge
CARD_CX = [275, 810]                      # caption centre per card
CAPTION_Y = [500, 893, 1291]              # caption centre per row
CAPTION_FILL = [(478, 523), (871, 916), (1268, 1314)]

COPY = {
    "en": {
        "title": "Women's Shoe Photo Restoration",
        "subtitle": "Detail repair  ·  Colour correction  ·  E-commerce finishing",
        "before": "Before", "after": "After",
        "captions": [
            "01  Black stiletto  |  Light & shadow",
            "02  Satin bridal pump  |  Texture restored",
            "03  Red Mary Jane  |  Colour correction",
            "04  Suede ankle boot  |  Detail repair",
            "05  Gold sandal  |  Background cleanup",
            "06  Ballet flat  |  Sharper detail",
        ],
        "footer": "AI-generated demo examples · not real client work · curify-ai.com",
        "fonts": {"title": (TIMES, 1, 60), "sub": (TIMES, 0, 28), "cap": (TIMES, 1, 25),
                  "label": (HIRA, 0, 21), "foot": (HIRA, 0, 17)},
        "out": "womens-shoe-restoration-en.jpg",
    },
    "zh": {
        "title": "女鞋照片修复",
        "subtitle": "细节修复  ·  色彩校正  ·  电商精修",
        "before": "修复前", "after": "修复后",
        "captions": [
            "01  黑色高跟鞋  |  光影修复",
            "02  缎面婚鞋  |  质感还原",
            "03  红色玛丽珍  |  色彩校正",
            "04  麂皮短靴  |  细节修复",
            "05  金色凉鞋  |  背景净化",
            "06  芭蕾平底鞋  |  清晰增强",
        ],
        "footer": "AI 生成演示案例 · 非真实客户项目 · curify-ai.com",
        "fonts": {"title": (HEI, 0, 72), "sub": (HIRA, 0, 30), "cap": (HEI, 0, 27),
                  "label": (HIRA, 0, 21), "foot": (HIRA, 0, 18)},
        "out": "womens-shoe-restoration-zh.jpg",
    },
}


def font(spec):
    path, index, size = spec
    return ImageFont.truetype(path, size, index=index)


def centred(d, cx, cy, text, f, fill):
    l, t, r, b = d.textbbox((0, 0), text, font=f)
    d.text((cx - (r - l) / 2 - l, cy - (b - t) / 2 - t), text, font=f, fill=fill)
    return (r - l)


def ruled(d, cy, text, f, fill, margin=26, gap=22, width=1086):
    w = centred(d, width / 2, cy, text, f, fill)
    left_end, right_start = width / 2 - w / 2 - gap, width / 2 + w / 2 + gap
    d.line((margin, cy, left_end, cy), fill=RULE, width=2)
    d.line((right_start, cy, width - margin, cy), fill=RULE, width=2)


def build(lang):
    c = COPY[lang]
    im = Image.open(SRC).convert("RGB")
    d = ImageDraw.Draw(im)
    W, H = im.size
    f = {k: font(v) for k, v in c["fonts"].items()}

    # 1. Paint out every baked-in line of text.
    d.rectangle((0, 0, W, 152), fill=BG)
    for (y0, y1) in CAPTION_FILL:
        d.rectangle((44, y0, 512, y1), fill=BG)
        d.rectangle((578, y0, 1046, y1), fill=BG)
    d.rectangle((0, 1358, W, 1410), fill=BG)

    # 2. Title, ruled subtitle, captions, ruled footer.
    centred(d, W / 2, 58, c["title"], f["title"], INK)
    ruled(d, 124, c["subtitle"], f["sub"], INK)
    for i, cap in enumerate(c["captions"]):
        row, col = divmod(i, 2)
        centred(d, CARD_CX[col], CAPTION_Y[row], cap, f["cap"], INK)
    ruled(d, 1384, c["footer"], f["foot"], GREY)

    # 3. Label pills over the 修复前 / 修复后 tags (tag sits ~+13..+66, +11..+28).
    for top in ROWS:
        for xs, label in ((BEFORE_X, c["before"]), (AFTER_X, c["after"])):
            for x in xs:
                l, t, r, b = d.textbbox((0, 0), label, font=f["label"])
                w = max(r - l + 26, 74)
                box = (x + 8, top + 6, x + 8 + w, top + 40)
                d.rounded_rectangle(box, 10, fill=(26, 26, 26))
                centred(d, (box[0] + box[2]) / 2, (box[1] + box[3]) / 2, label, f["label"], (255, 255, 255))

    out = HERE / c["out"]
    im.save(out, quality=90)
    print(out.name, im.size)


if __name__ == "__main__":
    for lang in ("en", "zh"):
        build(lang)
