"""Constantes et utilitaires partagés (rendu vidéo + audio)."""
import json, pathlib, re, subprocess
EP = pathlib.Path(__file__).resolve().parent.parent
BUILD = EP / "build"; ASSETS = EP / "assets"
W, H, FPS, SR = 1280, 720, 24, 44100
LEAD = 0.35          # silence avant la voix dans chaque ligne
TERM_START, TERM_CPS = 0.5, 42.0   # démarrage et vitesse de frappe du terminal

def parse_rendu(s):
    toks = re.findall(r'(\w+)="([^"]*)"|(\w+)=(\S+)|(\w+)', s)
    kind, flags, kv = None, set(), {}
    for a, b, c, d, e in toks:
        if a: kv[a] = b
        elif c: kv[c] = d
        elif e:
            if kind is None: kind = e
            else: flags.add(e)
    return kind, flags, kv

def duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)], capture_output=True, text=True, check=True)
    return float(r.stdout.strip())

def timeline():
    return json.loads((BUILD / "timeline.json").read_text())
