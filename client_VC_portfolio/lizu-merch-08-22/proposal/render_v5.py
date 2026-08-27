# -*- coding: utf-8 -*-
"""V5：祝福语 · 黎锦纹样带 · 复合式冰箱贴 · 白查十二时系列。

依据 2026-08-27 客户反馈与 examples/bestsellers：
  畅销款 = 木框 + 真实黎锦织物 + 银饰 + 品牌背卡（三层材质，不是平面印刷图腾）
  两个负面参考夹住口味区间：吴哥土色拓片「老气」/ 掐丝珐琅 Q 版「太现代」
所有纹样仍取自 assets/totem-lib（客户原稿矢量）。
"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, "assets/totem-lib/mask")
META = json.load(open(f"{T}/meta.json"))
FZ = "/System/Library/Fonts/STHeiti Medium.ttc"
FS = "/System/Library/Fonts/Supplemental/Songti.ttc"
def font(s, serif=False): return ImageFont.truetype(FS if serif else FZ, s)

INK=(0x14,0x20,0x2B); MUT=(0x8A,0x92,0x99); SUB=(0x38,0x43,0x4E)
NAVY=(0x16,0x2B,0x45); CREAM=(0xF2,0xF0,0xE8); GOLD=(0xC8,0x95,0x2E)
RED=(0xC2,0x35,0x2C); WOOD=(0xA8,0x7C,0x50); WOOD2=(0x8B,0x62,0x3C)
SILVER=(0xD6,0xDA,0xDE); SILV2=(0xA8,0xB0,0xB8); PAPER=(0xF4,0xF3,0xEE)
TEAL=(0x0E,0x7C,0x94); ORG=(0xFF,0x7A,0x59); GRN=(0x2F,0x6B,0x4F)

# 祝福语 —— 由客户原稿的官方寓意改写，可直接上吊牌
BLESS = {
 "image1": ("大力神",  "自然与英雄崇拜",   "山高水长 · 护你周全"),
 "image2": ("大力神·繁衍","繁衍生息 长久万代","生生不息 · 代代长久"),
 "image3": ("龙图腾",  "风调雨顺",        "风调雨顺 · 岁岁安稳"),
 "image4": ("蝴蝶图腾","美好爱情",        "蝶自飞来 · 有情成双"),
 "image5": ("牛图腾",  "农业丰饶 家庭幸福","五谷丰登 · 家宅安宁"),
 "image6": ("人骑牛图腾","崇尚勇武",       "无畏向前 · 路自宽阔"),
 "image7": ("狗牙花图腾","辟邪护佑",       "花开辟邪 · 一路平安"),
 "image8": ("摇篮图腾","婴儿安宁 人丁兴旺","稚子安睡 · 家有新枝"),
 "image9": ("龟图腾",  "延年益寿",        "慢慢来 · 长长久久"),
 "image10":("狗图腾",  "护家平安",        "有它守门 · 家宅无忧"),
 "image11":("鸟图腾",  "爱情美满 排忧解难","心事有解 · 良人常伴"),
 "image12":("鱼图腾",  "年年丰收 五谷丰登","年年有余 · 岁岁丰足"),
 "image13":("鹿图腾",  "吉祥如意 幸福平安","所遇皆吉 · 所愿皆成"),
 "image14":("蛙图腾",  "多子多福",        "多子多福 · 雨水丰沛"),
 "image15":("人图腾",  "祖先崇拜",        "根在此处 · 行必有归"),
}

def mask(k): return np.array(Image.open(f"{T}/{k}.png").convert("L")) > 127

def glyph(k, size, color, pad=.10):
    m = mask(k); h, w = m.shape
    box = int(size*(1-pad*2)); sc = min(box/w, box/h)
    im = Image.fromarray((m*255).astype("uint8")).resize(
        (max(1,int(w*sc)), max(1,int(h*sc))), Image.LANCZOS)
    L = Image.new("RGBA", (size, size), (0,0,0,0))
    L.paste(Image.new("RGBA", im.size, color+(255,)), ((size-im.width)//2,(size-im.height)//2), im)
    return L

def glyph_fit(k, w, h, color):
    """按给定宽高盒子等比缩放（用于纹样带）。"""
    m = mask(k); mh, mw = m.shape
    sc = min(w/mw, h/mh)
    im = Image.fromarray((m*255).astype("uint8")).resize(
        (max(1,int(mw*sc)), max(1,int(mh*sc))), Image.LANCZOS)
    L = Image.new("RGBA", (w, h), (0,0,0,0))
    L.paste(Image.new("RGBA", im.size, color+(255,)), ((w-im.width)//2,(h-im.height)//2), im)
    return L

def rr(sz, fill, r=14, outline=None, w=0):
    c = Image.new("RGBA", sz, (0,0,0,0))
    ImageDraw.Draw(c).rounded_rectangle([0,0,sz[0]-1,sz[1]-1], r, fill=fill, outline=outline, width=w)
    return c

def brocade(w, h, keys, ground=NAVY, cols=(CREAM, RED, (0x6E,0x9A,0xC4)), rows=3):
    """黎锦纹样带：深底 + 图腾横向重复，行间夹细几何线。真实黎锦即此结构。"""
    band = Image.new("RGBA", (w, h), ground+(255,))
    d = ImageDraw.Draw(band)
    rh = h / rows
    for r in range(rows):
        k = keys[r % len(keys)]
        c = cols[r % len(cols)]
        cell = int(rh*0.86)
        n = max(2, int(w / (cell*1.1)))
        step = w / n
        for i in range(n):
            g = glyph_fit(k, int(step*0.86), cell, c)
            band.alpha_composite(g, (int(i*step + (step-g.width)/2), int(r*rh + (rh-cell)/2)))
        if r < rows-1:
            y = int((r+1)*rh)
            d.line([0,y,w,y], fill=cols[(r+1) % len(cols)]+(150,), width=max(1,int(h*0.012)))
    return band

def silver_crescent(w, h):
    """黎族银饰：月牙 + 流苏（畅销款上的标志性配件）。"""
    L = Image.new("RGBA", (w, h), (0,0,0,0)); d = ImageDraw.Draw(L)
    d.pieslice([0, 0, w, int(h*1.25)], 195, 345, fill=SILVER+(255,))
    d.pieslice([int(w*.13), int(h*.16), int(w*.87), int(h*1.14)], 195, 345, fill=(0,0,0,0))
    d.arc([0, 0, w, int(h*1.25)], 195, 345, fill=SILV2+(255,), width=2)
    n = 7
    for i in range(n):
        x = int(w*.14 + i*(w*.72)/(n-1))
        d.line([x, int(h*.52), x, int(h*.86)], fill=SILV2+(255,), width=3)
        d.ellipse([x-4, int(h*.84), x+4, int(h*.98)], fill=SILVER+(255,))
    return L

def header(d, t, sub, pad=44):
    d.text((pad,32), t, font=font(30, True), fill=INK)
    d.text((pad,74), sub, font=font(14), fill=MUT)


# ── 1. 祝福语对照 ────────────────────────────────────────────
def sheet_bless(path):
    C, CW, pad, gap, head = 5, 218, 44, 16, 112
    keys = list(BLESS)
    rows = (len(keys)+C-1)//C
    W = pad*2 + CW*C + gap*(C-1); H = head + rows*(CW+88) + pad
    im = Image.new("RGB", (W,H), (0xFA,0xFA,0xF8)); d = ImageDraw.Draw(im)
    header(d, "十五式图腾 · 祝福语", "每款产品认领一句，印在吊牌与背卡上。这是游客「带走的理由」——买的不是纪念品，是一句祝福。")
    for i,k in enumerate(keys):
        x = pad + (i%C)*(CW+gap); y = head + (i//C)*(CW+88)
        t = rr((CW,CW), NAVY+(255,), 14)
        t.alpha_composite(glyph(k, CW, CREAM, pad=.22))
        im.paste(t,(x,y),t)
        nm, mean, bl = BLESS[k]
        d.text((x, y+CW+9),  nm,   font=font(15, True), fill=INK)
        d.text((x, y+CW+31), mean, font=font(11),       fill=MUT)
        d.text((x, y+CW+52), bl,   font=font(14, True), fill=RED)
    im.save(path, quality=92); print("  ok", os.path.basename(path), im.size)


# ── 2. 黎锦纹样带 ────────────────────────────────────────────
def sheet_brocade(path):
    pad, head = 44, 112
    W, BW, BH, gap = 1290, 1202, 118, 22
    specs = [("三行经典带", ["image4","image14","image12"], NAVY, (CREAM,RED,(0x6E,0x9A,0xC4))),
             ("双色素雅带", ["image9","image7"],            NAVY, (CREAM,(0x8C,0xA9,0xC4))),
             ("暖色节庆带", ["image11","image13","image5"], (0x14,0x20,0x2B), (GOLD,RED,CREAM)),
             ("浅底反转带", ["image12","image4","image9"],  PAPER, (NAVY,RED,TEAL))]
    H = head + len(specs)*(BH+46) + pad
    im = Image.new("RGB",(W,H),(0xFA,0xFA,0xF8)); d = ImageDraw.Draw(im)
    header(d, "黎锦纹样带（由真实图腾生成）",
           "畅销款上真正抓眼的是密集的织锦纹样带，而非单一图腾。黎锦本身就是「图腾横向重复 + 行间细线」的结构，故可由 15 式忠实生成。")
    y = head
    for nm, keys, gr, cols in specs:
        band = brocade(BW, BH, keys, ground=gr, cols=cols)
        im.paste(band, (pad, y), band)
        d.text((pad, y+BH+8), nm, font=font(15, True), fill=INK)
        d.text((pad+130, y+BH+9), " · ".join(BLESS[k][0] for k in keys), font=font(12), fill=MUT)
        y += BH+46
    im.save(path, quality=92); print("  ok", os.path.basename(path), im.size)


# ── 3. 复合式冰箱贴（对标畅销款三层材质）────────────────────
def sheet_composite(path):
    CW, pad, gap, head = 300, 44, 20, 124
    C = 4; W = pad*2 + CW*C + gap*(C-1); H = head + CW + 96 + pad
    im = Image.new("RGB",(W,H),(0xFA,0xFA,0xF8)); d = ImageDraw.Draw(im)
    header(d, "冰箱贴 · 复合款（对标贵司畅销款的材质层次）",
           "畅销款 = 木框 + 真实织锦 + 银饰 + 品牌背卡。以下保留这套结构，只把织锦与图腾换成美孚原稿纹样，并加上祝福语。")
    specs = [("圆形木框 · 织锦嵌片","image14",["image4","image14"],"round",True),
             ("筒裙形 · 织锦满嵌","image12",["image12","image9","image4"],"skirt",True),
             ("扇形 · 纹样带 + 银饰","image11",["image11","image13"],"fan",True),
             ("方形卡装 · 纹样带底","image7",["image7","image12"],"card",False)]
    y = head
    for i,(nm,hero,bandkeys,kind,silver) in enumerate(specs):
        x = pad + i*(CW+gap)
        t = Image.new("RGBA",(CW,CW),(0,0,0,0)); dd = ImageDraw.Draw(t)
        # 背卡（米色卡纸）
        t.alpha_composite(rr((CW-20,CW-20), (0xED,0xE7,0xD6,255), 10), (10,10))
        bb = brocade(CW-20, 20, ["image4","image9"], ground=NAVY, cols=(CREAM,RED), rows=1)
        t.alpha_composite(bb, (10, CW-38))
        d2 = ImageDraw.Draw(t)
        d2.text((20, 18), "海南黎族织锦", font=font(15, True), fill=NAVY)
        d2.text((20, 40), "BAICHA · 白查村", font=font(10), fill=MUT)
        cx, cy = CW//2, CW//2 + 6
        if kind == "round":
            R = 84
            dd.ellipse([cx-R,cy-R,cx+R,cy+R], fill=WOOD+(255,))
            dd.ellipse([cx-R+13,cy-R+13,cx+R-13,cy+R-13], fill=NAVY+(255,))
            inner = brocade(2*(R-13), 2*(R-13), bandkeys, rows=3)
            cm = Image.new("L",(2*(R-13),)*2,0); ImageDraw.Draw(cm).ellipse([0,0,2*(R-13)-1,2*(R-13)-1],fill=255)
            t.paste(inner,(cx-R+13,cy-R+13),cm)
            dd.ellipse([cx-R,cy-R,cx+R,cy+R], outline=WOOD2+(255,), width=3)
        elif kind == "skirt":
            pts=[(cx-52,cy-70),(cx+52,cy-70),(cx+72,cy+72),(cx-72,cy+72)]
            dd.polygon(pts, fill=WOOD+(255,))
            inner=[(cx-42,cy-58),(cx+42,cy-58),(cx+60,cy+60),(cx-60,cy+60)]
            dd.polygon(inner, fill=NAVY+(255,))
            bb2 = brocade(124, 120, bandkeys, rows=3)
            pm = Image.new("L",(124,120),0); ImageDraw.Draw(pm).polygon(
                [(p[0]-(cx-62), p[1]-(cy-60)) for p in inner], fill=255)
            t.paste(bb2,(cx-62,cy-60),pm)
        elif kind == "fan":
            dd.pieslice([cx-92,cy-56,cx+92,cy+128], 180, 360, fill=WOOD+(255,))
            dd.pieslice([cx-78,cy-42,cx+78,cy+114], 180, 360, fill=NAVY+(255,))
            bb3 = brocade(156, 78, bandkeys, rows=2)
            fm = Image.new("L",(156,78),0)
            ImageDraw.Draw(fm).pieslice([0,0,156,156],180,360,fill=255)
            t.paste(bb3,(cx-78,cy-42),fm)
        else:
            dd.rounded_rectangle([cx-88,cy-72,cx+88,cy+72], 10, fill=NAVY+(255,))
            bb4 = brocade(176, 144, bandkeys, rows=4)
            km = Image.new("L",(176,144),0)
            ImageDraw.Draw(km).rounded_rectangle([0,0,175,143],10,fill=255)
            t.paste(bb4,(cx-88,cy-72),km)
            t.alpha_composite(glyph(hero, 96, GOLD, pad=.06), (cx-48, cy-48))
        if kind != "card":
            t.alpha_composite(glyph(hero, 78, GOLD, pad=.06), (cx-39, cy-34))
        if silver:
            sc = silver_crescent(96, 54)
            t.alpha_composite(sc, (cx-48, cy+44))
        im.paste(t,(x,y),t)
        d.text((x, y+CW+10), nm, font=font(16, True), fill=INK)
        d.text((x, y+CW+34), BLESS[hero][2], font=font(14, True), fill=RED)
        d.text((x, y+CW+58), "木框 + 织锦纹样 + " + ("银饰 + " if silver else "") + "祝福语背卡",
               font=font(11), fill=MUT)
    im.save(path, quality=92); print("  ok", os.path.basename(path), im.size)


# ── 4. 白查十二时 · 明信片/贴纸系列 ──────────────────────────
def sheet_baicha12(path):
    CW, CH, pad, gap, head = 218, 300, 44, 16, 124
    C = 6
    scenes = [("晨· 炊烟","image15","晨起 · 炊烟自屋顶升"),
              ("辰· 织锦","image4","日光上机 · 一寸一寸织"),
              ("午· 稻田","image5","牛行田间 · 五谷渐熟"),
              ("未· 溪浴","image12","溪水清凉 · 鱼在脚边"),
              ("酉· 归家","image13","日落而归 · 鹿影入林"),
              ("夜· 火塘","image1","火塘不熄 · 祖先在侧")]
    W = pad*2 + CW*C + gap*(C-1); H = head + CH + 76 + pad
    im = Image.new("RGB",(W,H),(0xFA,0xFA,0xF8)); d = ImageDraw.Draw(im)
    header(d, "「白查十二时」· 明信片 / 贴纸系列",
           "方向 C 的插画语言按会议决定只用于纸品。以六个时辰串起村落一日，六张成套——成套是收集动机，也是提高客单价最便宜的办法。")
    grounds = [(0xF6,0xE9,0xD2),(0xE9,0xF0,0xE4),(0xF3,0xE4,0xD8),
               (0xDE,0xEC,0xEF),(0xF2,0xE2,0xDC),(0x1E,0x2A,0x38)]
    inks =    [NAVY,GRN,(0x8B,0x5E,0x3C),TEAL,RED,GOLD]
    for i,(t1,k,cap) in enumerate(scenes):
        x = pad + i*(CW+gap); y = head
        card = rr((CW,CH), grounds[i]+(255,), 10, outline=(0xD8,0xDC,0xD4,255), w=2)
        cd = ImageDraw.Draw(card)
        band = brocade(CW-2, 26, ["image4","image9"], ground=NAVY,
                       cols=(CREAM,RED,(0x6E,0x9A,0xC4)), rows=1)
        card.alpha_composite(band, (1, CH-27))
        card.alpha_composite(glyph(k, 150, inks[i], pad=.08), (CW//2-75, 74))
        cd.text((18, 24), t1, font=font(21, True), fill=inks[i])
        cd.line([18, 56, 62, 56], fill=inks[i]+(160,), width=2)
        cd.text((18, CH-72), cap, font=font(12), fill=inks[i] if i!=5 else CREAM)
        im.paste(card,(x,y),card)
        d.text((x, y+CH+12), t1.replace("· ","·"), font=font(14, True), fill=INK)
    im.save(path, quality=92); print("  ok", os.path.basename(path), im.size)


os.makedirs(os.path.join(HERE,"assets/v5"), exist_ok=True)
sheet_bless(os.path.join(HERE,"assets/v5/v5_blessings.jpg"))
sheet_brocade(os.path.join(HERE,"assets/v5/v5_brocade.jpg"))
sheet_composite(os.path.join(HERE,"assets/v5/v5_magnet_composite.jpg"))
sheet_baicha12(os.path.join(HERE,"assets/v5/v5_baicha12.jpg"))
