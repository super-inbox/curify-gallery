"""Single paid submission; persist task ID before polling. No automatic resubmission.
Usage: python3 generate.py submit | poll
Uses existing MINIMAX_API_KEY_CN or CURIFY_ENV_FILE (never prints credentials).
"""
import os,sys,json,base64
from pathlib import Path
import requests
ROOT=Path(__file__).resolve().parent
STATE=ROOT/'generation.json'
HOST='https://api.minimaxi.com'
env=Path(os.environ.get('CURIFY_ENV_FILE',str(Path.home()/'curify-studio/curify_background/.env')))
if env.exists():
 for line in env.read_text().splitlines():
  if '=' in line and not line.strip().startswith('#'):
   k,v=line.split('=',1);os.environ.setdefault(k.strip(),v.strip().strip('\"').strip("'"))
headers={'Authorization':'Bearer '+os.environ['MINIMAX_API_KEY_CN'],'Content-Type':'application/json'}
job=json.loads(STATE.read_text()) if STATE.exists() else {}
if sys.argv[1]=='submit':
 if job: raise SystemExit('Existing job: inspect or poll; submission not repeated.')
 prompt=(ROOT/'motion-prompt.txt').read_text()
 job={'status':'submitting','model':'MiniMax-H3','duration':15,'resolution':'768P','ratio':'9:16','prompt':prompt}
 STATE.write_text(json.dumps(job,indent=2))
 body={k:job[k] for k in ['model','duration','resolution','ratio']}
 body['content']=[{'type':'image_url','image_url':{'url':'data:image/png;base64,'+base64.b64encode((ROOT/'first-frame.png').read_bytes()).decode()}},{'type':'text','text':prompt}]
 r=requests.post(HOST+'/v2/video_generation',headers=headers,json=body,timeout=180);r.raise_for_status();j=r.json()
 tid=j.get('task_id') or j.get('id')
 if not tid:
  job['status']='submission_failed';job['message']=(j.get('base_resp') or {}).get('status_msg','No task ID returned')
 else:job.update(task_id=str(tid),status='submitted')
 STATE.write_text(json.dumps(job,indent=2));print(job['status'],job.get('task_id',''),job.get('message',''))
elif sys.argv[1]=='poll':
 if job.get('status')=='downloaded':print('Already downloaded');raise SystemExit()
 r=requests.get(HOST+'/v2/query/video_generation',params={'task_id':job['task_id']},headers=headers,timeout=60);r.raise_for_status()
 it=next((x for x in r.json().get('items',[]) if str(x.get('id'))==job['task_id']),None)
 if it:
  job['status']=it.get('status','Unknown')
  url=(it.get('content') or {}).get('url') or it.get('download_url')
  if url and job['status'].lower() in ['success','succeeded','completed']:
   video=requests.get(url,timeout=180);video.raise_for_status();(ROOT/'jade-portal-15s-source.mp4').write_bytes(video.content);job['status']='downloaded'
  STATE.write_text(json.dumps(job,indent=2))
 print(job['status'])
