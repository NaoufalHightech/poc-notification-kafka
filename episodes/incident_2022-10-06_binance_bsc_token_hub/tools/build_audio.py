#!/usr/bin/env python3
"""Synthétise la musique de fond et les effets (assets/music, assets/sfx), place la voix, mixe -> build/mix.wav.
Tout est généré par du code (numpy), sans échantillon externe : aucun droit à gérer."""
import subprocess, wave, sys
import numpy as np
from common import *
rng = np.random.default_rng(42)
def t_(d): return np.arange(int(d * SR)) / SR
def lp(x, k):  # moyenne glissante = passe-bas simple
    c = np.cumsum(np.insert(x, 0, 0)); return (c[k:] - c[:-k]) / k if k > 1 else x
def wavw(path, x):
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes())
def env(n, a=0.005, r=0.2): e = np.minimum(np.arange(n) / (a * SR + 1), 1) * np.exp(-np.arange(n) / (r * SR)); return e
# ---- effets
def whoosh(): n = int(0.7 * SR); x = rng.normal(0, 1, n); x = x - lp(x, 40)[: n] if False else x; y = np.convolve(x, np.ones(60) / 60, "same"); e = np.sin(np.linspace(0, np.pi, n)) ** 2; return y * e * 0.9
def ping(): t = t_(0.9); return (np.sin(2 * np.pi * 1320 * t) + 0.4 * np.sin(2 * np.pi * 1980 * t)) * env(len(t), 0.002, 0.18) * 0.5
def alert(): t = t_(0.7); f = np.where(t < 0.3, 880, 660); return np.sign(np.sin(2 * np.pi * f * t)) * 0.18 * env(len(t), 0.003, 0.5) * (1 + 0 * t)
def hit(): t = t_(1.2); return (np.sin(2 * np.pi * (70 - 25 * t) * t) * 1.0 + rng.normal(0, 0.15, len(t))) * env(len(t), 0.002, 0.28) * 0.9
def tick(): n = int(0.02 * SR); return rng.normal(0, 1, n) * np.exp(-np.arange(n) / (0.004 * SR)) * 0.35
def glitch():
    x = np.zeros(int(0.45 * SR))
    for s in (0.0, 0.08, 0.17, 0.26):
        n = int(rng.uniform(0.02, 0.07) * SR); i = int(s * SR); x[i:i + n] += rng.normal(0, 1, n) * np.exp(-np.arange(n) / (0.02 * SR)) * 0.6
    return x
def blip(): t = t_(0.12); return np.sin(2 * np.pi * 1800 * t) * env(len(t), 0.001, 0.03) * 0.3
SFX = dict(whoosh=whoosh, ping=ping, alert=alert, hit=hit, tick=tick, glitch=glitch, blip=blip)
sfx = {k: f() for k, f in SFX.items()}
for k, v in sfx.items(): wavw(ASSETS / "sfx" / f"{k}.wav", v / (np.abs(v).max() + 1e-9) * 0.9)
# ---- musique : nappe sombre, deux battements lents, légère dérive
tl = timeline(); total = tl["total"] + 3; n = int(total * SR); t = np.arange(n) / SR
m = np.zeros(n)
for f0, g in ((55.0, 0.5), (82.41, 0.3), (110.0, 0.22), (164.81, 0.1)):
    for det in (-0.4, 0.4): m += g * np.sin(2 * np.pi * (f0 + det) * t + 0.3 * np.sin(2 * np.pi * 0.05 * t))
m *= 0.55 + 0.45 * np.sin(2 * np.pi * t / 23.0) ** 2
pulse = np.zeros(n)
for bt in np.arange(2.0, total - 1, 4.0): i = int(bt * SR); k = min(int(1.5 * SR), n - i); pulse[i:i + k] += np.sin(2 * np.pi * 41 * np.arange(k) / SR) * np.exp(-np.arange(k) / (0.35 * SR))
noise = np.convolve(rng.normal(0, 1, n), np.ones(200) / 200, "same") * 8 * (0.3 + 0.3 * np.sin(2 * np.pi * t / 17.0))
music = (m * 0.5 + pulse * 0.6 + noise * 0.12); music /= np.abs(music).max()
wavw(BUILD / "music_raw.wav", music)
(ASSETS / "music").mkdir(parents=True, exist_ok=True)
subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", str(BUILD / "music_raw.wav"), "-ac", "1", "-b:a", "96k", str(ASSETS / "music" / "ambient_dark.mp3")])
# ---- voix + effets
def load(path):
    out = BUILD / "voice_norm" / (pathlib.Path(path).stem + ".wav"); out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", str(EP / path), "-ac", "1", "-ar", str(SR), str(out)])
    with wave.open(str(out)) as w: return np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
voice = np.zeros(n); fx = np.zeros(n); duck = np.zeros(n)
def put(buf, x, at, g=1.0):
    i = int(at * SR); 
    if i < 0 or i >= n: return
    k = min(len(x), n - i); buf[i:i + k] += x[:k] * g
for l in tl["lines"]:
    s = l["start"]; v = load(l["voice"]); put(voice, v, s + LEAD); duck[int((s + LEAD) * SR): int((s + LEAD) * SR) + len(v)] = 1
    kind, fl, kv = parse_rendu(l["rendu"]); put(fx, sfx["whoosh"], s, 0.22)
    if "glitch" in fl: put(fx, sfx["glitch"], s + 0.05, 0.5); put(fx, sfx["hit"], s + 0.05, 0.35)
    if kind == "terminal":
        nch = sum(len(x) for x in kv.get("lines", "").split("|"))
        for c in range(0, nch + 3 * len(kv.get("lines", "").split("|")), 2): put(fx, sfx["tick"], s + TERM_START + c / TERM_CPS, 0.5)
        if l["id"] == "L01": put(fx, sfx["alert"], s + TERM_START + nch / TERM_CPS + 0.4, 0.5)
    if kind == "bignum": put(fx, sfx["hit"], s + 0.4, 0.4)
    if kind == "timeline": put(fx, sfx["ping"], s + 0.2, 0.5)
    if kind == "chart" and kv.get("mode") == "spike": put(fx, sfx["alert"], s + 0.3 + 5.5 * 0.5, 0.5); put(fx, sfx["alert"], s + 0.3 + 5.5 * 0.72, 0.5)
    if kind == "diagram" and kv.get("stage") == "6": [put(fx, sfx["alert"], s + 0.6 + i * 0.35, 0.3) for i in range(9)]
    if kind == "diagram" and kv.get("stage") == "5": put(fx, sfx["hit"], s + 3.0, 0.5)
    if kind == "quote": put(fx, sfx["blip"], s + 0.4, 0.5)
k = int(0.35 * SR); duck = np.convolve(duck, np.ones(k) / k, "same")
mix = voice * 1.0 + fx * 0.55 + music * (0.26 - 0.17 * duck)
mix /= max(1.0, np.abs(mix).max() / 0.95); wavw(BUILD / "mix.wav", mix); print("mix.wav", round(total), "s")
