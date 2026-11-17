#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
ffmpeg -hide_banner -loglevel error -i source.mp4 -vf 'crop=720:1120:0:80,pad=720:1280:0:80:black,setsar=1' -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a copy -movflags +faststart -y friends-then-and-now-rednote-clean.mp4
ffmpeg -hide_banner -loglevel error -ss 2 -i friends-then-and-now-rednote-clean.mp4 -frames:v 1 -y cover.jpg
ffmpeg -hide_banner -loglevel error -i friends-then-and-now-rednote-clean.mp4 -vf 'fps=1/5,scale=180:-1,tile=5x3' -frames:v 1 -y qa-contact.jpg
ffmpeg -hide_banner -loglevel error -i friends-then-and-now-rednote-clean.mp4 -f null -
