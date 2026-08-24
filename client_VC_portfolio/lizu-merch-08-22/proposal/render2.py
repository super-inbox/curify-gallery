# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import numpy as np, json, os
T="totem/mask"; META=json.load(open(f"{T}/meta.json"))
FZ="/System/Library/Fonts/STHeiti Medium.ttc"; FS="/System/Library/Fonts/Supplemental/Songti.ttc"
def font(s,serif=False): return ImageFont.truetype(FS if serif else FZ, s)
def glyph(key,size,color,pad=.10):
    m=np.array(Image.open(f"{T}/{key}.png").convert("L"))>127
    h,w=m.shape; box=int(size*(1-pad*2)); sc=min(box/w,box/h)
    im=Image.fromarray((m*255).astype("uint8")).resize((max(1,int(w*sc)),max(1,int(h*sc))),Image.LANCZOS)
    L=Image.new("RGBA",(size,size),(0,0,0,0))
    L.paste(Image.new("RGBA",im.size,color+(255,)),((size-im.width)//2,(size-im.height)//2),im); return L
def rr(size,fill,r=14):
    c=Image.new("RGBA",size,(0,0,0,0)); ImageDraw.Draw(c).rounded_rectangle([0,0,size[0]-1,size[1]-1],r,fill=fill); return c

WAYS=[("A  墨蓝本白","沉稳克制 · 已定基调",(0x1E,0x3A,0x5F),(0xF2,0xF0,0xE8)),
      ("B  浅底反转","通透留白 · 最不老气",(0xF4,0xF3,0xEE),(0x16,0x2B,0x45)),
      ("C  海岛明快","年轻客群 · 货架抓眼",(0x0E,0x7C,0x94),(0xFF,0x7A,0x59)),
      ("D  椰林清新","海南在地 · 清爽",(0xED,0xF0,0xE8),(0x2F,0x6B,0x4F)),
      ("E  暖阳撞色","高对比 · 适合小件",(0x14,0x20,0x2B),(0xF2,0xB1,0x2E))]
PICK=["image14","image11","image12","image4"]   # 蛙 鸟 鱼 蝴蝶（避开含万字纹的鹿）

def colorways(path):
    RAIL,CW,pad,gap,head=210,236,44,16,110
    W=pad*2+RAIL+CW*len(PICK)+gap*(len(PICK)-1)
    H=head+34+len(WAYS)*(CW+gap)+pad
    im=Image.new("RGB",(W,H),(0xFA,0xFA,0xF8)); d=ImageDraw.Draw(im)
    d.text((pad,32),"配色方案 · 五选一",font=font(31,True),fill=(0x14,0x20,0x2B))
    d.text((pad,74),"同一组真实图腾，五种配色。纹样取自贵司《掼蛋扑克纹样参考》原稿，未作改动。",
           font=font(14),fill=(0x6E,0x76,0x7E))
    for i,k in enumerate(PICK):
        d.text((pad+RAIL+i*(CW+gap),head+8),META[k]["name"],font=font(14),fill=(0x8A,0x92,0x99))
    y=head+34
    for label,note,bg,ink in WAYS:
        d.text((pad,y+CW//2-24),label,font=font(19,True),fill=(0x14,0x20,0x2B))
        d.text((pad,y+CW//2+6),note,font=font(13),fill=(0x8A,0x92,0x99))
        for i,k in enumerate(PICK):
            t=rr((CW,CW),bg+(255,),16); t.alpha_composite(glyph(k,CW,ink,pad=.20))
            im.paste(t,(pad+RAIL+i*(CW+gap),y),t)
        y+=CW+gap
    im.save(path,quality=92); print(f"  ✓ {path} {im.size}")

def products(path):
    """把新配色落到真实品类上：冰箱贴 / 杯垫 / 帆布袋。"""
    pads=[("图腾外形冰箱贴","image14",(0x0E,0x7C,0x94),(0xFF,0x7A,0x59),"cut"),
          ("陶瓷杯垫","image12",(0xF4,0xF3,0xEE),(0x16,0x2B,0x45),"round"),
          ("陶瓷杯垫","image4",(0x0E,0x7C,0x94),(0xF2,0xF0,0xE8),"round"),
          ("覆膜帆布袋","image11",(0xED,0xF0,0xE8),(0x2F,0x6B,0x4F),"tote"),
          ("覆膜帆布袋","image7",(0x14,0x20,0x2B),(0xF2,0xB1,0x2E),"tote"),
          ("亚克力挂绳","image9",(0xF4,0xF3,0xEE),(0x16,0x2B,0x45),"cut")]
    CW,pad,gap,head=250,44,18,104
    C=3; rows=(len(pads)+C-1)//C
    W=pad*2+CW*C+gap*(C-1); H=head+rows*(CW+52)+pad
    im=Image.new("RGB",(W,H),(0xFA,0xFA,0xF8)); d=ImageDraw.Draw(im)
    d.text((pad,32),"新配色的产品应用",font=font(31,True),fill=(0x14,0x20,0x2B))
    d.text((pad,74),"同一批图腾，换配色与器形后的效果。均为真实图腾，非再创作。",
           font=font(14),fill=(0x6E,0x76,0x7E))
    for i,(nm,k,bg,ink,kind) in enumerate(pads):
        x=pad+(i%C)*(CW+gap); y=head+(i//C)*(CW+52)
        if kind=="round":
            t=Image.new("RGBA",(CW,CW),(0,0,0,0)); dd=ImageDraw.Draw(t)
            dd.ellipse([6,6,CW-7,CW-7],fill=bg+(255,))
            dd.ellipse([6,6,CW-7,CW-7],outline=(ink[0],ink[1],ink[2],90),width=3)
            t.alpha_composite(glyph(k,CW,ink,pad=.26))
        elif kind=="tote":
            t=Image.new("RGBA",(CW,CW),(0,0,0,0)); dd=ImageDraw.Draw(t)
            body=[int(CW*.15),int(CW*.30),int(CW*.85),int(CW*.95)]
            # 手柄先画，再用袋身盖住根部，避免出现悬空的小圆弧
            dd.arc([int(CW*.28),int(CW*.13),int(CW*.72),int(CW*.55)],195,345,
                   fill=(0xC9,0xC2,0xB2,255),width=9)
            dd.rounded_rectangle(body,10,fill=(0xEA,0xE6,0xDA,255))
            panel=Image.new("RGBA",(int(CW*.56),int(CW*.46)),bg+(255,))
            panel.alpha_composite(glyph(k,int(CW*.46),ink,pad=.10),(int(CW*.05),0))
            t.alpha_composite(panel,(int(CW*.22),int(CW*.38)))
        else:
            t=Image.new("RGBA",(CW,CW),(0,0,0,0))
            g=glyph(k,int(CW*.86),ink,pad=.06)
            halo=glyph(k,int(CW*.92),bg,pad=.06)
            t.alpha_composite(halo,(int(CW*.04),int(CW*.04)))
            t.alpha_composite(g,(int(CW*.07),int(CW*.07)))
        im.paste(t,(x,y),t)
        d.text((x,y+CW+10),nm,font=font(16,True),fill=(0x14,0x20,0x2B))
        d.text((x,y+CW+32),META[k]["name"]+" · "+META[k]["meaning"],font=font(12),fill=(0x8A,0x92,0x99))
    im.save(path,quality=92); print(f"  ✓ {path} {im.size}")

os.makedirs("v3",exist_ok=True)
colorways("v3/v3_colorways.jpg"); products("v3/v3_products.jpg")
