#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
ffmpeg -hide_banner -loglevel error -i jade-portal-15s-source.mp4 -t 15 -vf 'crop=756:1344,scale=720:1280,setsar=1' -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -af 'loudnorm=I=-16:TP=-1.5:LRA=11' -c:a aac -b:a 192k -movflags +faststart jade-portal-15s.mp4 -y
ffmpeg -hide_banner -loglevel error -ss 13.8 -i jade-portal-15s.mp4 -frames:v 1 cover.jpg -y
ffmpeg -hide_banner -loglevel error -i jade-portal-15s.mp4 -vf 'fps=1,scale=180:-1,tile=5x3' -frames:v 1 qa-contact.jpg -y
ffmpeg -hide_banner -loglevel error -i jade-portal-15s.mp4 -f null -
