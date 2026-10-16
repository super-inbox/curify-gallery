# -*- coding: utf-8 -*-
"""
2x2 grid cover, RedNote 3:4 — the format a competitor post in
`curify-frontend/raw/rednote-example-09-22/` uses (224 likes, 197 saves): a four-up of
on-model / product frames with large overlaid Chinese type, plus pain-first body copy.

We take the FORM. Everything in the frame is ours: four scenes of one ivory handbag,
cropped out of `ecommerce_ad_videos/fashion_batch_campaign/` — our own campaign demo,
already cleared `ship` in index.json. The source frames carry burnt-in English captions,
so each crop is taken from a caption-free band of its scene.

⛔ Not copied from the reference: its wording, its yellow-on-black type treatment, its
"Powered by …" watermark, and its 全品类可接 capability claim.

Run:  python3 make_rn_grid_cover.py
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
VIDEO = os.path.expanduser(
    "~/curify-gallery/ecommerce_ad_videos/fashion_batch_campaign/"
    "curify_fashion_batch_ad_narrated.mp4")
OUT = os.path.join(HERE, "rn-grid-箱包四图.jpg")
TMP = "/tmp/_rn_grid"

W, H = 1080, 1440
CELL = 540
GRID_TOP = 180

INK = "#1A1A1A"
ACC = "#C0521E"
CREAM = "#FAF8F2"

HEI = "/System/Library/Fonts/STHeiti Medium.ttc"
HIRA = "/System/Library/Fonts/Hiragino Sans GB.ttc"

# (timestamp, crop-y) — y picked so the 1080x1080 square misses the burnt-in caption
SCENES = [
    ("0.3", 430, "产品图"),
    ("2.8", 120, "模特图"),
    ("5.8", 400, "场景图"),
    ("8.8", 400, "细节图"),
]


def sh(cmd):
    subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)


def main():
    os.makedirs(TMP, exist_ok=True)
    cells = []
    for i, (t, cy, label) in enumerate(SCENES):
        raw = f"{TMP}/raw{i}.png"
        cell = f"{TMP}/cell{i}.png"
        sh(f'ffmpeg -y -v error -ss {t} -i "{VIDEO}" -frames:v 1 '
           f'-vf "crop=1080:1080:0:{cy}" "{raw}"')
        # square -> cell, with a small label chip bottom-left
        sh(f'magick "{raw}" -resize {CELL}x{CELL}^ -gravity center '
           f'-extent {CELL}x{CELL} "{cell}"')
        sh(f'magick "{cell}" '
           f'-fill "rgba(250,248,242,0.92)" -draw "roundrectangle 18,{CELL-56} 140,{CELL-16} 10,10" '
           f'-font "{HEI}" -pointsize 26 -fill "{INK}" '
           f'-annotate +34+{CELL-26} "{label}" "{cell}"')
        cells.append(cell)

    # assemble the 2x2
    sh(f'magick montage {" ".join(chr(34)+c+chr(34) for c in cells)} '
       f'-tile 2x2 -geometry +0+0 -background none "{TMP}/grid.png"')

    # canvas: cream, grid inset, then type over it
    sh(f'magick -size {W}x{H} xc:"{CREAM}" '
       f'"{TMP}/grid.png" -geometry +0+{GRID_TOP} -composite "{TMP}/base.png"')

    y_hdr = 96
    band_top = GRID_TOP + CELL - 150          # type sits across the grid's middle seam
    sh(f'magick "{TMP}/base.png" '
       # top tag
       f'-font "{HEI}" -pointsize 30 -fill "{ACC}" -annotate +64+{y_hdr} "箱包 · 服装 · 饰品" '
       f'-font "{HIRA}" -pointsize 25 -fill "#787468" -annotate +64+{y_hdr+44} "一个款，拍不完的图" '
       # dark scrim behind the headline so it reads over any frame
       f'-fill "rgba(26,26,26,0.62)" -draw "rectangle 0,{band_top} {W},{band_top+300}" '
       f'-font "{HEI}" -pointsize 104 -fill white '
       f'-annotate +58+{band_top+126} "一个款" '
       f'-font "{HEI}" -pointsize 104 -fill "#F2C14E" '
       f'-annotate +58+{band_top+248} "出一整套图" '
       # bottom strip
       f'-fill "{CREAM}" -draw "rectangle 0,{GRID_TOP+2*CELL} {W},{H}" '
       f'-font "{HEI}" -pointsize 31 -fill "{INK}" '
       f'-annotate +64+{GRID_TOP+2*CELL+72} "产品图 · 模特图 · 场景图 · 细节图" '
       f'-font "{HIRA}" -pointsize 24 -fill "#787468" '
       f'-annotate +64+{GRID_TOP+2*CELL+118} "AI 生成演示 · 非客户实拍 · curify-ai.com" '
       f'"{OUT}"')
    print("wrote", os.path.basename(OUT))


if __name__ == "__main__":
    main()
