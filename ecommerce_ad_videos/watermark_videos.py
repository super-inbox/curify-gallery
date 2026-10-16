#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Slanted tiled Curify watermark for the ad videos in this folder.

⚠️ **The parameters are not chosen here.** They are lifted verbatim from the house
convention in `curify-frontend/scripts/lib/watermark.cjs` (`TILE_DEFAULTS`), which the
image scripts already use:

    logoPct 0.22 · rotate -30° · opacity 0.15 · spacingFactor 1.8 · logo = public/logo.svg

The overlay is built with the SAME ImageMagick pipeline that module runs, then composited
onto the video with ffmpeg. If the convention changes, change it there and re-run this —
do not retune it here.

Usage:
    python3 watermark_videos.py                 # the four MANAGED videos
    python3 watermark_videos.py fabric_ad       # just one
    python3 watermark_videos.py --force         # rebuild even if output is newer
"""
import argparse
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.expanduser("~/curify-frontend/public/logo.svg")

# verbatim from curify-frontend/scripts/lib/watermark.cjs → TILE_DEFAULTS
LOGO_PCT = 0.22
SPACING_FACTOR = 1.8
OPACITY = 0.15
ROTATE = -30


def sh(cmd):
    return subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True).stdout.strip()


def probe(path):
    out = sh(f'ffprobe -v error -select_streams v:0 -show_entries stream=width,height '
             f'-of csv=p=0:s=x "{path}"')
    w, h = out.split("x")[:2]
    return int(w), int(h)


def has_audio(path):
    return bool(sh(f'ffprobe -v error -select_streams a -show_entries stream=index '
                   f'-of csv=p=0 "{path}"'))


def build_overlay(w, h, dest):
    """Same three magick steps as applyTiledWatermark(), at video dimensions."""
    logo_px = round(w * LOGO_PCT)
    tmp = dest + ".logo.png"
    try:
        sh(f'magick -background none "{LOGO}" -resize {logo_px}x -rotate {ROTATE} '
           f'-alpha set -channel A -evaluate multiply {OPACITY} +channel "{tmp}"')
        lw, lh = sh(f'magick identify -format "%wx%h" "{tmp}"').split("x")
        pw, ph = round(int(lw) * SPACING_FACTOR), round(int(lh) * SPACING_FACTOR)
        sh(f'magick "{tmp}" -gravity center -background none -extent {pw}x{ph} "{tmp}"')
        sh(f'magick -size {w}x{h} tile:"{tmp}" "{dest}"')
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)


def watermark(src, dest):
    w, h = probe(src)
    overlay = dest + ".overlay.png"
    try:
        build_overlay(w, h, overlay)
        amap = '-map 0:a? -c:a copy' if has_audio(src) else '-an'
        sh(f'ffmpeg -y -v error -i "{src}" -i "{overlay}" '
           f'-filter_complex "[0:v][1:v]overlay=0:0:format=auto[v]" -map "[v]" {amap} '
           f'-c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p '
           f'-movflags +faststart "{dest}"')
    finally:
        if os.path.exists(overlay):
            os.remove(overlay)


# The four moved out of the folder root on 2026-09-22. Kept explicit so a bare run
# does not quietly watermark unrelated assets that happen to match <id>/<id>.mp4 —
# cg_hunter did exactly that on the first run. Use --all to sweep everything.
MANAGED = ["beauty_cream", "fabric_ad", "matcha_drink", "rotation_chair"]


def targets(only=None, everything=False):
    """Per-id folders holding <id>/<id>.mp4. Root-level files are left alone."""
    names = sorted(os.listdir(HERE)) if (everything or only) else MANAGED
    for name in names:
        d = os.path.join(HERE, name)
        if not os.path.isdir(d) or (only and name != only):
            continue
        src = os.path.join(d, f"{name}.mp4")
        if os.path.exists(src):
            yield name, src, os.path.join(d, f"{name}-watermarked.mp4")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("only", nargs="?")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--all", action="store_true",
                    help="sweep every <id>/<id>.mp4, not just MANAGED")
    a = ap.parse_args()

    if not os.path.exists(LOGO):
        sys.exit(f"logo not found: {LOGO}")

    found = 0
    for name, src, dest in targets(a.only, a.all):
        found += 1
        if os.path.exists(dest) and not a.force and os.path.getmtime(dest) > os.path.getmtime(src):
            print(f"skip  {name} (up to date)")
            continue
        watermark(src, dest)
        w, h = probe(dest)
        mb = os.path.getsize(dest) / 1e6
        print(f"wrote {name}-watermarked.mp4  {w}x{h}  {mb:.1f}MB")
    if not found:
        sys.exit("no <id>/<id>.mp4 found")


if __name__ == "__main__":
    main()
