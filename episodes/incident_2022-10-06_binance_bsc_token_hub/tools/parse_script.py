#!/usr/bin/env python3
"""script.md (tableaux | Lnn | Expression | Texte | Écran |) + scenes.md (colonne Rendu) -> build/script.json."""
import json, re, sys, pathlib
ep = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
def rows(path):
    scene = None
    for ln in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"#{2,3} Scène (\d+) : (.*)", ln)
        if m: scene = (int(m.group(1)), m.group(2).strip()); continue
        if re.match(r"\| L\d+ \|", ln):
            cells = [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", ln.strip())[1:-1]]
            yield scene, cells
rendu = {c[0]: c[2].strip("`") for _, c in rows(ep / "scenes.md")}
out = []
for scene, c in rows(ep / "script.md"):
    out.append(dict(id=c[0], scene=scene[0], section=scene[1], expr=c[1], texte=c[2], visuel=c[3], rendu=rendu[c[0]]))
(ep / "build").mkdir(exist_ok=True)
(ep / "build" / "script.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(out), "lignes,", sum(len(l["texte"].split()) for l in out), "mots")
