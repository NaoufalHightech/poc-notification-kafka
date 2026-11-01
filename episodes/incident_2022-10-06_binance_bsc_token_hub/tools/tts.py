#!/usr/bin/env python3
"""Voix off locale : Piper (voix fr_FR 'tom', licence MIT). Écrit assets/voice/Lxx.wav.
Le modèle (~60 Mo) est téléchargé une fois dans ~/.cache/incident_log_tts (non versionné).
Dépendance : pip install piper-tts"""
import json, os, pathlib, subprocess, sys, wave
from piper import PiperVoice, SynthesisConfig
ep = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
cache = pathlib.Path(os.path.expanduser("~/.cache/incident_log_tts")); cache.mkdir(parents=True, exist_ok=True)
name = "vits-piper-fr_FR-tom-medium"; mdir = cache / name
if not mdir.exists():  # archive publiée par le projet sherpa-onnx (mêmes poids que rhasspy/piper-voices)
    tgz = cache / (name + ".tar.bz2")
    subprocess.check_call(["curl", "-fsSL", "-o", str(tgz), f"https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/{name}.tar.bz2"])
    subprocess.check_call(["tar", "xjf", str(tgz), "-C", str(cache)])
voice = PiperVoice.load(str(mdir / "fr_FR-tom-medium.onnx"))
cfg = SynthesisConfig(length_scale=1.12, noise_scale=0.6, noise_w_scale=0.7)  # un peu plus lent et posé
out = ep / "assets" / "voice"; out.mkdir(parents=True, exist_ok=True)
for l in json.loads((ep / "build" / "script.json").read_text()):
    f = out / f"{l['id']}.wav"
    if f.exists(): continue
    with wave.open(str(f), "wb") as w: voice.synthesize_wav(l["texte"], w, cfg)
    with wave.open(str(f)) as w: print(l["id"], round(w.getnframes() / w.getframerate(), 1), "s", flush=True)
