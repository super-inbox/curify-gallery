# -*- coding: utf-8 -*-
"""冰箱贴专题图：真实图腾 × 配色 / 机关工艺示意。
纹样全部取自 assets/totem-lib（客户原稿矢量），无生成式模型参与。"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, "assets/totem-lib/mask")
META = json.load(open(f"{T}/meta.json"))
FZ = "/System/Library/Fonts/STHeiti Medium.ttc"
FS = "/System/Library/Fonts/Supplemental/Songti.ttc"
def font(s, serif=False): return ImageFont.truetype(FS if serif else FZ, s)

def mask(key):
    return np.array(Image.open(f"{T}/{key}.png").convert("L")) > 127

def glyph(key, size, color, pad=.10):
    m = mask(key); h, w = m.shape
    box = int(size*(1-pad*2)); sc = min(box/w, box/h)
    im = Image.fromarray((m*255).astype("uint8")).resize(
        (max(1,int(w*sc)), max(1,int(h*sc))), Image.LANCZOS)
    L = Image.new("RGBA", (size, size), (0,0,0,0))
    L.paste(Image.new("RGBA", im.size, color+(255,)), ((size-im.width)//2, (size-im.height)//2), im)
    return L

def rr(size, fill, r=14, outline=None, w=0):
    c = Image.new("RGBA", size, (0,0,0,0))
    ImageDraw.Draw(c).rounded_rectangle([0,0,size[0]-1,size[1]-1], r, fill=fill, outline=outline, width=w)
    return c

INK=(0x14,0x20,0x2B); MUT=(0x8A,0x92,0x99); SUB=(0x38,0x43,0x4E)
WAYS=[("A 墨蓝本白",(0x1E,0x3A,0x5F),(0xF2,0xF0,0xE8)),
      ("B 浅底反转",(0xF4,0xF3,0xEE),(0x16,0x2B,0x45)),
      ("C 海岛明快",(0x0E,0x7C,0x94),(0xFF,0x7A,0x59)),
      ("D 椰林清新",(0xED,0xF0,0xE8),(0x2F,0x6B,0x4F)),
      ("E 暖阳撞色",(0x14,0x20,0x2B),(0xF2,0xB1,0x2E))]

# ── 1. 图腾外形模切 × 五配色 ───────────────────────────────
def sheet_diecut(path):
    KEYS=["image14","image11","image12","image4","image9"]   # 蛙 鸟 鱼 蝴蝶 龟
    CW,pad,gap,head,RAIL=190,44,14,108,180
    W=pad*2+RAIL+CW*len(KEYS)+gap*(len(KEYS)-1)
    H=head+30+len(WAYS)*(CW+gap)+pad
    im=Image.new("RGB",(W,H),(0xFA,0xFA,0xF8)); d=ImageDraw.Draw(im)
    d.text((pad,32),"冰箱贴 · 图腾外形模切 × 五配色",font=font(30,True),fill=INK)
    d.text((pad,74),"刀线沿图腾轮廓走，产品本身即图腾。同一副刀模可出多个纹样，不额外增加起订量。",
           font=font(14),fill=MUT)
    for i,k in enumerate(KEYS):
        d.text((pad+RAIL+i*(CW+gap),head+4),META[k]["name"],font=font(13),fill=MUT)
    y=head+30
    for label,bg,ink in WAYS:
        d.text((pad,y+CW//2-10),label,font=font(17,True),fill=INK)
        for i,k in enumerate(KEYS):
            x=pad+RAIL+i*(CW+gap)
            tile=Image.new("RGBA",(CW,CW),(0,0,0,0))
            tile.alpha_composite(glyph(k,int(CW*.98),bg,pad=.05),(int(CW*.01),int(CW*.01)))  # 白边
            tile.alpha_composite(glyph(k,int(CW*.86),ink,pad=.05),(int(CW*.07),int(CW*.07)))
            im.paste(tile,(x,y),tile)
        y+=CW+gap
    im.save(path,quality=92); print(f"  ✓ {os.path.basename(path)} {im.size}")

# ── 2. 机关工艺示意 ───────────────────────────────────────
def sheet_mech(path):
    CW,pad,gap,head=286,44,20,112
    items=["转","门","滑","层"]
    W=pad*2+CW*4+gap*3; H=head+CW+92+pad
    im=Image.new("RGB",(W,H),(0xFA,0xFA,0xF8)); d=ImageDraw.Draw(im)
    d.text((pad,32),"冰箱贴 · 四种机关（工厂现有工艺）",font=font(30,True),fill=INK)
    d.text((pad,74),"从「一张贴片」变成「有动作的小物」。这是把客单价从 ¥19 抬到 ¥35–49 的关键，也是最不像旅游纪念品的做法。",
           font=font(14),fill=MUT)
    BG,ACC=(0xF2,0xF0,0xE8),(0x1E,0x3A,0x5F)
    ORG=(0xFF,0x7A,0x59)
    for i,kind in enumerate(items):
        x=pad+i*(CW+gap); y=head
        t=rr((CW,CW),(0xFF,0xFF,0xFF,255),18,outline=(0xE1,0xE4,0xDD,255),w=2)
        dd=ImageDraw.Draw(t); c=CW//2
        if kind=="转":   # 外圈固定 + 内盘转动，窗口换图腾
            dd.ellipse([26,26,CW-27,CW-27],fill=ACC+(255,))
            dd.ellipse([54,54,CW-55,CW-55],fill=BG+(255,))
            t.alpha_composite(glyph("image14",CW-140,ACC,pad=.02),(70,70))
            for a,lab in ((-52,"蛙"),(52,"鸟")):
                pass
            dd.arc([16,16,CW-17,CW-17],200,340,fill=ORG+(255,),width=6)
            dd.polygon([(CW-46,44),(CW-28,52),(CW-44,64)],fill=ORG+(255,))
        elif kind=="门": # 船型屋对开门，半开露出大力神
            dd.rounded_rectangle([30,86,CW-31,CW-52],10,fill=ACC+(255,))
            dd.pieslice([30,44,CW-31,150],180,360,fill=(0xB4,0x76,0x3C,255))
            # 内腔与大力神（先画，门后盖）
            dd.rectangle([c-46,102,c+46,CW-58],fill=(0x0E,0x1B,0x2C,255))
            t.alpha_composite(glyph("image1",84,(0xF2,0xF0,0xE8),pad=.02),(c-42,108))
            # 两扇半开的门：外侧窄、内侧留出缝
            for sgn in (-1,1):
                x0=c+sgn*48; x1=c+sgn*(c-34)
                dd.polygon([(min(x0,x1),102),(max(x0,x1),94),
                            (max(x0,x1),CW-50),(min(x0,x1),CW-58)],
                           fill=(0x2C,0x4D,0x74,255),outline=BG+(255,))
            dd.arc([c-74,c-30,c-30,c+14],250,20,fill=ORG+(255,),width=4)
            dd.arc([c+30,c-30,c+74,c+14],160,290,fill=ORG+(255,),width=4)
        elif kind=="滑": # 抽拉露出寓意文字
            dd.rounded_rectangle([34,72,CW-35,CW-72],10,fill=ACC+(255,))
            t.alpha_composite(glyph("image12",92,BG,pad=.02),(46,c-46))
            dd.rounded_rectangle([c+6,80,CW-42,CW-80],8,fill=BG+(255,))
            dd.text((c+22,c-24),"年年",font=font(20,True),fill=ACC)
            dd.text((c+22,c+2),"有余",font=font(20,True),fill=ACC)
            dd.line([CW-52,c-40,CW-52,c+40],fill=ORG+(255,),width=5)
            dd.polygon([(CW-40,c),(CW-22,c-10),(CW-22,c+10)],fill=ORG+(255,))
        else:            # 双层磁吸：前层镂空，后层撞色
            dd.rounded_rectangle([64,52,CW-34,CW-84],10,fill=ORG+(255,))
            back=Image.new("RGBA",(CW,CW),(0,0,0,0))
            fr=rr((CW-98,CW-136),ACC+(255,),10)
            m=glyph("image7",CW-136,(0,0,0),pad=.14).split()[3]
            hole=Image.new("RGBA",fr.size,(0,0,0,0))
            hole.paste(Image.new("RGBA",(CW-136,CW-136),(0,0,0,0)),(0,0))
            fr.paste((0,0,0,0),(6,0),m)
            back.alpha_composite(fr,(34,84))
            t.alpha_composite(back)
        im.paste(t,(x,y),t)
        titles={"转":("转转冰箱贴","转动内盘，窗口依次显示不同图腾"),
                "门":("对开门冰箱贴","船型屋外形，开门露出大力神"),
                "滑":("滑轨冰箱贴","抽拉露出该图腾的吉祥寓意"),
                "层":("双层磁吸","前层镂空图腾，后层撞色透出")}
        nm,desc=titles[kind]
        d.text((x,y+CW+14),nm,font=font(17,True),fill=INK)
        d.text((x,y+CW+40),desc,font=font(13),fill=MUT)
    im.save(path,quality=92); print(f"  ✓ {os.path.basename(path)} {im.size}")

os.makedirs(os.path.join(HERE,"assets/v3"),exist_ok=True)
sheet_diecut(os.path.join(HERE,"assets/v3/v3_magnet_diecut.jpg"))
sheet_mech(os.path.join(HERE,"assets/v3/v3_magnet_mech.jpg"))
