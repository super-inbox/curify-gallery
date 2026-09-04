# -*- coding: utf-8 -*-
"""V7：带祝福语的版本（与无字版并存，不替换）。

难点：图腾外形模切后产品轮廓即图腾，没有平面留白放字。
故给出三种加字方式，而不是只挑一种。
"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np, json, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, "assets/totem-lib/mask")
FZ = "/System/Library/Fonts/STHeiti Medium.ttc"
FS = "/System/Library/Fonts/Supplemental/Songti.ttc"
def font(s, serif=False): return ImageFont.truetype(FS if serif else FZ, s)

INK=(0x14,0x20,0x2B); MUT=(0x8A,0x92,0x99)
NAVY=(0x16,0x2B,0x45); DEEP=(0x0F,0x1E,0x38); CREAM=(0xF2,0xF0,0xE8)
GOLD=(0xC8,0x95,0x2E); RED=(0xC2,0x35,0x2C); WOOD=(0xA8,0x7C,0x50)
WOOD2=(0x8B,0x62,0x3C); PAPER=(0xF4,0xF3,0xEE); TEAL=(0x0E,0x7C,0x94)
GRN=(0x2F,0x6B,0x4F); AMBER=(0xE8,0xA8,0x3E); SILVER=(0xD6,0xDA,0xDE)

BLESS = {
 "image1":("大力神","山高水长","护你周全"),   "image4":("蝴蝶图腾","蝶自飞来","有情成双"),
 "image7":("狗牙花图腾","花开辟邪","一路平安"),"image9":("龟图腾","慢慢来","长长久久"),
 "image11":("鸟图腾","心事有解","良人常伴"), "image12":("鱼图腾","年年有余","岁岁丰足"),
 "image13":("鹿图腾","所遇皆吉","所愿皆成"), "image14":("蛙图腾","多子多福","雨水丰沛"),
}

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

def vtext(layer, xy, text, f, fill, gap=3):
    """竖排：逐字堆叠。中文最自然的加字方式，也最省宽度。"""
    d = ImageDraw.Draw(layer); x, y = xy
    for ch in text:
        b = d.textbbox((0,0), ch, font=f)
        d.text((x - (b[2]-b[0])//2, y), ch, font=f, fill=fill)
        y += (b[3]-b[1]) + gap + 4
    return y

def arctext(layer, cx, cy, r, text, f, fill, start=-90, span=140):
    """弧排：沿圆周排字，用于圆形器物。"""
    n = max(1, len(text)-1)
    for i, ch in enumerate(text):
        a = math.radians(start - span/2 + (span*i/n if n else 0))
        ci = Image.new("RGBA", (f.size*2, f.size*2), (0,0,0,0))
        ImageDraw.Draw(ci).text((f.size//2, f.size//2), ch, font=f, fill=fill)
        ci = ci.rotate(-math.degrees(a)-90, resample=Image.BICUBIC, expand=False)
        layer.alpha_composite(ci, (int(cx+math.cos(a)*r)-f.size, int(cy+math.sin(a)*r)-f.size))

def seal(layer, xy, ch, size=26):
    """印章式小方块，作点睛。"""
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle([xy[0],xy[1],xy[0]+size,xy[1]+size],3,fill=RED+(255,))
    f = font(int(size*0.62), True)
    b = d.textbbox((0,0),ch,font=f)
    d.text((xy[0]+(size-(b[2]-b[0]))//2-b[0], xy[1]+(size-(b[3]-b[1]))//2-b[1]), ch, font=f, fill=CREAM)

def header(d,t,sub,pad=44):
    d.text((pad,32),t,font=font(30,True),fill=INK)
    d.text((pad,74),sub,font=font(14),fill=MUT)


# ── 1. 图腾外形模切：三种加字方式 × 配色 ────────────────────
def diecut_text(path):
    CW, pad, gap, head = 268, 44, 20, 118
    ways = [
      ("① 底座条","图腾下接一条刀模底座，横排四字。单件模切，成本不变。","base"),
      ("② 竖排侧栏","图腾偏左，右侧竖排八字 + 朱印。最像传统器物。","side"),
      ("③ 图腾纯粹 · 字在背卡","磁贴本体不加字，祝福语印在背卡上。保图腾完整。","card"),
    ]
    ways = ways * 1
    cols = [("A 墨蓝本白",NAVY,CREAM,GOLD),("C 海岛明快",TEAL,CREAM,AMBER),("E 暖阳撞色",DEEP,AMBER,CREAM)]
    W = pad*2 + CW*3 + gap*2
    H = head + len(ways)*(CW+80) + pad
    im = Image.new("RGB",(W,H),(0xFA,0xFA,0xF8)); d = ImageDraw.Draw(im)
    header(d,"图腾外形模切 · 加祝福语的三种做法",
      "图腾即外形之后本体没有留白，所以加字有三条路。无字版保留，以下为可选的加字版。")
    keys = ["image14","image12","image11"]
    y = head
    for wi,(wn,wd,kind) in enumerate(ways):
        for ci,(cn,bg,ink,acc) in enumerate(cols):
            x = pad+ci*(CW+gap); k = keys[ci]
            nm, l1, l2 = BLESS[k]
            t = rr((CW,CW),(0xFF,0xFF,0xFF,255),12,outline=(0xE6,0xE9,0xE2,255),w=2)
            dd = ImageDraw.Draw(t); c = CW//2
            if kind=="base":
                # 白卡上必须用深色描图腾；ink 是给深底用的浅色
                t.alpha_composite(glyph(k,CW-92,bg,pad=.04),(c-(CW-92)//2,26))
                dd.rounded_rectangle([c-84,CW-84,c+84,CW-38],8,fill=bg+(255,))
                dd.rounded_rectangle([c-80,CW-80,c+80,CW-42],6,outline=acc+(180,),width=1)
                f=font(21,True); b=dd.textbbox((0,0),l1,font=f)
                dd.text((c-(b[2]-b[0])//2,CW-76),l1,font=f,fill=ink)
            elif kind=="side":
                t.alpha_composite(glyph(k,CW-110,bg,pad=.04),(24,40))
                dd.line([CW-96,34,CW-96,CW-34],fill=bg+(120,),width=2)
                # 中文竖排右起：第一句在最右
                vtext(t,(CW-42,40),l1,font(20,True),bg)
                vtext(t,(CW-72,40),l2,font(20,True),MUT)
                seal(t,(CW-58,CW-70),"福",24)
            else:
                dd.rounded_rectangle([16,16,CW-17,CW-17],10,fill=(0xED,0xE7,0xD6,255))
                dd.text((30,30),"海南黎族织锦",font=font(13,True),fill=NAVY)
                f=font(19,True)
                dd.text((30,CW-72),l1,font=f,fill=RED)
                dd.text((30,CW-46),l2,font=f,fill=RED)
                t.alpha_composite(glyph(k,CW-104,acc,pad=.04),(c-14,38))
                t.alpha_composite(glyph(k,CW-116,bg,pad=.04),(c-8,44))
            im.paste(t,(x,y),t)
            if ci==0:
                d.text((x,y+CW+10),wn,font=font(17,True),fill=INK)
                d.text((x,y+CW+36),wd,font=font(12),fill=MUT)
            else:
                d.text((x,y+CW+10),cn+" · "+nm,font=font(13),fill=MUT)
        y += CW+80
    im.save(path,quality=92); print("  ok",os.path.basename(path),im.size)


# ── 2. 四种机关：祝福语作为"被揭开"的内容 ───────────────────
def mech_text(path):
    CW, pad, gap, head = 292, 44, 20, 118
    W = pad*2+CW*4+gap*3; H = head+CW+96+pad
    im = Image.new("RGB",(W,H),(0xFA,0xFA,0xF8)); d = ImageDraw.Draw(im)
    header(d,"四种机关 · 把祝福语变成「被揭开的那句话」",
      "机关款加字最自然：字不是印在表面，而是转开/拉开/推开之后才出现——动作本身成了仪式。")
    y = head
    specs = [("转转","转动内盘，窗口依次显示图腾与对应祝福","rot"),
             ("对开门","推开门，里面是祖先纹与那句话","door"),
             ("滑轨","抽出即是这一式的祝福语","slide"),
             ("双层磁吸","前层镂空图腾，后层透出朱字","layer")]
    for i,(nm,desc,kind) in enumerate(specs):
        x = pad+i*(CW+gap); c = CW//2
        t = rr((CW,CW),(0xFF,0xFF,0xFF,255),16,outline=(0xE1,0xE4,0xDD,255),w=2)
        dd = ImageDraw.Draw(t)
        if kind=="rot":
            # 外圈固定深色，中央转盘开窗；窗内是图腾 + 该式祝福。
            # 弧排在窄环带上易倒字，改为窗口内直排，最稳。
            dd.ellipse([24,24,CW-25,CW-25],fill=NAVY+(255,))
            dd.ellipse([46,46,CW-47,CW-47],fill=CREAM+(255,))
            dd.ellipse([46,46,CW-47,CW-47],outline=AMBER+(255,),width=2)
            t.alpha_composite(glyph("image14",96,NAVY,pad=.02),(c-48,72))
            f=font(19,True)
            for li,ln in enumerate(("多子多福","雨水丰沛")):
                bb=dd.textbbox((0,0),ln,font=f)
                dd.text((c-(bb[2]-bb[0])//2, 176+li*26), ln, font=f,
                        fill=NAVY if li==0 else MUT)
            dd.arc([14,14,CW-15,CW-15],196,344,fill=AMBER+(255,),width=5)
            dd.polygon([(CW-46,40),(CW-26,49),(CW-44,61)],fill=AMBER+(255,))
            dd.text((34,CW-40),"转动内盘换下一式",font=font(12),fill=MUT)
        elif kind=="door":
            dd.rounded_rectangle([28,84,CW-29,CW-50],10,fill=NAVY+(255,))
            dd.pieslice([28,42,CW-29,148],180,360,fill=WOOD+(255,))
            dd.rectangle([c-46,100,c+46,CW-56],fill=DEEP+(255,))
            t.alpha_composite(glyph("image1",70,CREAM,pad=.02),(c-35,104))
            f=font(16,True)
            dd.text((c-32,CW-92),"护你周全",font=f,fill=AMBER)
            for sg in (-1,1):
                x0=c+sg*48; x1=c+sg*(c-30)
                dd.polygon([(min(x0,x1),100),(max(x0,x1),92),(max(x0,x1),CW-48),(min(x0,x1),CW-56)],
                           fill=(0x2C,0x4D,0x74,255),outline=CREAM+(200,))
        elif kind=="slide":
            dd.rounded_rectangle([30,70,CW-31,CW-70],10,fill=NAVY+(255,))
            t.alpha_composite(glyph("image12",84,CREAM,pad=.02),(44,c-42))
            dd.rounded_rectangle([c+4,78,CW-38,CW-78],8,fill=CREAM+(255,))
            f=font(22,True)
            dd.text((c+22,c-40),"年年",font=f,fill=NAVY)
            dd.text((c+22,c-10),"有余",font=f,fill=NAVY)
            seal(t,(c+26,c+26),"福",22)
            dd.polygon([(CW-34,c),(CW-16,c-10),(CW-16,c+10)],fill=AMBER+(255,))
        else:
            dd.rounded_rectangle([62,50,CW-24,CW-84],10,fill=RED+(255,))
            # 前层右边缘 = 30 + (CW-100)；文字必须落在它之外
            fx = 30 + (CW-100) + 8
            f=font(18,True)
            dd.text((fx,c-28),"心事",font=f,fill=CREAM)
            dd.text((fx,c-2),"有解",font=f,fill=CREAM)
            fr = rr((CW-100,CW-140),NAVY+(255,),10)
            m = glyph("image11",CW-140,(0,0,0),pad=.14).split()[3]
            fr.paste((0,0,0,0),(6,0),m)
            t.alpha_composite(fr,(30,84))
        im.paste(t,(x,y),t)
        d.text((x,y+CW+12),nm+"（加字版）",font=font(17,True),fill=INK)
        d.text((x,y+CW+38),desc,font=font(12),fill=MUT)
    im.save(path,quality=92); print("  ok",os.path.basename(path),im.size)


# ── 3. 其余 SKU 的加字版 ────────────────────────────────────
def sku_text(path):
    CW, pad, gap, head = 240, 44, 18, 118
    W = pad*2+CW*5+gap*4; H = head+CW+96+pad
    im = Image.new("RGB",(W,H),(0xFA,0xFA,0xF8)); d = ImageDraw.Draw(im)
    header(d,"其余 SKU 的加字版",
      "同一套祝福语铺到相关品类上。字全部竖排或弧排，配朱红小印，与织锦纹样带同版面。")
    y = head
    def frame():
        return rr((CW,CW),(0xFF,0xFF,0xFF,255),12,outline=(0xE6,0xE9,0xE2,255),w=2)
    # 杯垫：弧排
    t=frame(); dd=ImageDraw.Draw(t); c=CW//2
    dd.ellipse([26,26,CW-27,CW-27],fill=(0xF6,0xEE,0xE2,255),outline=NAVY+(255,),width=3)
    t.alpha_composite(glyph("image13",CW-158,NAVY,pad=.04),(79,72))
    arctext(t,c,c,c-44,"所遇皆吉",font(18,True),NAVY,start=-90,span=104)
    _f=font(17,True); _bb=ImageDraw.Draw(t).textbbox((0,0),"所愿皆成",font=_f)
    ImageDraw.Draw(t).text((c-(_bb[2]-_bb[0])//2, CW-84),"所愿皆成",font=_f,fill=RED)
    im.paste(t,(pad,y),t)
    # 挂绳：竖排
    t=frame(); dd=ImageDraw.Draw(t)
    for j,(k,col) in enumerate(zip(["image9","image4"],[NAVY,TEAL])):
        bx=48+j*84
        dd.rounded_rectangle([bx,40,bx+60,CW-30],8,fill=col+(255,))
        t.alpha_composite(glyph(k,52,CREAM,pad=.16),(bx+4,50))
        vtext(t,(bx+30,106),BLESS[k][1],font(15,True),CREAM,gap=1)
        dd.line([bx+30,40,bx+30,24],fill=(0xC0,0xC6,0xBE,255),width=3)
    im.paste(t,(pad+CW+gap,y),t)
    # 贴纸：每腾配四字
    t=frame(); dd=ImageDraw.Draw(t)
    dd.rounded_rectangle([20,26,CW-21,CW-26],8,fill=PAPER+(255,),outline=(0xD2,0xD6,0xCF,255),width=2)
    for j,k in enumerate(["image14","image12","image4","image11"]):
        r_,c_=divmod(j,2); bx=32+c_*98; by=44+r_*84
        col=[NAVY,RED,GRN,TEAL][j]
        t.alpha_composite(glyph(k,54,col,pad=.14),(bx,by))
        dd.text((bx-2,by+56),BLESS[k][1],font=font(13,True),fill=col)
    im.paste(t,(pad+2*(CW+gap),y),t)
    # 帆布袋：纹样带 + 竖排
    t=frame(); dd=ImageDraw.Draw(t); c=CW//2
    dd.arc([c-46,26,c+46,96],195,345,fill=(0xC9,0xC2,0xB2,255),width=9)
    dd.rounded_rectangle([34,60,CW-35,CW-28],8,fill=(0xEA,0xE6,0xDA,255))
    dd.rounded_rectangle([48,96,CW-92,CW-56],4,fill=NAVY+(255,))
    t.alpha_composite(glyph("image11",70,CREAM,pad=.12),(56,110))
    vtext(t,(CW-68,92),"心事有解",font(15,True),NAVY,gap=1)
    seal(t,(CW-80,CW-58),"福",20)
    im.paste(t,(pad+3*(CW+gap),y),t)
    # 明信片：竖排题款
    t=frame(); dd=ImageDraw.Draw(t)
    dd.rounded_rectangle([34,32,CW-35,CW-32],8,fill=(0xF6,0xE9,0xD2,255),outline=(0xD8,0xDC,0xD4,255),width=2)
    t.alpha_composite(glyph("image1",108,NAVY,pad=.06),(52,74))
    vtext(t,(CW-66,54),"山高水长",font(18,True),NAVY)
    vtext(t,(CW-96,54),"护你周全",font(18,True),MUT)
    seal(t,(CW-78,CW-72),"福",22)
    im.paste(t,(pad+4*(CW+gap),y),t)
    for i,(nm,desc) in enumerate([
        ("陶瓷杯垫","弧排环绕 · 上蓝下朱"),
        ("亚克力挂绳","竖排四字 · 窄面最省空间"),
        ("异形贴纸","每腾配四字 · 一版多句"),
        ("本色帆布袋","纹样带 + 竖排题款 + 朱印"),
        ("明信片 / 票根卡","双行竖排 · 留白最多")]):
        x = pad+i*(CW+gap)
        d.text((x,y+CW+12),nm,font=font(16,True),fill=INK)
        d.text((x,y+CW+38),desc,font=font(12),fill=MUT)
    im.save(path,quality=92); print("  ok",os.path.basename(path),im.size)


os.makedirs(os.path.join(HERE,"assets/v7"), exist_ok=True)
diecut_text(os.path.join(HERE,"assets/v7/v7_diecut_text.jpg"))
mech_text(os.path.join(HERE,"assets/v7/v7_mech_text.jpg"))
sku_text(os.path.join(HERE,"assets/v7/v7_sku_text.jpg"))
