# -*- coding: utf-8 -*-
"""Render colorway / shape proposals from the client's AUTHENTIC totem masks.

No generative model touches the motifs — every glyph is the client's own totem,
recoloured and laid out. That is the "考据 → 矢量还原 → 受控应用" workflow, run.
"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np, json, os

T = "totem/mask"
META = json.load(open(f"{T}/meta.json"))
FZ = "/System/Library/Fonts/STHeiti Medium.ttc"
FS = "/System/Library/Fonts/Supplemental/Songti.ttc"
def font(sz, serif=False): return ImageFont.truetype(FS if serif else FZ, sz)

def glyph(key, size, color, pad=0.10):
    """Return an RGBA layer of one totem in `color`, fitted into size box."""
    m = np.array(Image.open(f"{T}/{key}.png").convert("L")) > 127
    h, w = m.shape
    box = int(size * (1 - pad * 2))
    sc = min(box / w, box / h)
    im = Image.fromarray((m * 255).astype("uint8")).resize(
        (max(1, int(w * sc)), max(1, int(h * sc))), Image.LANCZOS)
    layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    solid = Image.new("RGBA", im.size, color + (255,))
    layer.paste(solid, ((size - im.width) // 2, (size - im.height) // 2), im)
    return layer

def rounded(size, fill, r=14):
    c = Image.new("RGBA", size, (0, 0, 0, 0))
    ImageDraw.Draw(c).rounded_rectangle([0, 0, size[0]-1, size[1]-1], r, fill=fill)
    return c

# ── 配色方案：客户否掉的"老气"= 土褐 + 做旧 + 写实 + 满版；这些全部反向 ──
WAYS = [
 ("A 墨蓝本白",  "沉稳 · 已定基调", (0x1E,0x3A,0x5F), (0xF2,0xF0,0xE8)),
 ("B 浅底反转",  "通透 · 留白最多", (0xF4,0xF3,0xEE), (0x16,0x2B,0x45)),
 ("C 海岛明快",  "年轻 · 客单价友好", (0x0E,0x7C,0x94), (0xFF,0x7A,0x59)),
 ("D 椰林清新",  "清爽 · 海南在地", (0xEDF0E8 >> 16 & 255, 0xEDF0E8 >> 8 & 255, 0xEDF0E8 & 255), (0x2F,0x6B,0x4F)),
 ("E 暖阳撞色",  "醒目 · 货架抓眼", (0x14,0x20,0x2B), (0xF2,0xB1,0x2E)),
]
PICK = ["image14", "image11", "image12", "image13"]   # 蛙 鸟 鱼 鹿

def sheet_colorways(path):
    CW, pad, gap = 250, 46, 18
    head, foot = 92, 40
    W = pad*2 + CW*len(PICK) + gap*(len(PICK)-1)
    rowh = CW + foot
    H = head + rowh*len(WAYS) + pad
    im = Image.new("RGB", (W, H), (0xFA, 0xFA, 0xF8))
    d = ImageDraw.Draw(im)
    d.text((pad, 34), "配色方案 · 五选一", font=font(30, True), fill=(0x14,0x20,0x2B))
    d.text((pad, 70), "同一组真实图腾，五种配色。纹样取自贵司掼蛋扑克牌原稿，未作改动。",
           font=font(15), fill=(0x6E,0x76,0x7E))
    y = head
    for label, note, bg, ink in WAYS:
        for i, k in enumerate(PICK):
            x = pad + i*(CW+gap)
            tile = rounded((CW, CW), bg + (255,), 16)
            tile.alpha_composite(glyph(k, CW, ink, pad=0.19))
            im.paste(tile, (x, y), tile)
            if i == 0:
                d.text((x, y+CW+9), label, font=font(17, True), fill=(0x14,0x20,0x2B))
                d.text((x, y+CW+9), " "*0, font=font(13), fill=(0,0,0))
            if i == 1:
                d.text((x, y+CW+12), note, font=font(13), fill=(0x8A,0x92,0x99))
            if i >= 2:
                nm = META[k]["name"]
                d.text((x, y+CW+12), nm, font=font(13), fill=(0x8A,0x92,0x99))
        y += rowh
    im.save(path, quality=92)
    print(f"  ✓ {path}  {im.size[0]}x{im.size[1]}")

# ── 形状 / 版式方案 ──────────────────────────────────────────
def sheet_shapes(path):
    BG, INK, ACC = (0xF4,0xF3,0xEE), (0x1E,0x3A,0x5F), (0xFF,0x7A,0x59)
    CW, pad, gap = 300, 46, 20
    W = pad*2 + CW*4 + gap*3
    H = 92 + CW + 46 + pad
    im = Image.new("RGB", (W, H), (0xFA,0xFA,0xF8)); d = ImageDraw.Draw(im)
    d.text((pad, 34), "版式方案 · 四选一", font=font(30, True), fill=(0x14,0x20,0x2B))
    d.text((pad, 70), "同一个蛙图腾，四种排布方式。选定做法后其余图腾按同一逻辑铺开。",
           font=font(15), fill=(0x6E,0x76,0x7E))
    y = 92
    labels = ["① 单一主体 · 大留白", "② 超大裁切 · 局部特写", "③ 网格重复 · 满版", "④ 横向纹样带"]
    for i, lab in enumerate(labels):
        x = pad + i*(CW+gap)
        tile = rounded((CW, CW), BG + (255,), 16)
        if i == 0:
            tile.alpha_composite(glyph("image14", CW, INK, pad=0.26))
        elif i == 1:
            g = glyph("image14", int(CW*1.9), INK, pad=0.02)
            tile.alpha_composite(g, (-int(CW*0.45), -int(CW*0.42)))
            tile = Image.composite(tile, Image.new("RGBA", tile.size, (0,0,0,0)),
                                   rounded((CW,CW),(255,255,255,255),16).split()[3])
        elif i == 2:
            cell = CW // 4
            for r in range(4):
                for c in range(4):
                    col = INK if (r + c) % 2 == 0 else ACC
                    tile.alpha_composite(glyph("image14", cell, col, pad=0.16), (c*cell, r*cell))
            tile = Image.composite(tile, Image.new("RGBA", tile.size, (0,0,0,0)),
                                   rounded((CW,CW),(255,255,255,255),16).split()[3])
        else:
            band_h = CW // 3
            band = Image.new("RGBA", (CW, band_h), INK + (255,))
            n = 4; cw = CW // n
            for c in range(n):
                band.alpha_composite(glyph("image14", cw, BG, pad=0.20), (c*cw, (band_h-cw)//2))
            tile.alpha_composite(band, (0, (CW-band_h)//2))
            tile = Image.composite(tile, Image.new("RGBA", tile.size, (0,0,0,0)),
                                   rounded((CW,CW),(255,255,255,255),16).split()[3])
        im.paste(tile, (x, y), tile)
        d.text((x, y+CW+13), lab, font=font(15), fill=(0x38,0x43,0x4E))
    im.save(path, quality=92); print(f"  ✓ {path}  {im.size[0]}x{im.size[1]}")

# ── 全套 15 图腾 + 寓意（考据资产总览）────────────────────────
def sheet_library(path):
    C, CW, pad, gap = 5, 210, 46, 16
    keys = list(META.keys())
    rows = (len(keys)+C-1)//C
    W = pad*2 + CW*C + gap*(C-1)
    H = 96 + rows*(CW+56) + pad
    im = Image.new("RGB", (W, H), (0xFA,0xFA,0xF8)); d = ImageDraw.Draw(im)
    d.text((pad, 34), "美孚黎族图腾库 · 15 式", font=font(30, True), fill=(0x14,0x20,0x2B))
    d.text((pad, 72), "全部取自贵司《文创掼蛋扑克纹样参考》原稿，逐一矢量化，未作再创作。",
           font=font(15), fill=(0x6E,0x76,0x7E))
    for i, k in enumerate(keys):
        x = pad + (i % C)*(CW+gap); y = 96 + (i//C)*(CW+56)
        tile = rounded((CW,CW), (0xF2,0xF0,0xE8,255), 14)
        tile.alpha_composite(glyph(k, CW, (0x1E,0x3A,0x5F), pad=0.20))
        im.paste(tile, (x,y), tile)
        d.text((x, y+CW+8),  META[k]["name"],    font=font(16, True), fill=(0x14,0x20,0x2B))
        d.text((x, y+CW+30), META[k]["meaning"], font=font(12),       fill=(0x8A,0x92,0x99))
    im.save(path, quality=92); print(f"  ✓ {path}  {im.size[0]}x{im.size[1]}")

os.makedirs("v3", exist_ok=True)
sheet_library("v3/v3_library.jpg")
sheet_colorways("v3/v3_colorways.jpg")
sheet_shapes("v3/v3_shapes.jpg")
