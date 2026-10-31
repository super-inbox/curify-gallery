"""Append a 4-second native typography CTA; preserve the original 15-second master."""
from pathlib import Path
import subprocess,json
R=Path(__file__).resolve().parent
B='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
F='/System/Library/Fonts/Supplemental/Arial.ttf'
C='/System/Library/Fonts/STHeiti Medium.ttc'
def text(t,y,size,font=B,color='white'):
 return f"drawtext=fontfile='{font}':text='{t}':fontsize={size}:fontcolor={color}:x=(w-text_w)/2:y={y}"
filters=["drawbox=x=0:y=0:w=720:h=1280:color=0x211238:t=fill",
"drawbox=x=0:y=0:w=720:h=12:color=0x8B5CF6:t=fill",
text('Curify',270,70),text('AI VISUAL STUDIO',355,20,F,'0xC4B5DA'),
text('Batch Generation',490,48),text('批量生成产品广告',560,32,C,'0xE7DDF9'),
text('Product images + videos, at scale.',630,25,F,'0xC4B5DA'),
"drawbox=x=80:y=750:w=560:h=92:color=0x8254ED:t=fill",
text('DM “BATCH” for a quote',777,32),text('私信「批量」 · 获取方案与报价',875,27,C,'0xE7DDF9'),
text('Send your product + video count',952,23,F,'0xC4B5DA'),text('AI-GENERATED CONCEPT',1110,16,F,'0xA69AB8'),
'fade=t=in:st=0:d=0.25']
cmd=['ffmpeg','-hide_banner','-loglevel','error','-i',str(R/'jade-portal-15s.mp4'),'-f','lavfi','-i','color=c=0x211238:s=720x1280:r=24:d=4','-filter_complex',
 '[1:v]'+','.join(filters)+'[card];[0:v]setsar=1,setpts=PTS-STARTPTS[v0];[v0][card]concat=n=2:v=1:a=0[v];[0:a]asplit=2[a0][tail];[a0]afade=t=out:st=14.7:d=0.3[a1];[tail]atrim=start=11:end=15,asetpts=PTS-STARTPTS,volume=0.5,afade=t=in:st=0:d=0.4,afade=t=out:st=2.8:d=1.2[a2];[a1][a2]concat=n=2:v=0:a=1[a]',
 '-map','[v]','-map','[a]','-t','19','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart','-y',str(R/'jade-portal-19s-batch-cta.mp4')]
subprocess.run(cmd,check=True)
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-ss','17','-i',str(R/'jade-portal-19s-batch-cta.mp4'),'-frames:v','1','-y',str(R/'batch-cta-preview.jpg')],check=True)
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-i',str(R/'jade-portal-19s-batch-cta.mp4'),'-f','null','-'],check=True)
j=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','stream=codec_name,codec_type,width,height,r_frame_rate:format=duration,size','-of','json',str(R/'jade-portal-19s-batch-cta.mp4')]))
assert abs(float(j['format']['duration'])-19)<0.1
j['decode_check']='passed';j['cta_duration_s']=4;j['audio_note']='Original generated audio; final 4s reused at half volume under CTA with fades.'
(R/'qa-batch-cta.json').write_text(json.dumps(j,indent=2)+'\n')
print('Built and verified 19-second Batch Generation CTA version.')
