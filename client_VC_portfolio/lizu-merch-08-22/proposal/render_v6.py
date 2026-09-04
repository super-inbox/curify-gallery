# -*- coding: utf-8 -*-
"""V6：依 national-museum-examples 设计的新 SKU + 全线产品接触表。
纹样一律取自 assets/totem-lib（客户原稿矢量）。"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, "assets/totem-lib/mask")
META = json.load(open(f"{T}/meta.json"))
FZ = "/System/Library/Fonts/STHeiti Medium.ttc"
FS = "/System/Library/Fonts/Supplemental/Songti.ttc"
def font(s, serif=False): return ImageFont.truetype(FS if serif else FZ, s)

INK=(0x14,0x20,0x2B); MUT=(0x8A,0x92,0x99)
NAVY=(0x16,0x2B,0x45); DEEP=(0x0F,0x1E,0x38); CREAM=(0xF2,0xF0,0xE8)
GOLD=(0xC8,0x95,0x2E); RED=(0xC2,0x35,0x2C); WOOD=(0xA8,0x7C,0x50)
WOOD2=(0x8B,0x62,0x3C); SILVER=(0xD6,0xDA,0xDE); PAPER=(0xF4,0xF3,0xEE)
TEAL=(0x0E,0x7C,0x94); GRN=(0x2F,0x6B,0x4F); AMBER=(0xE8,0xA8,0x3E)

BLESS = {
 "image1":"山高水长 · 护你周全","image2":"生生不息 · 代代长久","image3":"风调雨顺 · 岁岁安稳",
 "image4":"蝶自飞来 · 有情成双","image5":"五谷丰登 · 家宅安宁","image6":"无畏向前 · 路自宽阔",
 "image7":"花开辟邪 · 一路平安","image8":"稚子安睡 · 家有新枝","image9":"慢慢来 · 长长久久",
 "image10":"有它守门 · 家宅无忧","image11":"心事有解 · 良人常伴","image12":"年年有余 · 岁岁丰足",
 "image13":"所遇皆吉 · 所愿皆成","image14":"多子多福 · 雨水丰沛","image15":"根在此处 · 行必有归",
}
ALL = list(BLESS)

def glyph(k, size, color, pad=.10):
    m = np.array(Image.open(f"{T}/{k}.png").convert("L")) > 127
    h, w = m.shape; box = int(size*(1-pad*2)); sc = min(box/w, box/h)
    im = Image.fromarray((m*255).astype("uint8")).resize(
        (max(1,int(w*sc)), max(1,int(h*sc))), Image.LANCZOS)
    L = Image.new("RGBA",(size,size),(0,0,0,0))
    L.paste(Image.new("RGBA",im.size,color+(255,)),((size-im.width)//2,(size-im.height)//2),im)
    return L

def rr(sz, fill, r=14, outline=None, w=0):
    c = Image.new("RGBA", sz, (0,0,0,0))
    ImageDraw.Draw(c).rounded_rectangle([0,0,sz[0]-1,sz[1]-1], r, fill=fill, outline=outline, width=w)
    return c

def band(w, h, keys, ground=NAVY, cols=(CREAM,RED,(0x6E,0x9A,0xC4)), rows=2):
    b = Image.new("RGBA",(w,h),ground+(255,)); rh=h/rows
    for r in range(rows):
        k=keys[r%len(keys)]; c=cols[r%len(cols)]; cell=int(rh*.84)
        n=max(2,int(w/(cell*1.15))); step=w/n
        for i in range(n):
            g=glyph(k,cell,c,pad=.14)
            b.alpha_composite(g,(int(i*step+(step-cell)/2), int(r*rh+(rh-cell)/2)))
    return b

def header(d,t,sub,pad=44):
    d.text((pad,32),t,font=font(30,True),fill=INK)
    d.text((pad,74),sub,font=font(14),fill=MUT)


# ── V6-1：依博物馆参考设计的五款新 SKU ─────────────────────
def museum_skus(path):
    CW, pad, gap, head = 286, 44, 20, 116
    C = 5; W = pad*2+CW*C+gap*(C-1); H = head+CW+96+pad
    im = Image.new("RGB",(W,H),(0xFA,0xFA,0xF8)); d = ImageDraw.Draw(im)
    header(d,"依国博参考新增的五款 SKU",
      "取自贵司提供的国博/敦煌店在售形态。左起第一款最贴近本项目——那件文物本身就是汉代织锦，与黎锦同类。")
    y = head
    items = [
      ("木质滑动亮灯冰箱贴","汉代织锦护臂的同构做法 · 拉动换景","slide"),
      ("十五式图腾格册","生肖玲珑杯的格子构成 · 可作杯/贴纸/集章卡","grid"),
      ("陶瓷杯垫 · 放射纹章","国博杯垫的花瓣构图 · 每瓣一腾","medal"),
      ("织锦折扇","海南气候实用 · 扇面为纹样带","fan"),
      ("纸雕小夜灯","分层透光 · 船型屋剪影","lamp"),
    ]
    for i,(nm,desc,kind) in enumerate(items):
        x = pad+i*(CW+gap)
        t = rr((CW,CW),(0xFF,0xFF,0xFF,255),16,outline=(0xE1,0xE4,0xDD,255),w=2)
        dd = ImageDraw.Draw(t); c = CW//2
        if kind=="slide":
            t.alpha_composite(rr((CW-52,CW-96),WOOD+(255,),10),(26,44))
            t.alpha_composite(rr((CW-84,CW-140),DEEP+(255,),6),(42,66))
            bb = band(CW-84,CW-140,["image12","image4","image9"],ground=DEEP,
                      cols=(AMBER,CREAM,RED),rows=3)
            t.alpha_composite(bb,(42,66))
            dd.rounded_rectangle([42,66,CW-43,CW-75],6,outline=GOLD+(255,),width=2)
            for ax,ar in ((30,180),(CW-31,0)):
                dd.polygon([(ax,c),(ax+(12 if ar else -12),c-9),(ax+(12 if ar else -12),c+9)],
                           fill=RED+(255,))
            dd.text((c-42,CW-64),"← 滑动 →",font=font(13,True),fill=WOOD2)
        elif kind=="grid":
            PADX, TOP, BOT = 20, 26, 46          # 卡内可用区，避免溢出卡片
            t.alpha_composite(rr((CW-PADX*2, CW-TOP-BOT), DEEP+(255,), 8), (PADX, TOP))
            cols_, rows_ = 4, 3
            gw, gh = CW-PADX*2-16, CW-TOP-BOT-40
            cell = min(gw//cols_, gh//rows_)
            ox = PADX + (CW-PADX*2 - cell*cols_)//2
            oy = TOP + 10
            for j,k in enumerate(ALL[:cols_*rows_]):
                r_,c_ = divmod(j, cols_)
                col=[CREAM,AMBER,RED,(0x8C,0xA9,0xC4)][j%4]
                cimg = rr((cell-4,cell-4),(0x1E,0x36,0x58,255),4)
                cimg.alpha_composite(glyph(k,cell-4,col,pad=.18))
                t.alpha_composite(cimg,(ox+c_*cell, oy+r_*cell))
            dd.text((PADX+8, oy+rows_*cell+8), "十五式 · 集齐成册", font=font(13), fill=CREAM)
        elif kind=="medal":
            R=104
            dd.ellipse([c-R,c-R,c+R,c+R],fill=(0xF6,0xEE,0xE2,255),outline=NAVY+(255,),width=3)
            dd.ellipse([c-34,c-34,c+34,c+34],fill=NAVY+(255,))
            t.alpha_composite(glyph("image4",64,CREAM,pad=.08),(c-32,c-32))
            import math
            for j in range(8):
                ang=math.radians(j*45-90); rx=c+int(math.cos(ang)*66); ry=c+int(math.sin(ang)*66)
                dd.ellipse([rx-27,ry-27,rx+27,ry+27],fill=(0xE6,0xDC,0xC8,255),outline=NAVY+(180,),width=2)
                t.alpha_composite(glyph(ALL[j],48,NAVY,pad=.12),(rx-24,ry-24))
        elif kind=="fan":
            import math
            dd.pieslice([c-118,c-70,c+118,c+166],200,340,fill=DEEP+(255,))
            dd.pieslice([c-40,c+8,c+40,c+88],200,340,fill=(0xFF,0xFF,0xFF,255))
            for j in range(9):
                ang=math.radians(200+j*17.5)
                dd.line([c+int(math.cos(ang)*38),c+48+int(math.sin(ang)*38),
                         c+int(math.cos(ang)*116),c+48+int(math.sin(ang)*116)],
                        fill=(0x2A,0x3E,0x5E,255),width=2)
            for j,k in enumerate(["image11","image4","image13"]):
                ang=math.radians(228+j*42)
                gx=c+int(math.cos(ang)*80); gy=c+48+int(math.sin(ang)*80)
                t.alpha_composite(glyph(k,48,AMBER,pad=.10),(gx-24,gy-24))
            dd.rounded_rectangle([c-16,c+92,c+16,c+128],4,fill=WOOD2+(255,))
        else:
            dd.polygon([(c-72,CW-58),(c+72,CW-58),(c+52,c-52),(c-52,c-52)],fill=(0xF6,0xE7,0xC8,255))
            for j,al in enumerate([90,150,210]):
                dd.polygon([(c-72+j*48,CW-58),(c-40+j*48,CW-58),(c-30+j*40,c-52),(c-52+j*40,c-52)],
                           fill=(0xE8,0xC9,0x8E,255) if j%2 else (0xF2,0xDD,0xB4,255))
            t.alpha_composite(glyph("image1",96,(0x6B,0x4A,0x22),pad=.06),(c-48,c-6))
            dd.rounded_rectangle([c-84,CW-58,c+84,CW-40],5,fill=(0xD8,0xD2,0xC4,255))
            dd.ellipse([c-10,c-72,c+10,c-52],fill=AMBER+(255,))
        im.paste(t,(x,y),t)
        d.text((x,y+CW+12),nm,font=font(16,True),fill=INK)
        d.text((x,y+CW+38),desc,font=font(12),fill=MUT)
    im.save(path,quality=92); print("  ok",os.path.basename(path),im.size)


# ── V6-2：全线产品接触表（本次提案的完整 SKU 一览）─────────
def contact_sheet(path):
    CW, pad, gap, head = 210, 44, 16, 132
    rowsdef = [
      ("引流款 · 零售 19-39 元", [
        ("图腾外形冰箱贴","亚克力模切 · 3 纹样","magnet_cut"),
        ("木质开门冰箱贴","300 起 · 唯一带机关","magnet_door"),
        ("亚克力挂绳","3 款 · 同模","strap"),
        ("异形贴纸套装","一版多腾 · 免开模","sticker"),
        ("明信片 / 票根卡","白查十二时插画","postcard"),
      ]),
      ("主力款 · 零售 29-69 元", [
        ("陶瓷杯垫","放射纹章 · 4 款","coaster"),
        ("本色帆布袋","丝网印 · 不覆膜","tote"),
        ("集章卡 + 印章","分设景点 · 带动全程","stamp"),
        ("织锦折扇","扇面纹样带","fanmini"),
        ("木质滑动亮灯冰箱贴","镇店 · 拉动换景","slidemini"),
      ]),
    ]
    C = 5
    W = pad*2+CW*C+gap*(C-1)
    H = head + len(rowsdef)*(CW+78) + pad + 20
    im = Image.new("RGB",(W,H),(0xFA,0xFA,0xF8)); d = ImageDraw.Draw(im)
    header(d,"本次提案的完整 SKU 一览",
      "两档十款。全部使用贵司原稿图腾，零售价全部落在 19-69 元区间。★ 为本轮依国博参考新增。")
    y = head
    for title, items in rowsdef:
        d.text((pad, y-26), title, font=font(16), fill=RED)
        for i,(nm,desc,kind) in enumerate(items):
            x = pad+i*(CW+gap)
            t = rr((CW,CW),(0xFF,0xFF,0xFF,255),12,outline=(0xE4,0xE7,0xE0,255),w=2)
            dd = ImageDraw.Draw(t); c = CW//2
            if kind=="magnet_cut":
                t.alpha_composite(glyph("image14",CW-40,CREAM,pad=.04),(20,20))
                t.alpha_composite(glyph("image14",CW-56,NAVY,pad=.04),(28,28))
            elif kind=="magnet_door":
                dd.rounded_rectangle([34,42,CW-35,CW-42],8,fill=WOOD+(255,))
                dd.rectangle([c-34,58,c+34,CW-58],fill=DEEP+(255,))
                t.alpha_composite(glyph("image1",58,AMBER,pad=.04),(c-29,c-30))
                for sg in (-1,1):
                    dd.polygon([(c+sg*36,56),(c+sg*62,50),(c+sg*62,CW-52),(c+sg*36,CW-58)],
                               fill=(0x2C,0x4D,0x74,255),outline=CREAM+(200,))
            elif kind=="strap":
                for j,(k,col) in enumerate(zip(["image9","image4","image12"],[NAVY,TEAL,GRN])):
                    dd.rounded_rectangle([28+j*56,52,68+j*56,CW-70],6,fill=col+(255,))
                    t.alpha_composite(glyph(k,40,CREAM,pad=.14),(28+j*56,c-34))
                    dd.line([48+j*56,52,48+j*56,34],fill=(0xC0,0xC6,0xBE,255),width=3)
            elif kind=="sticker":
                dd.rounded_rectangle([22,26,CW-23,CW-26],8,fill=PAPER+(255,),outline=(0xD2,0xD6,0xCF,255),width=2)
                for j,k in enumerate(ALL[:6]):
                    r_,c_=divmod(j,3); col=[NAVY,RED,GRN,TEAL,GOLD,NAVY][j]
                    t.alpha_composite(glyph(k,50,col,pad=.14),(32+c_*50,48+r_*62))
            elif kind=="postcard":
                for j,off in enumerate([(26,44),(44,32),(62,20)]):
                    dd.rounded_rectangle([off[0],off[1],off[0]+104,off[1]+76],5,
                        fill=[(0xF6,0xE9,0xD2,255),(0xE9,0xF0,0xE4,255),(0xDE,0xEC,0xEF,255)][j],
                        outline=(0xD2,0xD6,0xCF,255),width=2)
                t.alpha_composite(glyph("image6",90,NAVY,pad=.10),(66,26))
            elif kind=="coaster":
                import math
                R=76; dd.ellipse([c-R,c-R,c+R,c+R],fill=(0xF6,0xEE,0xE2,255),outline=NAVY+(255,),width=3)
                dd.ellipse([c-24,c-24,c+24,c+24],fill=NAVY+(255,))
                t.alpha_composite(glyph("image4",46,CREAM,pad=.08),(c-23,c-23))
                for j in range(6):
                    ang=math.radians(j*60-90); rx=c+int(math.cos(ang)*48); ry=c+int(math.sin(ang)*48)
                    t.alpha_composite(glyph(ALL[j],34,NAVY,pad=.10),(rx-17,ry-17))
            elif kind=="tote":
                dd.arc([c-42,26,c+42,90],195,345,fill=(0xC9,0xC2,0xB2,255),width=8)
                dd.rounded_rectangle([34,56,CW-35,CW-30],8,fill=(0xEA,0xE6,0xDA,255))
                bb=band(CW-90,52,["image11","image4"],ground=NAVY,cols=(CREAM,RED),rows=2)
                t.alpha_composite(bb,(45,c-6))
            elif kind=="stamp":
                dd.rounded_rectangle([20,40,CW-70,CW-40],6,fill=PAPER+(255,),outline=NAVY+(255,),width=2)
                for j,k in enumerate(["image14","image12","image9","image4"]):
                    r_,c_=divmod(j,2)
                    dd.rectangle([32+c_*50,54+r_*52,32+c_*50+40,54+r_*52+40],outline=(0xC0,0xC6,0xBE,255),width=2)
                    if j<2: t.alpha_composite(glyph(k,40,RED,pad=.14),(32+c_*50,54+r_*52))
                dd.rounded_rectangle([CW-62,58,CW-28,CW-72],5,fill=WOOD2+(255,))
                dd.rounded_rectangle([CW-66,CW-72,CW-24,CW-48],4,fill=NAVY+(255,))
            elif kind=="fanmini":
                import math
                dd.pieslice([c-84,c-52,c+84,c+116],200,340,fill=DEEP+(255,))
                for j in range(7):
                    ang=math.radians(203+j*22)
                    dd.line([c+int(math.cos(ang)*26),c+34+int(math.sin(ang)*26),
                             c+int(math.cos(ang)*82),c+34+int(math.sin(ang)*82)],
                            fill=(0x2A,0x3E,0x5E,255),width=2)
                for j,k in enumerate(["image11","image13"]):
                    ang=math.radians(238+j*64)
                    t.alpha_composite(glyph(k,38,AMBER,pad=.10),
                                      (c+int(math.cos(ang)*58)-19, c+34+int(math.sin(ang)*58)-19))
                dd.rounded_rectangle([c-12,c+64,c+12,c+92],3,fill=WOOD2+(255,))
            else:
                t.alpha_composite(rr((CW-46,CW-76),WOOD+(255,),8),(23,38))
                bb=band(CW-72,CW-108,["image12","image4"],ground=DEEP,cols=(AMBER,CREAM),rows=2)
                t.alpha_composite(bb,(36,54))
                dd.rounded_rectangle([36,54,CW-37,CW-56],4,outline=GOLD+(255,),width=2)
                dd.text((c-30,CW-52),"← 滑动 →",font=font(11,True),fill=WOOD2)
            im.paste(t,(x,y),t)
            star = " ★" if kind in ("stamp","fanmini","slidemini","sticker") else ""
            d.text((x,y+CW+9), nm+star, font=font(14,True), fill=INK)
            d.text((x,y+CW+31), desc, font=font(11), fill=MUT)
        y += CW+78
    im.save(path,quality=92); print("  ok",os.path.basename(path),im.size)


os.makedirs(os.path.join(HERE,"assets/v6"), exist_ok=True)
museum_skus(os.path.join(HERE,"assets/v6/v6_museum_skus.jpg"))
contact_sheet(os.path.join(HERE,"assets/v6/v6_contact_sheet.jpg"))
