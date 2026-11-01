#!/usr/bin/env python3
"""Lit les voix assets/voice/Lxx.(wav|mp3|flac|m4a), calcule la timeline, met à jour les chapitres de config.json.
Si tu remplaces les voix par les tiennes, relance render.sh : tout se recale sur les durées réelles."""
import json, sys
from common import *
script = json.loads((BUILD / "script.json").read_text())
PAD = {"L03": 1.2, "L09": 1.3, "L20": 1.4, "L25": 1.6, "L31": 2.5}
t, out = 1.0, []
for l in script:
    vf = next((p for ext in ("wav", "mp3", "flac", "m4a", "ogg") for p in [ASSETS / "voice" / f"{l['id']}.{ext}"] if p.exists()), None)
    if vf is None: sys.exit(f"voix manquante pour {l['id']} (assets/voice/{l['id']}.wav)")
    d = duration(vf); total = LEAD + d + PAD.get(l["id"], 0.8)
    out.append({**l, "voice": str(vf.relative_to(EP)), "voice_dur": round(d, 3), "start": round(t, 3), "dur": round(total, 3)})
    t += total
end = round(t, 3)
(BUILD / "timeline.json").write_text(json.dumps({"total": end, "lines": out}, ensure_ascii=False, indent=1))
def mmss(s): return f"{int(s//60)}:{int(s%60):02d}"
first = {}
for l in out: first.setdefault(l["section"], l["start"])
chapters = [{"time": mmss(0 if i == 0 else s), "seconds": int(0 if i == 0 else s), "title": n} for i, (n, s) in enumerate(first.items())]
cp = EP / "config.json"; cfg = json.loads(cp.read_text()); cfg["duration_seconds"] = int(end); cfg["duration"] = mmss(end); cfg["chapters"] = chapters
cp.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n")
print(f"durée totale {mmss(end)} ({end:.0f}s)", "OK" if 300 <= end <= 480 else "HORS 5-8 min !")
