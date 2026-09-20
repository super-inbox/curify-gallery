# -*- coding: utf-8 -*-
"""
Two 3:4 RedNote cards for the 服装干货 posts in posts_rednote_kuaishou.md.

  rn-服装1-七类翻车.jpg   — the buyer's own seven rejection classes, as a checklist card
  rn-服装2-五个机位.jpg   — one reference x5 is not a set; the five shots answer five questions

Palette and typography follow the house cards:
`../2026-09-01-retouching/make_rednote_cards.py` and `make_a4_ratio_card.py`.

⛔ Nothing here is traced from, cropped from or derived from any client or lead asset.
Every mark is drawn by this script. The seven classes are a paraphrase of a rejection
taxonomy; no brand name, style number or filename from any source record appears.
"""
from PIL import Image, ImageDraw, ImageFont

OUT = "/Users/qqwjq/curify-gallery/smm_daily/2026-09-01-ecommerce/"

W, H = 1080, 1440                      # RedNote 3:4
BG   = (250, 248, 242)
INK  = (26, 26, 26)
MUTE = (120, 116, 106)
ACC  = (192, 82, 30)
GOOD = (58, 106, 84)
CARD = (255, 255, 255)
RULE = (226, 222, 212)
FILL = (238, 235, 226)                 # garment fill
EDGE = (184, 179, 165)                 # garment outline
BODY = (232, 228, 218)                 # body behind garment

HEI  = "/System/Library/Fonts/STHeiti Medium.ttc"
HIRA = "/System/Library/Fonts/Hiragino Sans GB.ttc"
MONO = "/System/Library/Fonts/SFNSMono.ttf"

def fb(s): return ImageFont.truetype(HEI, s)
def fr(s): return ImageFont.truetype(HIRA, s)
def fm(s): return ImageFont.truetype(MONO, s)

M = 70


def head(d, eyebrow, l1, l2=None, l2col=INK):
    d.text((M, 62), eyebrow, font=fb(25), fill=ACC)
    d.text((M, 112), l1, font=fb(58), fill=INK)
    if l2:
        d.text((M, 186), l2, font=fb(58), fill=l2col)


def foot(d, t1, t2, top=None):
    by = top if top else H - 168
    d.rounded_rectangle([M, by, W - M, by + 104], radius=14, fill=INK)
    d.text((M + 26, by + 22), t1, font=fb(23), fill=(240, 198, 168))
    d.text((M + 26, by + 58), t2, font=fr(21), fill=(196, 192, 184))
    d.text((M, H - 46), "curify-ai.com", font=fr(21), fill=MUTE)


def pill(d, x, y, text, font, fg, bg, padx=14, pady=7):
    tw = int(d.textlength(text, font=font))
    asc, desc = font.getmetrics()
    d.rounded_rectangle([x, y, x + tw + padx * 2, y + asc + desc + pady * 2],
                        radius=9, fill=bg)
    d.text((x + padx, y + pady), text, font=font, fill=fg)
    return x + tw + padx * 2


# ══════════════════════════════════════════════════ 01 · 七类翻车
im = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(im)

head(d, "服装 AI 出图 · 买家自己写的清单", "不能出现的", "七类问题。", ACC)

ROWS = [
    ("款式不还原 / 货不对版", "图好看但货不对 —— 退货率自己就上去了", True),
    ("姿势呆板",             "手直着贴在身侧、两只脚平行、表情是空的", False),
    ("脸和头发油",           "磨皮严重，AI 痕迹严重", False),
    ("头大 / 显胖",          "身材 55 分", False),
    ("色差",                 "肤色不匀，而且棚拍和外景之间还会飘", False),
    ("季节搭配分明",         "夏装配了冬天的配饰", False),
    ("图片过于相似",         "背景一样，或者姿势几乎一样", False),
]

y = 286
RH = 120
for i, (label, sub, first) in enumerate(ROWS, start=1):
    # big numeral, left gutter
    num = str(i)
    nf = fb(52)
    d.text((M, y + 20), num, font=nf, fill=ACC if first else (200, 196, 186))
    tx = M + 72

    d.text((tx, y + 14), label, font=fb(36), fill=INK)
    if first:
        lw = int(d.textlength(label, font=fb(36)))
        pill(d, tx + lw + 18, y + 20, "重中之重", fb(20), BG, ACC)
    d.text((tx, y + 64), sub, font=fr(25), fill=MUTE)

    if i < len(ROWS):
        d.line([(M, y + RH - 6), (W - M, y + RH - 6)], fill=RULE, width=2)
    y += RH

# the ordering IS the argument — call it out just above the footer
ny = y + 8
d.line([(M, ny), (M + 96, ny)], fill=ACC, width=4)
d.text((M, ny + 22), "注意顺序 —— 第一条是货不对版，不是好不好看。",
       font=fb(28), fill=INK)
d.text((M, ny + 64), "而 AI 最容易出问题的恰好是第一条：模型在重新画这件衣服，不是在搬这件衣服。",
       font=fr(23), fill=MUTE)

assert ny + 64 + 34 < H - 168, "closing note collides with the footer bar"

foot(d, "一个款出一整套图，产品线可以批量出",
     "发一张平铺图，我免费跑一套，连细节回检一起给你看 · 私信")
im.save(OUT + "rn-服装1-七类翻车.jpg", quality=94)
print("wrote rn-服装1-七类翻车.jpg")


# ══════════════════════════════════════════════════ 02 · 五个机位
im = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(im)

head(d, "一张参考图跑五遍 · 不等于一套图", "五张图，", "五个不同的问题。", ACC)


def torso(d, cx, top, w, h, *, placket=False, collar=False, skew=0.0):
    """A boxy garment silhouette. skew shifts the lower edge to suggest a turn."""
    hw = w / 2
    sx = w * skew
    d.polygon([(cx - hw, top), (cx + hw, top),
               (cx + hw + sx * 0.5, top + h), (cx - hw + sx * 0.5, top + h)],
              fill=FILL, outline=EDGE, width=3)
    # shoulder line
    d.line([(cx - hw, top + 10), (cx + hw, top + 10)], fill=EDGE, width=2)
    if placket:
        d.line([(cx + sx * 0.18, top + 14), (cx + sx * 0.5, top + h - 8)],
               fill=EDGE, width=2)
        for k in range(3):
            by = top + 44 + k * (h - 90) / 2
            d.ellipse([cx - 5 + sx * 0.24, by - 5, cx + 5 + sx * 0.24, by + 5],
                      fill=ACC)
    if collar:
        d.chord([cx - 26, top - 12, cx + 26, top + 26], 0, 180,
                fill=(246, 244, 237), outline=EDGE, width=3)
        d.line([(cx - 26, top + 7), (cx + 26, top + 7)], fill=EDGE, width=2)


def legs(d, cx, top, w, h):
    hw = w / 2
    d.polygon([(cx - hw, top), (cx + hw, top),
               (cx + hw - 6, top + h), (cx + 8, top + h),
               (cx + 5, top + 26), (cx - 5, top + 26),
               (cx - 8, top + h), (cx - hw + 6, top + h)],
              fill=BODY, outline=EDGE, width=3)


PN = 5
GAP = 14
PW = (W - 2 * M - GAP * (PN - 1)) // PN          # 176
PH = 400
py = 312

FY = py + 64          # every figure lives in this box, 190 tall
FH = 190
TY = py + 272         # caption baseline, clear of every figure

PANELS = [
    ("正面",      "款式、门襟、扣子"),
    ("背面",      "后领、背部结构"),
    ("全身",      "衣长和松紧\n买家就看这张"),
    ("四分之三侧", "侧面才看得清\n的结构"),
    ("生活场景",  "氛围，不是细节"),
]

for i, (title, sub) in enumerate(PANELS):
    x = M + i * (PW + GAP)
    d.rounded_rectangle([x, py, x + PW, py + PH], radius=12,
                        fill=CARD, outline=RULE, width=2)
    cx = x + PW / 2

    if i == 0:
        torso(d, cx, FY + 10, 100, 170, placket=True)
    elif i == 1:
        torso(d, cx, FY + 20, 100, 160, collar=True)
    elif i == 2:
        torso(d, cx, FY + 8, 92, 92, placket=True)
        legs(d, cx, FY + 104, 78, 86)
    elif i == 3:
        torso(d, cx, FY + 10, 88, 170, placket=True, skew=0.26)
        # the side seam is the whole reason this frame exists
        sx0, sy0 = cx + 30, FY + 26
        sx1, sy1 = cx + 41, FY + 172
        d.line([(sx0, sy0), (sx1, sy1)], fill=ACC, width=4)
    else:
        d.rectangle([x + 18, FY, x + PW - 18, FY + FH],
                    fill=(243, 240, 232), outline=RULE, width=2)
        d.line([(x + 18, FY + 144), (x + PW - 18, FY + 144)], fill=RULE, width=2)
        torso(d, cx, FY + 64, 56, 76)

    pill(d, x + 12, py + 12, str(i + 1), fb(21), BG, INK, padx=11, pady=5)

    d.text((x + 11, TY), title, font=fb(27), fill=INK)
    assert d.textlength(title, font=fb(27)) <= PW - 18, \
        f"panel {i+1} title overflows: {title}"
    for k, line in enumerate(sub.split("\n")):
        assert d.textlength(line, font=fr(19)) <= PW - 18, \
            f"panel {i+1} caption line overflows: {line}"
        d.text((x + 11, TY + 40 + k * 27), line, font=fr(19), fill=MUTE)

# every figure must stay inside its panel and clear of its caption
assert FY + FH < TY - 10, "figure overruns the caption"
assert TY + 40 + 28 * 2 < py + PH - 8, "caption overruns the panel"

# ── the contrast: one reference vs five ──────────────────────────────────────
cy = py + PH + 40
d.line([(M, cy), (W - M, cy)], fill=RULE, width=2)


def mark_x(d, cx, cy, r, col):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
    k = r * 0.44
    d.line([(cx - k, cy - k), (cx + k, cy + k)], fill=CARD, width=5)
    d.line([(cx - k, cy + k), (cx + k, cy - k)], fill=CARD, width=5)


def mark_v(d, cx, cy, r, col):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
    d.line([(cx - r * 0.46, cy + r * 0.02),
            (cx - r * 0.10, cy + r * 0.38),
            (cx + r * 0.48, cy - r * 0.40)], fill=CARD, width=5, joint="curve")


def strip(d, y, drawmark, mcol, line1, line2):
    d.rounded_rectangle([M, y, W - M, y + 130], radius=14, fill=CARD,
                        outline=RULE, width=2)
    drawmark(d, M + 48, y + 65, 25, mcol)
    d.text((M + 96, y + 32), line1, font=fb(30), fill=INK)
    d.text((M + 96, y + 78), line2, font=fr(23), fill=MUTE)


strip(d, cy + 30, mark_x, ACC,
      "同一张参考图 × 5",
      "五张几乎一样的图 —— 那是一张图加了点噪声，不是一套图")
strip(d, cy + 186, mark_v, GOOD,
      "五张参考图 × 5，并记下哪张出了哪张",
      "某一张不对的时候，你知道该换什么，而不是整套重跑")

d.text((M, cy + 350),
       "背景也要真的不一样：同一个场景换角度、换光、换道具位置算；",
       font=fr(23), fill=MUTE)
d.text((M, cy + 384),
       "同一个机位拍两次，不算。",
       font=fr(23), fill=MUTE)

assert cy + 384 + 34 < H - 168, "closing note collides with the footer bar"

foot(d, "一个 SKU 一整套图，产品线可以批量出",
     "发一张平铺图，我免费跑一套五张，并告诉你每张在承担什么 · 私信")
im.save(OUT + "rn-服装2-五个机位.jpg", quality=94)
print("wrote rn-服装2-五个机位.jpg")
