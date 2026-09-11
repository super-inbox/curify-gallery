#!/usr/bin/env python3
"""Assemble the LinkedIn cut: 20 shots -> concat -> burn captions -> mux audio."""
import os, subprocess, shlex, sys

BASE  = os.path.dirname(os.path.abspath(__file__))
GFX   = os.path.join(BASE, "gfx")
SHOTS = os.path.join(BASE, "shots"); os.makedirs(SHOTS, exist_ok=True)
G     = "/Users/qqwjq/curify-gallery"
F     = "/Users/qqwjq/curify-frontend"
HUMAN = f"{F}/raw/b-roll-09-05/human-video.mp4"
MUSIC = f"{G}/assets/music/monume-modern-futuristic-technology-519250.mp3"
W, H, FPS = 1080, 1350, 30

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode:
        print("FAILED:", cmd, "\n", r.stderr[-2500:]); sys.exit(1)

def hole(name):
    x, y, w, h = (int(v) for v in open(f"{GFX}/{name}.box").read().split())
    return x, y, w, h

ENC = "-c:v libx264 -crf 12 -preset veryfast -pix_fmt yuv420p -r 30"

def human(out, ss, y0, n, overlay=None, ov_st=0.12, fade_in=None, fade_out=None):
    v = f"[0:v]crop=720:900:0:{y0},scale={W}:{H}:flags=lanczos,setsar=1,fps={FPS}"
    if fade_in:  v += f",fade=in:st=0:d={fade_in}"
    chain, inputs, last = [], f'-ss {ss} -i "{HUMAN}"', None
    if overlay:
        inputs += f' -framerate {FPS} -loop 1 -i "{GFX}/{overlay}"'
        chain.append(v + "[v]")
        chain.append(f"[1:v]format=rgba,fade=in:st={ov_st}:d=0.38:alpha=1[o]")
        last = "[v][o]overlay=0:0"
    else:
        last = v
    if fade_out:
        st = (n - int(fade_out * FPS)) / FPS
        last += f",fade=out:st={st:.3f}:d={fade_out}"
    chain.append(last + "[out]")
    run(f'ffmpeg -y -v error {inputs} -filter_complex "{";".join(chain)}" '
        f'-map "[out]" -frames:v {n} -an {ENC} "{SHOTS}/{out}.mp4"')

def broll_full(out, src, ss, crop, n, overlay):
    cw, ch, cx, cy = crop
    run(f'ffmpeg -y -v error -ss {ss} -i "{src}" -framerate {FPS} -loop 1 -i "{GFX}/{overlay}.png" '
        f'-filter_complex "[0:v]crop={cw}:{ch}:{cx}:{cy},scale={W}:{H}:flags=lanczos,setsar=1,fps={FPS}[v];'
        f'[1:v]format=rgba,fade=in:st=0:d=0.25:alpha=1[o];[v][o]overlay=0:0[out]" '
        f'-map "[out]" -frames:v {n} -an {ENC} "{SHOTS}/{out}.mp4"')

def broll_card_video(out, src, ss, n, overlay, crop=None):
    hx, hy, hw, hh = hole(overlay)
    pre = f"crop={crop[0]}:{crop[1]}:{crop[2]}:{crop[3]}," if crop else ""
    run(f'ffmpeg -y -v error -ss {ss} -i "{src}" -framerate {FPS} -loop 1 -i "{GFX}/{overlay}.png" '
        f'-filter_complex "[0:v]{pre}scale={hw}:{hh}:flags=lanczos,setsar=1,fps={FPS}[m];'
        f'color=c=black:s={W}x{H}:r={FPS}[bg];[bg][m]overlay={hx}:{hy}[b];'
        f'[1:v]format=rgba[o];[b][o]overlay=0:0,fade=in:st=0:d=0.22[out]" '
        f'-map "[out]" -frames:v {n} -an {ENC} "{SHOTS}/{out}.mp4"')

def broll_card_still(out, img, n, overlay, zoom=0.09):
    hx, hy, hw, hh = hole(overlay)
    run(f'ffmpeg -y -v error -framerate {FPS} -loop 1 -i "{img}" '
        f'-framerate {FPS} -loop 1 -i "{GFX}/{overlay}.png" '
        f'-filter_complex "[0:v]scale={hw*2}:{hh*2}:flags=lanczos,setsar=1,'
        f"zoompan=z='1+{zoom}*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
        f'd=1:s={hw}x{hh}:fps={FPS}[m];'
        f'color=c=black:s={W}x{H}:r={FPS}[bg];[bg][m]overlay={hx}:{hy}[b];'
        f'[1:v]format=rgba[o];[b][o]overlay=0:0,fade=in:st=0:d=0.22[out]" '
        f'-map "[out]" -frames:v {n} -an {ENC} "{SHOTS}/{out}.mp4"')

def seq(out, folder, n, fade_in=None, fade_out=None):
    vf = f"scale={W}:{H},setsar=1,fps={FPS}"
    if fade_in:  vf += f",fade=in:st=0:d={fade_in}"
    if fade_out: vf += f",fade=out:st={(n - int(fade_out*FPS))/FPS:.3f}:d={fade_out}"
    run(f'ffmpeg -y -v error -framerate {FPS} -i "{GFX}/{folder}/%04d.png" '
        f'-vf "{vf}" -frames:v {n} -an {ENC} "{SHOTS}/{out}.mp4"')

# ------------------------------------------------------------------ shots
human("01", 0.00,    360, 219, overlay="open_mark.png", ov_st=4.40, fade_in=0.5)
human("02", 7.30,    275,  93, overlay="chapter_1.png")
broll_card_video("03", f"{G}/ecommerce_workflow/camera_marketing_kit_en.mp4",
                 4.5, 120, "s03")
broll_card_still("04", f"{G}/smm_daily/2026-09-01-retouching/"
                       "shared-retouching-blueprint.jpg", 111, "s04")
broll_full("05", f"{G}/ecommerce_workflow/backpack_viral_en.mp4", 11.0,
           (1080, 1350, 0, 0), 56, "s05")
broll_full("06", f"{F}/public/video/use-case-merch-en.mp4", 8.5,
           (800, 1000, 80, 60), 58, "s06")
human("07", 21.90,   360,  84)
human("08", 24.70,   275,  96, overlay="chapter_2.png")
broll_full("09", f"{G}/brand_brief/catte_coffee_brand_workflow_en.mp4", 18.6,
           (900, 1125, 90, 430), 105, "s09")
broll_card_still("10", f"{G}/designAI_manufacturing/layered-PSD/layers_product_en.jpg", 81, "s10")
seq("11", "mosaic", 96)
human("12", 37.30,   360, 147)
human("13", 42.20,   275,  57, overlay="chapter_3.png")
broll_card_still("14", f"{G}/designAI_manufacturing/"
                       "curify-agent-design-tool-orchestration-poster-2026-08-06.png", 57, "s14")
broll_card_still("15", f"{G}/DS_AI/agentic-evaluation.png", 56, "s15")
broll_card_video("16", f"{G}/Marketing_media/content-search-explainer/"
                       "curify-intro-template-search.mp4", 20.0, 58, "s16", crop=(1280, 656, 0, 28))
broll_card_video("17", f"{F}/public/video/asl-demo-translation.mp4", 10.0, 95, "s17")
human("18", 52.95,   360, 109, fade_out=0.20)
seq("19", "finale", 330, fade_in=0.27, fade_out=0.55)

# ------------------------------------------------------------------ assemble
order = ["01","02","03","04","05","06","07","08","09","10",
         "11","12","13","14","15","16","17","18","19"]
with open(f"{SHOTS}/list.txt", "w") as fh:
    for s in order:
        fh.write(f"file '{SHOTS}/{s}.mp4'\n")
run(f'ffmpeg -y -v error -f concat -safe 0 -i "{SHOTS}/list.txt" -c copy "{BASE}/silent.mp4"')

DUR = 2028 / FPS
VOICE = (f"[0:a]atrim=0:65.27,asetpts=N/SR/TB,highpass=f=85,afftdn=nr=10,"
         f"loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000,apad,atrim=0:{DUR},"
         f"afade=out:st={DUR-0.5:.2f}:d=0.5[va];[va]asplit=2[v1][sc]")
BED   = (f"[1:a]atrim=0:{DUR},asetpts=N/SR/TB,loudnorm=I=-17:TP=-2:LRA=9,"
         f"volume=-16dB,aresample=48000,afade=in:st=0:d=2.0,"
         f"afade=out:st={DUR-2.2:.2f}:d=2.2[bed]")
DUCK  = "[bed][sc]sidechaincompress=threshold=0.02:ratio=8:attack=15:release=380[bedduck]"
MIX   = "[v1][bedduck]amix=inputs=2:duration=first:normalize=0[a]"

def mux(out, with_music):
    if with_music:
        fc = f"{VOICE};{BED};{DUCK};{MIX}"
        ins = f'-i "{BASE}/silent.mp4" -i "{MUSIC}" -i "{HUMAN}"'
        fc = fc.replace("[0:a]", "[2:a]")
        amap = '-map "[a]"'
    else:
        fc = (f"[1:a]atrim=0:65.27,asetpts=N/SR/TB,highpass=f=85,afftdn=nr=10,"
              f"loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000,apad,atrim=0:{DUR},"
              f"afade=out:st={DUR-0.5:.2f}:d=0.5[a]")
        ins = f'-i "{BASE}/silent.mp4" -i "{HUMAN}"'
        amap = '-map "[a]"'
    run(f'ffmpeg -y -v error {ins} -filter_complex "{fc}" '
        f'-map 0:v {amap} '
        f'-vf "subtitles=\'{BASE}/captions.ass\':fontsdir=\'{F}/public/fonts\'" '
        f'-c:v libx264 -crf 19 -preset slow -profile:v high -level 4.1 -pix_fmt yuv420p '
        f'-x264-params "keyint=60:min-keyint=30" -movflags +faststart '
        f'-c:a aac -b:a 192k -ar 48000 -ac 2 -shortest "{out}"')

mux(f"{BASE}/curify-vision-linkedin.mp4", True)
mux(f"{BASE}/curify-vision-linkedin-nomusic.mp4", False)
print("done")
