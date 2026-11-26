#!/usr/bin/env bash
# Build THE ASH-SMEARED HEART from source: picture + score -> the_ash_smeared_heart.mp4
set -euo pipefail
cd "$(dirname "$0")"
python3 audio.py
python3 render.py video
ffmpeg -y -loglevel error -i build/video.mp4 -i build/audio.wav \
  -map 0:v -map 1:a -c:v copy -af "loudnorm=I=-16:TP=-1.5:LRA=14" -c:a aac -b:a 192k \
  -movflags +faststart -shortest the_ash_smeared_heart.mp4
echo "done: the_ash_smeared_heart.mp4"
