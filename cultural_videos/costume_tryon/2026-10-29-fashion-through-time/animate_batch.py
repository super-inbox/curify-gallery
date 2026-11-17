"""Resume only recorded jobs; never resubmit a failed or ambiguous request automatically."""
import importlib.util,json,os,time,concurrent.futures
from pathlib import Path
import requests
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('anim','/Users/qqwjq/curify-studio/dev/jayw/video_pipelines/costume_story_video/animate.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.load_env_file(Path('/Users/qqwjq/curify-studio/curify_background/.env'))
key=os.environ['MINIMAX_API_KEY_CN']
state=ROOT/'motion-jobs.json'; jobs=json.loads(state.read_text())
raw=ROOT/'raw';raw.mkdir(exist_ok=True)
prompt='A cinematic locked full-body fashion portrait. This adult woman breathes naturally and slowly turns her shoulders by ten degrees toward the camera, then gently settles. Subtle realistic fabric motion and one natural blink. Keep her identity, exact period outfit, colors, framing and backdrop consistent. No walking, no morphing, no outfit transformation, no camera zoom, no text, no logos, no added accessories. Anatomically natural hands.'
def save(): state.write_text(json.dumps(jobs,indent=2))
def submit(p):
 try:
  tid,note=m.submit_v1(key,'MiniMax-Hailuo-2.3',prompt,p,6,'1080P')
  return p.stem,{'task_id':tid,'status':note,'prompt':prompt,'model':'MiniMax-Hailuo-2.3','duration':6,'resolution':'1080P'}
 except Exception as e:return p.stem,{'status':'submission_uncertain','error_type':type(e).__name__,'prompt':prompt}
new=[p for p in sorted((ROOT/'frames').glob('*.png')) if p.stem not in jobs]
for p in new:jobs[p.stem]={'status':'submitting','prompt':prompt}
save()
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for name,result in pool.map(submit,new):
  jobs[name]=result;save();print(name,result['status'],flush=True)
for cycle in range(45):
 pending=[(n,j) for n,j in jobs.items() if j.get('task_id') and j.get('status') not in ['downloaded','Fail','Failed']]
 if not pending:break
 for n,j in pending:
  try:
   handle,status=m.poll_v1(key,j['task_id']);j['status']=status
   if handle and status=='Success':
    url=m.resolve_url(key,handle)
    if url:
     response=requests.get(url,timeout=180);response.raise_for_status()
     tmp=raw/(n+'.part');tmp.write_bytes(response.content);tmp.rename(raw/(n+'.mp4'));j['status']='downloaded'
   save();print(n,j['status'],flush=True)
  except Exception as e: print(n,'poll/download error',type(e).__name__,flush=True)
 if any(j.get('task_id') and j.get('status') not in ['downloaded','Fail','Failed'] for j in jobs.values()):time.sleep(20)
print('Finished pass',flush=True)
