from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
ROOT=Path(__file__).resolve().parents[3]
D=ROOT/'2026-09-01-retouching/demos/scene-worlds-2026-10-11'
V=ROOT/'2026-10-08-visual-design'
CJK='/System/Library/Fonts/Hiragino Sans GB.ttc'
BOLD='/System/Library/Fonts/STHeiti Medium.ttc'
EN='/System/Library/Fonts/Supplemental/Arial.ttf'
def font(size,zh=False,bold=False):return ImageFont.truetype(BOLD if zh and bold else CJK if zh else EN,size)
def text(d,pos,s,size=30,zh=False,bold=False,fill='#233342'):
 f=font(size,zh,bold)
 assert d.textbbox((0,0),s,font=f)[2]<1010,s
 d.text(pos,s,font=f,fill=fill)
def panel(canvas,path,box):
 im=Image.open(path).convert('RGB');im=ImageOps.contain(im,(box[2],box[3]),Image.Resampling.LANCZOS)
 canvas.paste(im,(box[0]+(box[2]-im.width)//2,box[1]+(box[3]-im.height)//2))
rows=[('01-jurassic','Jurassic rainforest','侏罗纪雨林'),('02-hogwarts','Hogwarts candlelit hall','霍格沃茨烛光长廊'),('03-frozen','Frozen-inspired ice palace','冰雪奇缘灵感冰宫'),('04-asgard','Asgard golden city','阿斯加德金色神域')]
for slug,en,zh in rows:
 for lang in ['en','zh']:
  z=lang=='zh';im=Image.new('RGB',(1080,1440),'#f7f5ef');d=ImageDraw.Draw(im)
  text(d,(40,30),'一张原图，换个电影世界' if z else 'One portrait. A different world.',44,z,True)
  text(d,(40,93),zh if z else en,30,z,fill='#93673e')
  text(d,(40,146),'原图 · AI 生成人物' if z else 'BEFORE · AI-generated model',24,z)
  panel(im,D/'00-source.png',(40,181,1000,545))
  text(d,(40,749),'场景增强 · 背景编辑示例' if z else 'AFTER · Scene-enhancement concept',24,z)
  panel(im,D/(slug+'.png'),(40,785,1000,545))
  text(d,(40,1360),'AI 生成修图概念 · 非客片 · curify-ai.com' if z else 'AI-generated retouching concepts · not client work · curify-ai.com',23,z,fill='#646b70')
  im.save(D/f'{slug}-before-after-{lang}.jpg',quality=94)
for lang in ['en','zh']:
 z=lang=='zh';im=Image.new('RGB',(1080,1440),'#f7f5ef');d=ImageDraw.Draw(im)
 text(d,(40,30),'同一个孩子，四个电影世界' if z else 'One child. Four cinematic worlds.',43,z,True)
 text(d,(40,96),'同一张 AI 原图的四种背景方向' if z else 'Four background edits from one synthetic source',27,z)
 text(d,(190,152),'AI 人物原图' if z else 'SYNTHETIC SOURCE',22,z)
 panel(im,D/'00-source.png',(190,192,700,382))
 for i,(slug,en,zh) in enumerate(rows):
  x=40+(i%2)*514;y=616+(i//2)*337
  text(d,(x,y),zh if z else en,24,z)
  panel(im,D/(slug+'.png'),(x,y+43,486,265))
 text(d,(40,1300),'观察重点：脸、头发、针织纹理、手和边缘' if z else 'Compare the face, hair, knit, hands and edges.',25,z)
 text(d,(40,1365),'AI 生成修图概念 · 非客片 · curify-ai.com' if z else 'AI-generated retouching concepts · not client work · curify-ai.com',23,z,fill='#646b70')
 im.save(D/f'overview-{lang}.jpg',quality=94)
for slug in ['celestial-south-heavenly-gate','celestial-jade-emperor-palace']:
 Image.open(V/(slug+'.png')).convert('RGB').save(V/(slug+'.jpg'),quality=95)
 for suffix,size in [('rn-3x4',(1080,1440)),('ig-4x5',(1080,1350))]:
  im=Image.new('RGB',size,'#122630');panel(im,V/(slug+'.png'),(0,0,*size));im.save(V/f'{slug}-{suffix}.jpg',quality=95)
print('Created 8 bilingual before/after cards, 2 overview sheets and 6 celestial JPEG assets')
