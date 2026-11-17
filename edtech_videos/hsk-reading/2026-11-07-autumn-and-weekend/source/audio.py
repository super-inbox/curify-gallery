from pathlib import Path
import json,urllib.request,concurrent.futures,time,xml.sax.saxutils,wave
from dotenv import dotenv_values
B=Path(__file__).resolve().parent
E=dotenv_values('/Users/qqwjq/curify-studio/curify_background/.env');key=E.get('AZURE_AI_API_KEY');region=E.get('AZURE_AI_REGION') or 'westus2'
assert key,'Azure speech configuration is missing'
def synth(c):
 p=B/'narration'/f'{c["id"]}.wav'
 if p.exists() and p.stat().st_size>1000:return
 sentences=[c['title_zh']+'。']+[x['zh'] for x in c['lines']]
 body="<break time='600ms'/>".join(xml.sax.saxutils.escape(x) for x in sentences)
 ssml="<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='https://www.w3.org/2001/mstts' xml:lang='zh-CN'><voice name='zh-CN-XiaoxiaoNeural'><mstts:express-as style='gentle'><prosody rate='-25%' pitch='-2%'>"+body+"</prosody></mstts:express-as><break time='700ms'/></voice></speak>"
 req=urllib.request.Request(f'https://{region}.tts.speech.microsoft.com/cognitiveservices/v1',data=ssml.encode(),headers={'Ocp-Apim-Subscription-Key':key,'Content-Type':'application/ssml+xml','X-Microsoft-OutputFormat':'riff-24khz-16bit-mono-pcm','User-Agent':'curify-hsk-reading'})
 for attempt in range(4):
  try:
   with urllib.request.urlopen(req,timeout=60) as r:data=r.read()
   assert data[:4]==b'RIFF' and len(data)>1000
   p.write_bytes(data)
   with wave.open(str(p)) as w:duration=w.getnframes()/w.getframerate()
   print(f'{c["id"]}: {duration:.1f}s female narration',flush=True);return
  except Exception:
   if attempt==3:raise
   time.sleep(2*(attempt+1))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:list(ex.map(synth,json.loads((B/'batch.json').read_text())))
