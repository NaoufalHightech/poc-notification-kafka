#!/usr/bin/env python3
"""script.md -> chapters.json (YouTube), build/blocks.json, build/overlay.ass, build/voice_concat.txt.
Durées : fichiers assets/voice/Bxx.(wav|mp3|flac|m4a) s'ils existent, sinon estimation à 150 mots/min.
Usage : build_meta.py [--wpm 150]   (affiche le compte de mots et la durée ; échoue si < 30 min ou < 5 500 mots)"""
import json, pathlib, re, subprocess, sys
EP = pathlib.Path(__file__).resolve().parent.parent
B = EP / "build"; B.mkdir(exist_ok=True)
WPM = float(sys.argv[sys.argv.index("--wpm") + 1]) if "--wpm" in sys.argv else 150.0
GAP = 0.35  # respiration entre deux blocs
TITLES = dict(A="Cold open : 00 h 42 min 59 s", B="Mise en place de l'enquête", C="Avant de comprendre le vol : blockchain, clés, nonce", D="La préparation de l'attaquant (36 h 25 min)", E="Chronologie minute par minute : le test, la frappe, la fuite", F="La faille : EIP-7702 et les trois détails qui tuent", G="La riposte : les boutons d'urgence", H="Attribution et cinq questions ouvertes", I="Bilan chiffré et conclusion")
text = (EP / "script.md").read_text(encoding="utf-8")

def voice_for(bid):
    for ext in ("wav", "mp3", "flac", "m4a", "ogg"):
        p = EP / "assets" / "voice" / f"{bid}.{ext}"
        if p.exists(): return p
def probe(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)], capture_output=True, text=True, check=True)
    return float(r.stdout)

sections, blocks, sec = [], [], None
for ln in text.splitlines():
    m = re.match(r"## ([A-I])\. (.+?) \((\d+:\d\d) – (\d+:\d\d)\)", ln)
    if m: sec = dict(letter=m.group(1), title=m.group(2).title().replace("Et ", "et "), target=m.group(3)); sections.append(sec); continue
    m = re.match(r"#### (B\d+) · (.*)", ln)
    if m: blocks.append(dict(id=m.group(1), title=m.group(2), section=sec["letter"], screen="", pause=0.0, words=0, narr=[])); continue
    if not blocks or ln.startswith(("---", "## ", "*")) or not ln.strip(): continue
    b = blocks[-1]
    if ln.startswith("[TEXTE À L'ÉCRAN:"): b["screen"] = re.sub(r'^\[TEXTE À L\'ÉCRAN:\s*"?(.*?)"?\]$', r"\1", ln.strip())
    elif ln.startswith("[PAUSE:"): b["pause"] += float(re.search(r"([\d.]+)s", ln).group(1))
    elif ln.startswith("["): pass
    else: b["narr"].append(ln.strip())
t, total_words, real = 0.0, 0, 0
for b in blocks:
    b["words"] = len(" ".join(b["narr"]).split()); total_words += b["words"]
    vp = voice_for(b["id"]); b["voice"] = str(vp.relative_to(EP)) if vp else None
    est = b["words"] / WPM * 60.0
    dur = probe(vp) if vp else est; real += bool(vp)
    b["start"] = round(t, 2); b["voice_dur"] = round(dur, 2); b["dur"] = round(dur + b["pause"] + GAP, 2); t += b["dur"]
total = round(t, 1)
def hms(s): s = int(s); return f"{s//3600}:{s%3600//60:02d}:{s%60:02d}" if s >= 3600 else f"{s//60}:{s%60:02d}"
first = {}
for b in blocks: first.setdefault(b["section"], b["start"])
names = {s["letter"]: s["title"] for s in sections}
chapters = [dict(time=hms(0 if i == 0 else first[s["letter"]]), seconds=int(0 if i == 0 else first[s["letter"]]), title=TITLES[s["letter"]]) for i, s in enumerate(sections)]
(EP / "chapters.json").write_text(json.dumps(dict(video="incident_2026-10-29_binance_hot_wallets_eip7702", timezone="UTC+3", total=hms(total), total_seconds=int(total), mode="voix réelle" if real == len(blocks) else f"estimation ({real}/{len(blocks)} voix)", chapters=chapters), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(B / "blocks.json").write_text(json.dumps(dict(total=total, blocks=blocks), ensure_ascii=False, indent=1), encoding="utf-8")
# ---- surimpression ASS : texte à l'écran (cyan) + cartons de section (orange)
def ass_t(s): return f"{int(s//3600)}:{int(s%3600//60):02d}:{s%60:05.2f}"
head = """[Script Info]
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Screen,DejaVu Sans Mono,38,&H00FFFF00,&H00FFFFFF,&H00000000,&H80000000,1,0,0,0,100,100,0,0,1,2,0,5,60,60,40,1
Style: Card,DejaVu Sans Mono,54,&H00008CFF,&H00FFFFFF,&H00000000,&H80000000,1,0,0,0,100,100,2,0,1,2,0,5,60,60,40,1
[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""
ev = []
for b in blocks:
    if b["screen"]:
        start = b["start"] + 0.5 + (3.0 if first[b["section"]] == b["start"] else 0)
        end = min(b["start"] + b["dur"] - 0.3, start + 9)
        if end > start: ev.append(f"Dialogue: 0,{ass_t(start)},{ass_t(end)},Screen,,0,0,0,,{{\\fad(200,300)}}{b['screen'].replace(chr(92), '').replace('{', '(').replace('}', ')')}")
    if first[b["section"]] == b["start"]:
        ev.append(f"Dialogue: 1,{ass_t(b['start'])},{ass_t(b['start'] + 3)},Card,,0,0,0,,{{\\fad(300,400)}}{b['section']}. {names[b['section']].upper()}")
(B / "overlay.ass").write_text(head + "\n".join(ev) + "\n", encoding="utf-8")
# ---- liste de concaténation de la voix (avec silences)
lines = []
for b in blocks:
    if b["voice"]: lines.append(f"file '{EP / b['voice']}'")
    gap = round(b["pause"] + GAP, 2); lines.append(f"file '{B / 'gaps' / (str(gap) + '.wav')}'")
(B / "voice_concat.txt").write_text("\n".join(lines) + "\n")
gaps = sorted({round(b["pause"] + GAP, 2) for b in blocks}); (B / "gaps.txt").write_text("\n".join(str(g) for g in gaps) + "\n")
(EP / "voice_lines.md").write_text("# Lignes à enregistrer (un fichier par bloc : assets/voice/Bxx.wav)\n\n" + "\n".join(f"**{b['id']}** · {b['title']}  \n{' '.join(b['narr'])}\n" for b in blocks), encoding="utf-8")
print(f"{len(blocks)} blocs · {total_words} mots · durée {hms(total)} ({int(total)} s) · mode : {'voix réelle' if real == len(blocks) else f'estimation, {real}/{len(blocks)} voix'}")
ok = total_words >= 5500 and total >= 30 * 60
print("OK (≥ 5 500 mots et ≥ 30 min)" if ok else "ÉCHEC : < 5 500 mots ou < 30 min")
sys.exit(0 if ok else 1)
