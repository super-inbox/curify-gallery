# -*- coding: utf-8 -*-
"""冰箱贴其它形态 + 低成本印刷品。纹样全部取自客户原稿矢量。"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np, json, os
HERE=os.path.dirname(os.path.abspath(__file__)); T=os.path.join(HERE,"assets/totem-lib/mask")
META=json.load(open(f"{T}/meta.json"))
FZ="/System/Library/Fonts/STHeiti Medium.ttc"; FS="/System/Library/Fonts/Supplemental/Songti.ttc"
def font(s,serif=False): return ImageFont.truetype(FS if serif else FZ,s)
def glyph(k,size,color,pad=.10):
    m=np.array(Image.open(f"{T}/{k}.png").convert("L"))>127; h,w=m.shape
    box=int(size*(1-pad*2)); sc=min(box/w,box/h)
    im=Image.fromarray((m*255).astype("uint8")).resize((max(1,int(w*sc)),max(1,int(h*sc))),Image.LANCZOS)
    L=Image.new("RGBA",(size,size),(0,0,0,0))
    L.paste(Image.new("RGBA",im.size,color+(255,)),((size-im.width)//2,(size-im.height)//2),im); return L
def rr(sz,fill,r=14,outline=None,w=0):
    c=Image.new("RGBA",sz,(0,0,0,0)); ImageDraw.Draw(c).rounded_rectangle([0,0,sz[0]-1,sz[1]-1],r,fill=fill,outline=outline,width=w); return c
INK=(0x14,0x20,0x2B); MUT=(0x8A,0x92,0x99)
NAVY=(0x16,0x2B,0x45); CREAM=(0xF2,0xF0,0xE8); GOLD=(0xC8,0x95,0x2E)
TEAL=(0x0E,0x7C,0x94); ORG=(0xFF,0x7A,0x59); GRN=(0x2F,0x6B,0x4F); PAPER=(0xF4,0xF3,0xEE)

def header(d,t,sub,pad=44):
    d.text((pad,32),t,font=font(30,True),fill=INK); d.text((pad,74),sub,font=font(14),fill=MUT)

# ── 冰箱贴其它形态 ─────────────────────────────────────────
def magnet_shapes(path):
    CW,pad,gap,head=250,44,18,110
    C=5; W=pad*2+CW*C+gap*(C-1); H=head+CW+62+pad
    im=Image.new("RGB",(W,H),(0xFA,0xFA,0xF8)); d=ImageDraw.Draw(im)
    header(d,"冰箱贴 · 五种器形（图腾外形之外）",
      "参考太原北齐壁画博物馆店在售形态。方形深底款是博物馆主流——成本最低、最好陈列、也最不像旅游纪念品。")
    y=head
    specs=[
     ("圆角方形 · 主推","雷公款同形态，深底单腾 + 细金线","sq"),
     ("圆形徽章式","可做磁贴或胸针两用","ci"),
     ("票根式长方","仿门票，写景区名与日期","tk"),
     ("立牌式","可立可贴，兼作桌面摆件","st"),
     ("九宫格套装","一版九腾，收集感最强","gr"),
    ]
    keys=["image1","image14","image12","image7","image11"]
    for i,(nm,desc,kind) in enumerate(specs):
        x=pad+i*(CW+gap); t=Image.new("RGBA",(CW,CW),(0,0,0,0)); dd=ImageDraw.Draw(t)
        if kind=="sq":
            t.alpha_composite(rr((CW-24,CW-24),NAVY+(255,),18))
            dd.rounded_rectangle([32,32,CW-33,CW-33],12,outline=GOLD+(255,),width=2)
            t.alpha_composite(glyph(keys[i],CW-90,CREAM,pad=.04),(45,45))
        elif kind=="ci":
            dd.ellipse([12,12,CW-13,CW-13],fill=NAVY+(255,))
            dd.ellipse([30,30,CW-31,CW-31],outline=GOLD+(255,),width=2)
            t.alpha_composite(glyph(keys[i],CW-96,CREAM,pad=.04),(48,48))
        elif kind=="tk":
            box=[18,64,CW-19,CW-64]
            dd.rounded_rectangle(box,8,fill=CREAM+(255,),outline=NAVY+(255,),width=3)
            for yy in range(76,CW-76,14): dd.ellipse([box[0]-5,yy,box[0]+5,yy+8],fill=(0xFA,0xFA,0xF8,255))
            t.alpha_composite(glyph(keys[i],86,NAVY,pad=.04),(34,int(CW/2)-43))
            dd.line([CW-108,76,CW-108,CW-76],fill=NAVY+(200,),width=2)
            dd.text((CW-96,int(CW/2)-30),"白查村",font=font(17,True),fill=NAVY)
            dd.text((CW-96,int(CW/2)-4),"BAICHA",font=font(11),fill=MUT)
            dd.text((CW-96,int(CW/2)+16),"年年丰收",font=font(13),fill=GOLD)
        elif kind=="st":
            dd.polygon([(60,40),(CW-60,40),(CW-60,CW-64),(60,CW-64)],fill=NAVY+(255,))
            dd.pieslice([60,16,CW-60,64],180,360,fill=NAVY+(255,))
            t.alpha_composite(glyph(keys[i],CW-140,CREAM,pad=.04),(70,58))
            dd.rounded_rectangle([44,CW-64,CW-45,CW-46],4,fill=(0xC9,0xC2,0xB2,255))
        else:
            cell=(CW-30)//3
            for r in range(3):
                for c in range(3):
                    kk=["image14","image11","image12","image4","image9","image7","image5","image8","image15"][r*3+c]
                    bgc=[NAVY,TEAL,NAVY,GRN,NAVY,ORG,NAVY,GOLD,NAVY][r*3+c]
                    cellim=rr((cell-3,cell-3),bgc+(255,),6)
                    cellim.alpha_composite(glyph(kk,cell-3,CREAM,pad=.18))
                    t.alpha_composite(cellim,(15+c*cell,15+r*cell))
        im.paste(t,(x,y),t)
        d.text((x,y+CW+8),nm,font=font(16,True),fill=INK)
        d.text((x,y+CW+32),desc,font=font(12),fill=MUT)
    im.save(path,quality=92); print(f"  ✓ {os.path.basename(path)} {im.size}")

# ── 低成本可印刷 SKU ───────────────────────────────────────
def cheap_skus(path):
    CW,pad,gap,head=250,44,18,110
    C=5; W=pad*2+CW*C+gap*(C-1); H=head+CW+62+pad
    im=Image.new("RGB",(W,H),(0xFA,0xFA,0xF8)); d=ImageDraw.Draw(im)
    header(d,"低成本可印刷 SKU（追加候选）",
      "全部免开模、起订低、单价个位数。用于把货架铺满与提高连带率，不占主力预算。")
    y=head
    items=[("镜片清洁布","超细纤维印花 · 零售 ¥12–19","cloth"),
           ("异形贴纸套装","模切贴纸一版多腾 · ¥9–19","sticker"),
           ("集章卡 + 印章","景区盖章打卡，带动复访","stamp"),
           ("纸质书签套装","四腾一套 · ¥15–25","mark"),
           ("明信片 / 票根卡","方向 C 插画 · ¥6–12","card")]
    for i,(nm,desc,kind) in enumerate(items):
        x=pad+i*(CW+gap); t=Image.new("RGBA",(CW,CW),(0,0,0,0)); dd=ImageDraw.Draw(t)
        if kind=="cloth":
            dd.rounded_rectangle([26,40,CW-27,CW-40],10,fill=TEAL+(255,))
            for r in range(2):
                for c in range(3):
                    t.alpha_composite(glyph(["image14","image11","image12","image4","image9","image7"][r*3+c],
                                            62,CREAM,pad=.16),(38+c*62,58+r*62))
            dd.arc([CW-70,CW-72,CW-30,CW-32],0,360,fill=CREAM+(180,),width=2)
        elif kind=="sticker":
            dd.rounded_rectangle([22,30,CW-23,CW-30],8,fill=PAPER+(255,),outline=(0xD2,0xD6,0xCF,255),width=2)
            ks=["image14","image11","image12","image4","image9","image7","image5","image8"]
            cols=[NAVY,ORG,GRN,TEAL,NAVY,GOLD,GRN,NAVY]
            for j,(kk,cc) in enumerate(zip(ks,cols)):
                r,c=divmod(j,4)
                t.alpha_composite(glyph(kk,54,cc,pad=.14),(30+c*54,54+r*74))
        elif kind=="stamp":
            dd.rounded_rectangle([20,44,CW-90,CW-44],8,fill=PAPER+(255,),outline=NAVY+(255,),width=2)
            for j,kk in enumerate(["image14","image12","image9","image4"]):
                r,c=divmod(j,2)
                dd.rectangle([34+c*62,60+r*62,34+c*62+50,60+r*62+50],outline=(0xC0,0xC6,0xBE,255),width=2)
                if j<2: t.alpha_composite(glyph(kk,50,ORG,pad=.16),(34+c*62,60+r*62))
            dd.rounded_rectangle([CW-78,70,CW-30,CW-96],6,fill=(0x8B,0x5E,0x3C,255))
            dd.rounded_rectangle([CW-84,CW-96,CW-24,CW-66],5,fill=NAVY+(255,))
            t.alpha_composite(glyph("image9",44,CREAM,pad=.14),(CW-76,CW-92))
        elif kind=="mark":
            for j,(kk,cc) in enumerate(zip(["image14","image11","image12","image7"],[NAVY,TEAL,GRN,GOLD])):
                bx=26+j*56
                dd.rounded_rectangle([bx,44,bx+46,CW-44],6,fill=cc+(255,))
                t.alpha_composite(glyph(kk,46,CREAM,pad=.10),(bx,int(CW/2)-46))
                dd.ellipse([bx+18,54,bx+28,64],fill=(0xFA,0xFA,0xF8,255))
        else:
            for j,off in enumerate([(30,54),(52,40),(74,26)]):
                cc=[PAPER,CREAM,PAPER][j]
                dd.rounded_rectangle([off[0],off[1],off[0]+128,off[1]+96],6,
                                     fill=cc+(255,),outline=(0xD2,0xD6,0xCF,255),width=2)
            t.alpha_composite(glyph("image6",118,NAVY,pad=.10),(80,32))
        im.paste(t,(x,y),t)
        d.text((x,y+CW+8),nm,font=font(16,True),fill=INK)
        d.text((x,y+CW+32),desc,font=font(12),fill=MUT)
    im.save(path,quality=92); print(f"  ✓ {os.path.basename(path)} {im.size}")

os.makedirs(os.path.join(HERE,"assets/v4"),exist_ok=True)
magnet_shapes(os.path.join(HERE,"assets/v4/v4_magnet_shapes.jpg"))
cheap_skus(os.path.join(HERE,"assets/v4/v4_cheap_skus.jpg"))
