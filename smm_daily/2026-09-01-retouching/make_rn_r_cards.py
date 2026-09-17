"""小红书版 · 声线 R（房产图后期）方法卡 —— 1080×1440。

和 FB 的 r1/r2/r3 是同一组论点，但**不是翻译**：
买家换了。美国那边是给经纪人供图的 listing photographer（MLS 交期）；
中文这边对应的是**民宿/短租房东与代运营、家装公司的完工案例图、以及售楼处/楼盘摄影**——
同一门手艺，不同的甲方，所以钩子从"MLS 截稿"换成"房源图点击率 / 案例图交付"。

配图和 FB 一样是**方法卡不是前后对比**，理由见 posts_fb.md 的 Build notes：
这个垂直我们没有可声称的交付成果，也没有一张有权展示的房产前后对比。

    python3 make_rn_r_cards.py
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1440
BG, INK, MUTE = (250, 248, 242), (26, 26, 26), (120, 116, 106)
ACC, GOOD, CARD, RULE = (192, 82, 30), (58, 106, 84), (255, 255, 255), (226, 222, 212)
OUT = "/Users/qqwjq/curify-gallery/smm_daily/2026-09-01-retouching/"
M = 70

HEI = "/System/Library/Fonts/STHeiti Medium.ttc"
HIRA = "/System/Library/Fonts/Hiragino Sans GB.ttc"
MONO = "/System/Library/Fonts/SFNSMono.ttf"


def fb(s):
    return ImageFont.truetype(HEI, s)


def fr(s):
    return ImageFont.truetype(HIRA, s)


def fm(s):
    return ImageFont.truetype(MONO, s)


def head(d, eyebrow, l1, l2=None):
    d.text((M, 62), eyebrow, font=fb(25), fill=ACC)
    d.text((M, 112), l1, font=fb(56), fill=INK)
    if l2:
        d.text((M, 186), l2, font=fb(56), fill=ACC)


def foot(d, t1, t2):
    by = H - 172
    d.rounded_rectangle([M, by, W - M, by + 108], radius=16, fill=(26, 26, 26))
    d.text((M + 26, by + 24), t1, font=fb(24), fill=(240, 198, 168))
    d.text((M + 26, by + 62), t2, font=fr(21), fill=(196, 192, 184))
    d.text((M, H - 46), "curify-ai.com", font=fr(20), fill=MUTE)


# ═══════════════════════ R1 · 改这张图，不是重画一张 ═══════════════════════
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
head(d, "房产图后期 · 甲方最常问的一句", "改这张图，", "不是重画一张。")

y = 300
for tag, col, steps, notes in [
    ("整张重绘", ACC, ["整张图进模型", "整张图出来"],
     ["每个像素都被改写 —— 台面、窗框、地板木纹，全是重新画的。",
      "缩略图看着还行，放大到 100% 就露馅。"]),
    ("原图上改", GOOD, ["框出要改的", "只填那一块", "其余不动"],
     ["你没指的那些像素根本没进模型。",
      "不是提示词里的承诺，是方法本身决定的。"]),
]:
    d.rounded_rectangle([M, y, W - M, y + 250], radius=16, fill=CARD, outline=RULE, width=2)
    d.text((M + 26, y + 22), tag, font=fb(28), fill=col)
    x, yy = M + 26, y + 84
    for i, s in enumerate(steps):
        wd = d.textlength(s, font=fr(22)) + 28
        d.rounded_rectangle([x, yy, x + wd, yy + 46], radius=8,
                            fill=(246, 244, 237), outline=RULE, width=2)
        d.text((x + 14, yy + 11), s, font=fr(22), fill=INK)
        x += wd
        if i < len(steps) - 1:
            d.text((x + 6, yy + 9), "→", font=fr(23), fill=MUTE); x += 34
    for i, ln in enumerate(notes):
        d.text((M + 26, y + 158 + i * 34), ln, font=fr(21), fill=MUTE)
    y += 276

d.text((M, y + 10), "整张重绘我们测过，然后放弃了。", font=fb(27), fill=INK)
d.text((M, y + 52), "与原图的细节相关性 = 0.007", font=fm(24), fill=ACC)

foot(d, "只有你指的那处会动。", "发我一张房源图和你想去掉的东西，我改完发回来，你放大对着看。")
im.save(OUT + "rn-R1-改图不是重画.jpg", quality=94)

# ═══════════════════════ R2 · 去杂物，十秒自检 ═══════════════════════
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
head(d, "去杂物 · 这条线最常接的活", "十秒钟，", "四步查完。")

items = [
    ("两张都放到 100% 再看", "别看平台压缩过的预览图 —— 你要找的痕迹正好被压没了。"),
    ("看东西原来在的那条边", "猜出来的填充是一片糊；真采样周围像素的，纹理颗粒对得上。"),
    ("看连续纹路有没有断", "瓷砖缝、地板木纹、砖缝必须直着穿过去。出现重复或错位就是编的。"),
    ("挑一处你没要求改的地方", "开关面板、踢脚线、远处的窗框。那里也变了 = 整张被重画了。"),
]
y = 320
for t, sub in items:
    d.rounded_rectangle([M, y, W - M, y + 172], radius=14, fill=CARD, outline=RULE, width=2)
    d.ellipse([M + 24, y + 40, M + 40, y + 56], fill=ACC)
    d.text((M + 58, y + 26), t, font=fb(29), fill=INK)
    words, line, ly = sub, "", y + 78
    for ch in words:
        if d.textlength(line + ch, font=fr(21)) > W - 2 * M - 84:
            d.text((M + 58, ly), line, font=fr(21), fill=MUTE); ly += 32; line = ch
        else:
            line += ch
    d.text((M + 58, ly), line, font=fr(21), fill=MUTE)
    y += 190

foot(d, "第四步才是真正的那一步。", "没要求改的地方也变了，说明整张房间被重新生成了。")
im.save(OUT + "rn-R2-去杂物自检.jpg", quality=94)

# ═══════════════════════ R3 · 室内色，别拉成灰的 ═══════════════════════
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
head(d, "室内色", "别拉成灰的，", "留一点暖。")
d.text((M, 272), "甲方几乎不会写进需求单，但每次都挑得出来。", font=fr(24), fill=MUTE)

sw = [((238, 228, 210), "原片", "混合光，窗外过曝"),
      ((246, 240, 228), "窗外找回", "室外救回来，室内留暖"),
      ((228, 234, 238), "过度处理", "发灰、发平、影子全被提亮")]
y, bw = 340, (W - 2 * M - 40) // 3
for i, (c, lab, sub) in enumerate(sw):
    x = M + i * (bw + 20)
    d.rounded_rectangle([x, y, x + bw, y + 168], radius=14, fill=c,
                        outline=ACC if i == 2 else RULE, width=3 if i == 2 else 2)
    d.text((x + 12, y + 182), lab, font=fb(25), fill=ACC if i == 2 else INK)
    line, ly = "", y + 216
    for ch in sub:
        if d.textlength(line + ch, font=fr(19)) > bw - 12:
            d.text((x + 12, ly), line, font=fr(19), fill=MUTE); ly += 26; line = ch
        else:
            line += ch
    d.text((x + 12, ly), line, font=fr(19), fill=MUTE)

y = 640
d.line([(M, y), (W - M, y)], fill=RULE, width=2)
for i, (t, sub) in enumerate([
    ("一套图比单张更值钱", "一套房三十张要读起来像同一个下午 —— 同一个白平衡、同一片天、同一种暖度。"),
    ("按参考图下单，别按参数下单", "「暖一点但别太暖」没人能执行；「对着这套调」可以，而且结果能对着验。"),
]):
    yy = y + 36 + i * 132
    d.text((M, yy), t, font=fb(29), fill=INK)
    line, ly = "", yy + 44
    for ch in sub:
        if d.textlength(line + ch, font=fr(21)) > W - 2 * M:
            d.text((M, ly), line, font=fr(21), fill=MUTE); ly += 32; line = ch
        else:
            line += ch
    d.text((M, ly), line, font=fr(21), fill=MUTE)

foot(d, "发三张，再发一套你想对的色。", "我按那个调回给你，你摆在一起看。")
im.save(OUT + "rn-R3-室内色.jpg", quality=94)

print("done — rn-R1 / rn-R2 / rn-R3")
