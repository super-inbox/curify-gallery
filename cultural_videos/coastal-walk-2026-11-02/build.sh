#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
source_video="${1:-/Users/qqwjq/Desktop/Weixin Videos2026-10-13_193444_737.mp4}"
ffmpeg -hide_banner -loglevel error -i "$source_video" -vf 'crop=630:1120:44:80,scale=720:1280:flags=lanczos,setsar=1' -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -c:a copy -movflags +faststart -y ../../drama_animation/coastal-walk-10s-cropped.mp4
ffmpeg -hide_banner -loglevel error -ss 1 -i ../../drama_animation/coastal-walk-10s-cropped.mp4 -frames:v 1 -y cover.jpg
ffmpeg -hide_banner -loglevel error -i ../../drama_animation/coastal-walk-10s-cropped.mp4 -vf 'fps=1,scale=216:-1,tile=5x2' -frames:v 1 -y qa-contact.jpg
ffmpeg -hide_banner -loglevel error -i ../../drama_animation/coastal-walk-10s-cropped.mp4 -f null -
