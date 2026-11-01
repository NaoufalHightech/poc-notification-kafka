#!/usr/bin/env bash
# Rendu complet de l'épisode : script -> voix -> timeline -> audio -> vidéo -> MP4 final (ffmpeg).
# Prérequis : python3 (numpy, Pillow), ffmpeg/ffprobe, police DejaVu. Voix de repère : pip install piper-tts.
# Ta voix : dépose assets/voice/L01.wav ... L31.wav (ou .mp3/.flac/.m4a) puis relance ./render.sh :
# la timeline, les sous-titres, les effets et les chapitres se recalent sur les durées réelles.
set -euo pipefail
cd "$(dirname "$0")"
SLUG="$(basename "$PWD")"
python3 tools/parse_script.py .                       # script.md + scenes.md -> build/script.json
if ! ls assets/voice/L01.* >/dev/null 2>&1; then      # pas de voix fournie : voix de repère (Piper)
  echo ">> aucune voix dans assets/voice : génération de la voix de repère"; python3 tools/tts.py .
fi
python3 tools/timeline.py                             # durées -> build/timeline.json + chapitres de config.json
python3 tools/build_audio.py                          # musique, effets, mixage -> build/mix.wav
python3 tools/make_thumbnail.py                       # assets/visuals/thumbnail.jpg
python3 tools/render_video.py                         # images -> build/video_silent.mp4
ffmpeg -y -loglevel error -i build/video_silent.mp4 -i build/mix.wav \
  -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart "build/${SLUG}.mp4"
echo "OK -> build/${SLUG}.mp4 ($(ffprobe -v error -show_entries format=duration -of csv=p=0 "build/${SLUG}.mp4") s)"
