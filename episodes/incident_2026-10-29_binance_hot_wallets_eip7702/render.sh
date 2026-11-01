#!/usr/bin/env bash
# Rendu ffmpeg de l'épisode (fond incident_log : scanlines, vignette, grain, horloge, surimpression).
#   ./render.sh                  # voix dans assets/voice/Bxx.wav -> build/<slug>.mp4 ; sans voix : aperçu muet chronométré à 150 mots/min
#   LIMIT=90 ./render.sh         # n'encode que les 90 premières secondes (test rapide)
#   WPM=155 ./render.sh          # cadence d'estimation quand il n'y a pas de voix
# Dépend de : python3, ffmpeg (libass, drawtext, DejaVu Sans Mono). Les visuels détaillés ([VISUEL: …]) se montent par-dessus ce fond.
set -euo pipefail
cd "$(dirname "$0")"
SLUG="$(basename "$PWD")"; W=1280; H=720; FPS=24
FONT="${FONT:-/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf}"
python3 tools/build_meta.py --wpm "${WPM:-150}"
TOTAL="$(python3 -c "import json;print(json.load(open('build/blocks.json'))['total'])")"
DUR="${LIMIT:-$TOTAL}"
mkdir -p build/gaps
while read -r g; do [ -f "build/gaps/$g.wav" ] || ffmpeg -nostdin -y -loglevel error -f lavfi -i "anullsrc=r=44100:cl=mono" -t "$g" -c:a pcm_s16le "build/gaps/$g.wav"; done < build/gaps.txt
# 1) piste voix : concaténation des fichiers voix + silences ; sans voix -> silence de la durée totale
if ls assets/voice/B01.* >/dev/null 2>&1; then
  ffmpeg -y -loglevel error -f concat -safe 0 -i build/voice_concat.txt -ar 44100 -ac 1 -c:a pcm_s16le build/voice.wav
else
  echo ">> aucune voix dans assets/voice : aperçu muet (durées estimées)"
  ffmpeg -y -loglevel error -f lavfi -i "anullsrc=r=44100:cl=mono" -t "$TOTAL" -c:a pcm_s16le build/voice.wav
fi
# 2) nappe sombre synthétisée + ducking sous la voix + normalisation -14 LUFS
ffmpeg -y -loglevel error -i build/voice.wav -f lavfi -i "aevalsrc='0.5*sin(2*PI*55*t)+0.3*sin(2*PI*82.41*t)+0.2*sin(2*PI*110*t)+0.08*sin(2*PI*164.81*t)':s=44100:d=${DUR}" \
  -filter_complex "[1:a]tremolo=f=0.1:d=0.5,lowpass=f=400,volume=0.55[m];[0:a]asplit[v1][v2];[m][v2]sidechaincompress=threshold=0.02:ratio=8:attack=60:release=700[md];[v1][md]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
  -map "[a]" -t "$DUR" -ar 44100 -c:a pcm_s16le build/mix.wav
# 3) vidéo : fond sombre + grain + scanlines + vignette + en-tête + horloge + surimpression ASS
ffmpeg -y -loglevel error -f lavfi -i "color=c=0x07090c:s=${W}x${H}:r=${FPS}:d=${DUR}" -i build/mix.wav \
  -vf "noise=alls=7:allf=t,drawgrid=w=0:h=3:t=1:c=black@0.28,vignette=PI/5,\
drawbox=x=0:y=0:w=${W}:h=56:color=black@0.45:t=fill,\
drawtext=fontfile=${FONT}:text='INCIDENT LOG':fontcolor=0xff6a00:fontsize=22:x=40:y=18,\
drawtext=fontfile=${FONT}:text='BINANCE · 29 OCT. 2026 · UTC+3 (LA MECQUE)':fontcolor=0x00e5ff:fontsize=18:x=250:y=21,\
drawtext=fontfile=${FONT}:text='%{pts\:hms}':fontcolor=0x00e5ff@0.8:fontsize=18:x=w-130:y=21,\
subtitles=build/overlay.ass" \
  -c:v libx264 -preset "${PRESET:-veryfast}" -crf 22 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart "build/${SLUG}.mp4"
echo "OK -> build/${SLUG}.mp4 ($(ffprobe -v error -show_entries format=duration -of csv=p=0 "build/${SLUG}.mp4") s)"
