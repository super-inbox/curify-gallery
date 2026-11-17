from pathlib import Path
import json,html,hashlib,subprocess,concurrent.futures,re
B=Path(__file__).resolve().parent
cs=json.loads((B/'batch.json').read_text());items=[]
for group,dest in [('images','images/nano_insp'),('previews','images/nano_insp_preview'),('video','video')]:
 for p in sorted((B/'publish'/group).iterdir()):
  items.append(dict(local=str(p),gcs=f'gs://curify-static/{dest}/{p.name}',url=f'https://cdn.curify-ai.com/{dest}/{p.name}',bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
assert len(items)==30
reviews={r['id']:r for r in json.loads((B/'visual-qa.json').read_text())}
assert set(reviews)=={c['id'] for c in cs}
for c in cs:
 assert reviews[c['id']]['status']=='pass'
 assert reviews[c['id']]['sha256']==hashlib.sha256((B/'cards'/f'{c["id"]}.png').read_bytes()).hexdigest()
(B/'upload-manifest.json').write_text(json.dumps(items,indent=2)+'\n')
rows=[]
for c in cs:
 rows.append(f'''<article><a href="cards/{c['id']}.png"><img loading="lazy" src="cards/{c['id']}.png" alt="{html.escape(c['title_zh'])}"></a><div><small>HSK {c['level']} · {html.escape(c['category'])}</small><h2>{html.escape(c['title_zh'])}</h2><p>{html.escape(c['title_en'])}</p><video controls preload="none" poster="cards/{c['id']}.png" src="video/{c['id']}.mp4"></video></div></article>''')
(B/'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>HSK watercolor readings</title><style>body{margin:0;background:#faf6ef;color:#493021;font:16px system-ui}header,main{max-width:1240px;margin:auto;padding:32px}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:24px}article{background:white;border:1px solid #e2d3c3;border-radius:16px;overflow:hidden}img,video{width:100%;display:block}video{aspect-ratio:3/4}article div{padding:18px}h2{margin:8px 0}header p{max-width:800px;line-height:1.5}</style><header><h1>Chinese for real life</h1><p>10 HSK 2–3 readings in the approved watercolor template. Eight sentences, pinyin, eight vocabulary words and slow female Mandarin narration. Click a card to open it at full size.</p></header><main>'''+''.join(rows)+'</main></html>')
def qa(c):
 p=B/'video'/f'{c["id"]}.mp4'
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]))
 streams=probe['streams'];v=next(s for s in streams if s['codec_type']=='video');a=next(s for s in streams if s['codec_type']=='audio')
 assert v['codec_name']=='h264' and a['codec_name']=='aac' and v['width']==960 and v['height']==1280
 subprocess.run(['ffmpeg','-v','error','-i',str(p),'-f','null','-'],check=True,capture_output=True)
 D=float(a['duration']);V=float(v['duration']);assert 2.3<V-D<3.2
 assert v['r_frame_rate']=='30/1'
 audio=subprocess.run(['ffmpeg','-i',str(p),'-af','volumedetect','-vn','-sn','-f','null','-'],capture_output=True,text=True,check=True)
 level=float(re.search(r'mean_volume: ([\-0-9.]+) dB',audio.stderr).group(1));assert -40<level<-3
 frame_hashes=[]
 for at in [2,D-2]:
  frame_hashes.append(subprocess.check_output(['ffmpeg','-v','error','-ss',str(at),'-i',str(p),'-frames:v','1','-an','-f','md5','-'],text=True).strip())
 assert frame_hashes[0]!=frame_hashes[1],f'Static video: {p}'
 return dict(motion_frames_differ=True,id=c['id'],width=v['width'],height=v['height'],duration=V,audio_duration=D,mean_volume_db=level,full_decode='pass',video_codec=v['codec_name'],audio_codec=a['codec_name'],motion='slow upward scroll',voice='zh-CN-XiaoxiaoNeural',rate='-25%',card_sha256=hashlib.sha256((B/'cards'/f'{c["id"]}.png').read_bytes()).hexdigest())
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:checks=list(ex.map(qa,cs))
(B/'asset-qa.json').write_text(json.dumps(checks,indent=2)+'\n')
print(f'Packaged and decoded {len(checks)} videos; prepared {len(items)} CDN assets.')
