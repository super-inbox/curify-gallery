"""Render three 30-second bilingual editorial films from generated moving clips."""
from pathlib import Path
import json,subprocess,sys
from PIL import Image,ImageDraw,ImageFont
R=Path(__file__).resolve().parent
G=R.parents[2]
D=G/'smm_daily/2026-09-10-fb-souvenir-video/2026-10-29-fashion-through-time'
W=R/'edit';W.mkdir(exist_ok=True)
EN='/System/Library/Fonts/Supplemental/Georgia.ttf'
SANS='/System/Library/Fonts/Supplemental/Arial.ttf'
CN='/System/Library/Fonts/STHeiti Light.ttc'
META={
'fashion':dict(id='H1',file='100-years-of-fashion-30s',title='100 YEARS OF FASHION',zh='百年女装，轮廓怎么变？',scope='BRITAIN / FRANCE · SELECTED STYLES',scopezh='英法时装选例 · AI风格演绎',years=['1900','1925','1950','1975','2000'],labels=[('High neck · long skirt','高领长裙'),('Dropped waist · straight line','低腰直线'),('Fitted waist · full skirt','收腰蓬裙'),('Tailoring · flared trousers','套装喇叭裤'),('Blazer · bootcut denim','短西装与牛仔裤')]),
'gowns':dict(id='H2',file='gowns-through-time-30s',title='400 YEARS OF GOWNS',zh='四百年礼服，裙摆里的变化',scope='EUROPEAN FORMALWEAR · SELECTED STYLES',scopezh='欧洲上层礼服选例 · AI风格演绎',years=['1550','1750','1810','1860','1950'],labels=[('Renaissance · rich sleeves','文艺复兴：华丽衣袖'),('Rococo · wide silhouette','洛可可：横向裙撑'),('Empire · raised waist','帝政风：高腰长裙'),('Crinoline · bell-shaped skirt','裙撑时代：钟形裙摆'),('Eveningwear · sculpted volume','晚礼服：收腰与量感')]),
'bridal':dict(id='H3',file='100-years-of-bridal-style-30s',title='100 YEARS OF BRIDAL STYLE',zh='百年婚纱，浪漫换了轮廓',scope='BRITISH WHITE BRIDALWEAR · SELECTED STYLES',scopezh='英式白色婚纱选例 · AI风格演绎',years=['1920','1950','1980','2000','2020'],labels=[('Beading · dropped waist','珠饰与低腰线'),('Lace · tea-length skirt','蕾丝与中长蓬裙'),('Puff sleeves · taffeta','泡泡袖与塔夫绸'),('Strapless · A-line','抹胸与A字裙'),('Clean lines · crepe','简洁线条与绉纱')])}

def run(cmd):subprocess.run(cmd,check=True,stdout=subprocess.DEVNULL)
def centered(d,text,y,font,fill):
 box=d.textbbox((0,0),text,font=font);d.text(((1080-box[2])/2,y),text,font=font,fill=fill)
def overlay(key,i):
 m=META[key];im=Image.new('RGBA',(1080,1920),(0,0,0,0));d=ImageDraw.Draw(im)
 # Editorial frame keeps text away from the face, hands and garment silhouette.
 d.rectangle((0,0,1080,158),fill=(24,22,19,255))
 d.rectangle((0,1580,1080,1920),fill=(24,22,19,255))
 titlefont=ImageFont.truetype(SANS,42 if key!='bridal' else 37)
 centered(d,m['title'],43,titlefont,'#e8d7b5')
 centered(d,m['zh'],99,ImageFont.truetype(CN,32),'#f4f0e8')
 centered(d,'c. '+m['years'][i],1594,ImageFont.truetype(EN,63),'#f5e3bd')
 centered(d,m['labels'][i][0],1672,ImageFont.truetype(SANS,32),'#f4f0e8')
 centered(d,m['labels'][i][1],1717,ImageFont.truetype(CN,31),'#e4d5bc')
 for j,year in enumerate(m['years']):
  x=160+j*190;d.line((x-60,1780,x+60,1780),fill='#d6b77e' if j<=i else '#56514a',width=4)
  font=ImageFont.truetype(SANS,25);b=d.textbbox((0,0),year,font=font)
  d.text((x-b[2]/2,1795),year,font=font,fill='#f0d6a5' if j==i else '#9b958b')
 centered(d,m['scopezh'],1842,ImageFont.truetype(CN,24),'#b8b1a7')
 p=W/f'{key}-{i}-overlay.png';im.save(p);return p

def build(key):
 m=META[key];parts=[]
 for i,y in enumerate(m['years']):
  src=R/'raw'/f'{key}-{y}.mp4'
  if not src.exists():raise FileNotFoundError(src)
  info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','json',str(src)]))
  dur=float(info['format']['duration']);ov=overlay(key,i);out=W/f'{key}-{i}.mp4'
  # Original generated motion is retimed slightly to six seconds, not replaced by still pans.
  filt=f'[0:v]setpts=(PTS-STARTPTS)*{6/dur:.8f},fps=30,scale=798:1418:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:160:color=0x181613,setsar=1[v];[v][1:v]overlay=0:0,format=yuv420p[out]'
  run(['ffmpeg','-v','error','-y','-i',str(src),'-i',str(ov),'-filter_complex',filt,'-map','[out]','-an','-frames:v','180','-c:v','libx264','-preset','fast','-crf','18',str(out)])
  parts.append(out)
 cat=W/f'{key}-concat.txt';cat.write_text(''.join("file '"+str(p)+"'\n" for p in parts))
 out=R/(m['file']+'.mp4')
 music=G/'assets/music/alexgrohl-sweet-life-luxury-chill-438146.mp3'
 run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(cat),'-ss','8','-i',str(music),'-map','0:v','-map','1:a','-c:v','copy','-af','atrim=duration=30,asetpts=PTS-STARTPTS,loudnorm=I=-16:TP=-1.5:LRA=11,afade=t=out:st=28.5:d=1.5','-c:a','aac','-b:a','192k','-ar','48000','-t','30','-movflags','+faststart',str(out)])
 print(out,flush=True)
 preview=D/'previews';preview.mkdir(parents=True,exist_ok=True)
 thumbs=[]
 for n,t in enumerate([1,4,7,10,13,16,19,22,25,28]):
  p=W/f'{key}-qa-{n}.jpg';run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(out),'-frames:v','1',str(p)])
  thumb=Image.open(p).convert('RGB');thumb.thumbnail((216,384));thumbs.append(thumb)
 sheet=Image.new('RGB',(1080,808),'#181613');draw=ImageDraw.Draw(sheet)
 for n,thumb in enumerate(thumbs):sheet.paste(thumb,((n%5)*216,(n//5)*404))
 sheet.save(preview/(key+'-overview.jpg'),quality=90)
 run(['ffmpeg','-v','error','-y','-ss','1','-i',str(out),'-frames:v','1',str(preview/(key+'-cover.jpg'))])
 run(['ffmpeg','-v','error','-i',str(out),'-f','null','-'])
 report=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(out)]))
 (D/(key+'-media-report.json')).write_text(json.dumps(report,indent=2))
 return out
if __name__=='__main__':
 (D/'storyboard.json').write_text(json.dumps(META,ensure_ascii=False,indent=2))
 for key in (sys.argv[1:] or META):build(key)
