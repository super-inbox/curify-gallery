#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
ffmpeg -hide_banner -y -i source.mp4 -vf 'crop=1024:400:0:80,pad=1024:576:0:88:black,setsar=1' -c:v libx264 -crf 18 -preset medium -c:a copy -movflags +faststart stadium-camera-move-clean.mp4
