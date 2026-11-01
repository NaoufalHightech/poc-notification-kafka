# INCIDENT LOG · Binance : le pont qui a cru une fausse preuve (6 octobre 2022)

Épisode autonome de la chaîne **artificiel-intelligence**, au format de la branche `incident_log` du dépôt `motions` (`script.md` en tableaux `| Lnn | Expression | Texte | Écran |`, un dossier `incident_<date>_<sujet>`).

| Fichier | Rôle |
|---|---|
| `script.md` | Script narratif : titres YouTube, règles de rigueur, description de la voix, 8 scènes, sources, « À vérifier » |
| `scenes.md` | Charte visuelle/sonore, découpage par scène et consigne de rendu (colonne **Rendu**) de chaque ligne |
| `config.json` | Métadonnées YouTube : titre, description (avec sources), tags, chapitres (recalculés au rendu) |
| `render.sh` | Rendu complet vers `build/<slug>.mp4` (Pillow + numpy pour les images, ffmpeg pour l'assemblage) |
| `assets/voice/` | **Tes voix** `L01.wav` … `L31.wav` (ignorées par Git) |
| `assets/music/`, `assets/sfx/` | Nappe sombre et effets, synthétisés par `tools/build_audio.py` |
| `assets/visuals/thumbnail.jpg` | Miniature |
| `tools/` | `parse_script.py`, `tts.py` (voix de repère), `timeline.py`, `build_audio.py`, `render_video.py`, `make_thumbnail.py` |

## Utiliser ta voix

1. Enregistre chaque ligne du tableau de `script.md` (colonne *Texte*, expression indiquée) dans `assets/voice/Lxx.wav` (`.mp3`, `.flac`, `.m4a` acceptés).
2. `./render.sh` : la timeline se recale sur les durées réelles, les sous-titres, les effets sonores et les chapitres de `config.json` suivent. Durée visée : 5 à 8 min (le script actuel donne environ 6 min 20).
3. Sans fichier dans `assets/voice/`, `render.sh` génère une voix de repère (Piper « tom », MIT) pour caler le montage.

## Si tu modifies le texte

Change la ligne dans `script.md`, réenregistre `Lxx`, relance `./render.sh`. Pour une nouvelle consigne visuelle, édite la colonne **Rendu** de `scenes.md` (`terminal`, `bignum`, `diagram stage=0..6`, `chart mode=flat|spike|range`, `timeline upto=0..3`, `quote` ; drapeaux `glitch`, `scan`).

## Rigueur

Incident réel et public. Les logs affichés sont des **reconstitutions simulées** (annoncé dans l'épisode). Voir « À vérifier avant enregistrement » dans `script.md` avant de publier.
