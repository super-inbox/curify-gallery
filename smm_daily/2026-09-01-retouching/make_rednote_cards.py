# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC = "/Users/qqwjq/curify-studio/dev/jayw/video_pipelines/ecommerce_to_video/products/gen/"
OUT = "/Users/qqwjq/curify-gallery/smm_daily/2026-09-01-retouching/"

W, H = 1080, 1440                      # RedNote 3:4
BG   = (250, 248, 242)
INK  = (26, 26, 26)
MUTE = (120, 116, 106)
ACC  = (192, 82, 30)
GOOD = (58, 106, 84)
CARD = (255, 255, 255)
RULE = (226, 222, 212)

HEI  = "/System/Library/Fonts/STHeiti Medium.ttc"        # bold-ish
HIRA = "/System/Library/Fonts/Hiragino Sans GB.ttc"      # regular
MONO = "/System/Library/Fonts/SFNSMono.ttf"

def fb(s): return ImageFont.truetype(HEI, s)
def fr(s): return ImageFont.truetype(HIRA, s)
def fm(s): return ImageFont.truetype(MONO, s)

M = 70

def head(d, eyebrow, l1, l2=None):
    d.text((M, 62), eyebrow, font=fb(25), fill=ACC)
    d.text((M, 112), l1, font=fb(58), fill=INK)
    if l2:
        d.text((M, 186), l2, font=fb(58), fill=INK)

def foot(d, t1, t2, top=None):
    by = top if top else H - 168
    d.rounded_rectangle([M, by, W - M, by + 104], radius=14, fill=(26, 26, 26))
    d.text((M + 26, by + 22), t1, font=fb(23), fill=(240, 198, 168))
    d.text((M + 26, by + 58), t2, font=fr(21), fill=(196, 192, 184))
    d.text((M, H - 46), "curify-ai.com", font=fr(21), fill=MUTE)


# ============================================================ 01 批量一致性
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
head(d, "同一个产品 · 同一条流水线 · 跑两次", "出来的不是")
d.text((M, 186), "同一个瓶子。", font=fb(58), fill=ACC)

PW, PH = 434, 360
GAP = 32
x0, x1 = M, M + PW + GAP

def contain(img, pw, ph, ground):
    s = min(pw / img.width, ph / img.height)
    im2 = img.resize((max(1, int(img.width * s)), max(1, int(img.height * s))), Image.LANCZOS)
    p = Image.new("RGB", (pw, ph), ground)
    p.paste(im2, ((pw - im2.width) // 2, (ph - im2.height) // 2))
    return p

r1 = 296
d.text((M, r1 - 34), "各自生成 —— 主体漂了", font=fb(23), fill=ACC)
shelf  = Image.open(SRC + "serum_scene_shelf.jpg").crop((424, 296, 616, 776))
vanity = Image.open(SRC + "serum_scene_vanity.jpg").crop((414, 224, 622, 782))
for x, crop, tag in ((x0, shelf, "第 1 次"), (x1, vanity, "第 2 次")):
    im.paste(contain(crop, PW, PH, (240, 237, 229)), (x, r1))
    d.rectangle([x, r1, x + PW, r1 + PH], outline=RULE, width=2)
    tw = int(d.textlength(tag, font=fb(21)))
    d.rounded_rectangle([x + 12, r1 + 12, x + 40 + tw, r1 + 50], radius=8, fill=(26, 26, 26))
    d.text((x + 26, r1 + 19), tag, font=fb(21), fill=(250, 248, 242))

cy = r1 + PH + 20
for i, (a, b) in enumerate([
        ("泵头套管", "一节光面  →  分层带环"),
        ("标  签", "不透白、硬边  →  半透灰"),
        ("瓶  肩", "窄而方  →  宽而圆")]):
    d.text((M, cy + i * 34), "·", font=fb(24), fill=ACC)
    d.text((M + 22, cy + i * 34), a, font=fb(24), fill=INK)
    d.text((M + 150, cy + i * 34), b, font=fr(22), fill=MUTE)

r2 = 836
d.text((M, r2 - 34), "抠一次，贴两个背景", font=fb(23), fill=GOOD)
cut = Image.open(SRC + "serum.png").convert("RGBA")
ch = 282
cut = cut.resize((max(1, int(cut.width * ch / cut.height)), ch), Image.LANCZOS)

def sweep(top, mid, bot):
    g = Image.new("RGB", (PW, PH)); dr = ImageDraw.Draw(g)
    sp = int(PH * 0.68)
    for y in range(PH):
        if y < sp:
            t = y / sp; c = tuple(int(top[i] + (mid[i]-top[i]) * t) for i in range(3))
        else:
            t = (y - sp) / (PH - sp); c = tuple(int(mid[i] + (bot[i]-mid[i]) * t) for i in range(3))
        dr.line([(0, y), (PW, y)], fill=c)
    return g.filter(ImageFilter.GaussianBlur(1.2))

for x, (tag, ground) in zip((x0, x1), [
        ("背景 A", sweep((38, 52, 84), (92, 108, 138), (232, 232, 236))),
        ("背景 B", sweep((214, 206, 194), (232, 226, 216), (245, 242, 236)))]):
    p = ground.convert("RGBA")
    px = (PW - cut.width) // 2; py = PH - ch - 36
    sh = Image.new("RGBA", (PW, PH), (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse([px - 16, py + ch - 18, px + cut.width + 16, py + ch + 22],
                               fill=(0, 0, 0, 78))
    p.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
    p.alpha_composite(cut, (px, py))
    im.paste(p.convert("RGB"), (x, r2))
    d.rectangle([x, r2, x + PW, r2 + PH], outline=RULE, width=2)
    tw = int(d.textlength(tag, font=fb(21)))
    d.rounded_rectangle([x + 12, r2 + 12, x + 40 + tw, r2 + 50], radius=8, fill=GOOD)
    d.text((x + 26, r2 + 19), tag, font=fb(21), fill=(250, 248, 242))

d.text((M, r2 + PH + 20), "逐像素相同 —— 不是提示词写了，是主体根本没进模型。",
       font=fb(24), fill=GOOD)
foot(d, "一个瓶子，重画的只是标签。",
     "一整批模特图，跑偏的是买家正在量的版型。", top=H - 176)
im.save(OUT + "rn1-批量一致性.jpg", quality=94)


# ============================================================ 02 四个翻车点
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
head(d, "电商模特图 · 批量验收", "四个必查的", "翻车点")

items = [
    ("01", "内搭穿帮", ["原图模特里面那件打底会跟着出来，成品看着", "像穿在内衣外面。整版作废，最常见的一种。"]),
    ("02", "廓形漂移", ["宽松款悄悄变修身。图很好看，但买家在量的", "胸围和衣长变了 —— 退货率就藏在这里。"]),
    ("03", "细节抹平", ["扣子数量变了，尖角下摆变成平下摆，口袋线没了。", "可数的细节最不稳，也最好查。"]),
    ("04", "领口内里瞎编", ["单图生成时模型没见过后领内侧，只能编。", "颜色错的比形状错的多。"]),
]
y = 300
for num, title, lines in items:
    d.rounded_rectangle([M, y, W - M, y + 196], radius=14, fill=CARD, outline=RULE, width=2)
    d.text((M + 28, y + 26), num, font=fm(26), fill=ACC)
    d.text((M + 92, y + 20), title, font=fb(34), fill=INK)
    for i, ln in enumerate(lines):
        d.text((M + 92, y + 84 + i * 40), ln, font=fr(23), fill=MUTE)
    y += 216

foot(d, "别拿成品去比原图。",
     "挂拍和上身没有共同的基准点 —— 要比，比你自己的尺码表。")
im.save(OUT + "rn2-模特图翻车点.jpg", quality=94)


# ============================================================ 03 场景增强
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
head(d, "场景增强 · 人物锁死，只换背景", "两条路，", "只有一条不动脸。")

def lane(top, tag, col, steps, notes, ncol):
    h = 232
    d.rounded_rectangle([M, top, W - M, top + h], radius=14, fill=CARD, outline=RULE, width=2)
    d.text((M + 28, top + 24), tag, font=fb(25), fill=col)
    x = M + 28; yy = top + 80
    for i, s in enumerate(steps):
        w = d.textlength(s, font=fr(23)) + 30
        d.rounded_rectangle([x, yy, x + w, yy + 48], radius=8,
                            fill=(246, 244, 237), outline=RULE, width=2)
        d.text((x + 15, yy + 11), s, font=fr(23), fill=INK)
        x += w
        if i < len(steps) - 1:
            d.text((x + 8, yy + 10), "→", font=fr(24), fill=MUTE); x += 40
    for i, ln in enumerate(notes):
        d.text((M + 28, top + 150 + i * 32), ln, font=fr(22), fill=ncol)
    return top + h + 30

y = lane(300, "全图重绘", ACC, ["整张图进模型", "整张图出来"],
         ["每个像素都被改写 —— 这不是谁设置错了，是方法本身。",
          "脸会变。而且常常变得刚好让你签收。"], ACC)
y = lane(y, "分割 → 生成背景 → 合成", GOOD, ["抠出主体", "只生成背景", "贴回去"],
         ["主体像素原封不动 —— 不是靠指令，是靠定义。",
          "它压根没进过模型。"], GOOD)

d.text((M, y + 16), "所以「不要动人物」写在提示词里，不是控制手段。", font=fb(26), fill=INK)
d.text((M, y + 58), "提示词是请求，合成才是保证。", font=fr(25), fill=MUTE)
d.text((M, y + 110), "* 这是我们对这类需求的判断，不是跑出来的结论。", font=fr(20), fill=MUTE)

qy = y + 168
d.rounded_rectangle([M, qy, W - M, qy + 236], radius=14, fill=CARD, outline=RULE, width=2)
d.text((M + 28, qy + 24), "验收就查三处，一分钟", font=fb(25), fill=INK)
for i, ln in enumerate([
        "100% 放大看睫毛和碎发 —— 动了一根，就是重绘不是合成",
        "皮肤要留得住毛孔。糊了就是磨皮了",
        "眼里那个高光点最灵 —— 重绘几乎一定会挪位置"]):
    d.text((M + 28, qy + 80 + i * 46), "·", font=fb(24), fill=ACC)
    d.text((M + 50, qy + 80 + i * 46), ln, font=fr(23), fill=MUTE)

foot(d, "批量的难点是一致，不是好看。",
     "全身 / 半身 / 特写三种景别，按套走量，量大单价明显往下走。")
im.save(OUT + "rn3-场景增强.jpg", quality=94)

print("done")
