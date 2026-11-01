# Scènes · INCIDENT LOG · Binance, le pont qui a cru une fausse preuve

Découpage de montage et instructions de rendu. `script.md` porte le texte, `scenes.md` porte le visuel, le son et la consigne machine lue par `tools/render_video.py` (colonne **Rendu**).

## Charte visuelle et sonore (commune à toutes les scènes)

- **Cadre** : 1280×720, 24 i/s ; fond quasi noir `#07090c`, vert terminal `#39ff88` (OK), ambre `#ffb000` (horodatages), rouge `#ff3b4e` (anomalie), gris `#5b6b78` (contexte).
- **Bandeau haut** : « INCIDENT LOG · BINANCE / BSC TOKEN HUB » à gauche, partie narrative à droite. **Bas** : sous-titres de la voix, identifiant de ligne et timecode.
- **Couche constante** : scanlines légères, vignettage, grain. **Tension** (drapeau `glitch`) : tranches horizontales décalées, séparation RVB, scanlines renforcées.
- **Texte à l'écran** : horodatages UTC en ambre, noms de fichiers/logs en monospace, citations courtes ; tout log est marqué *reconstitution*.
- **Son** : nappe sombre synthétisée (`assets/music/`), volume bas sous la voix ; effets (`assets/sfx/`) : whoosh discret à chaque ligne, bips d'alerte, impacts graves, clics de frappe, ping de timeline, bruit de glitch.
- **Voix** : fichiers `assets/voice/Lxx.wav` (ou .mp3/.flac/.m4a). Le montage se recale sur leur durée réelle.

## Types de rendu

`terminal` (log tapé ligne à ligne) · `bignum` (grand nombre / horodatage + légende) · `diagram` (pont Beacon Chain ↔ Smart Chain, `stage` 0 à 6) · `chart` (`flat`, `spike`, `range`) · `timeline` (`upto` = dernier événement allumé) · `quote` (carte de texte, lignes séparées par `|`).

## Scène 0 : Cold open : le pont dit oui

Partie : Hook. Lignes : L01 à L03.

| N° | Visuel (intention) | Rendu |
|---|---|---|
| L01 | écran noir, un curseur clignote ; la ligne de log "proof OK" apparaît en vert | `terminal glitch lines="06 oct. 2022 · token-hub · relay request received\|verify_proof(IAVL) ... OK\|status: ACCEPTED"` |
| L02 | compteur géant 2 000 000 BNB, la valeur en dollars apparaît en dessous | `bignum glitch big="2 000 000 BNB" small="≈ 570 millions de dollars (estimation de l'époque)"` |
| L03 | deux cases barrées "clé privée volée" et "mot de passe cassé", puis "preuve acceptée" en rouge | `quote glitch text="Aucune clé volée.\|Aucun mot de passe cassé.\|Le système a cru ce qu'on lui montrait."` |

## Scène 1 : Le contexte : un pont entre deux chaînes

Partie : Contexte. Lignes : L04 à L09.

| N° | Visuel (intention) | Rendu |
|---|---|---|
| L04 | bandeau "RECONSTITUTION" sur fond de grille, sources listées | `quote text="Reconstitution à partir d'analyses publiques.\|Les logs affichés sont simulés.\|Sources : description."` |
| L05 | deux blocs, Beacon Chain et Smart Chain, reliés par un pont "Token Hub" | `diagram stage=0` |
| L06 | cadenas sur la Beacon Chain, jetons créés sur la Smart Chain, total constant | `diagram stage=1` |
| L07 | la Smart Chain "aveugle", une preuve Merkle arrive, module IAVL en surbrillance | `diagram stage=2` |
| L08 | séquence de quatre étapes qui s'allument : verrouiller, relayer, vérifier, créer | `diagram stage=3` |
| L09 | courbe d'activité plate et verte, mention "aucune alerte" | `chart mode=flat label="créations de BNB par heure · ligne de base"` |

## Scène 2 : Avant l'attaque : le bruit de fond

Partie : Chronologie. Lignes : L10 à L11.

| N° | Visuel (intention) | Rendu |
|---|---|---|
| L10 | timeline, premier point : 5 octobre, petite somme reçue par une adresse neuve | `timeline upto=0` |
| L11 | log banal, rien ne bouge, une ligne se surligne doucement | `terminal lines="05 oct. · transfer 100 BNB -> 0x…(new address)\|balance check ... OK\|no anomaly flagged"` |

## Scène 3 : La soirée du 6 octobre

Partie : Chronologie. Lignes : L12 à L17.

| N° | Visuel (intention) | Rendu |
|---|---|---|
| L12 | timeline, deuxième point : jeudi 6 octobre, soirée UTC ; le log s'accélère | `timeline upto=1 scan` |
| L13 | log, "verify_proof ... OK" en vert, puis "mint 1 000 000 BNB" en rouge | `terminal glitch lines="relay request #1\|verify_proof(IAVL) ... OK\|mint 1,000,000 BNB -> attacker\|status: CONFIRMED"` |
| L14 | horodatage 20:43:xx UTC en gros, second mint | `bignum glitch big="20:43 UTC" small="2e création · 1 000 000 BNB (selon un suivi public)"` |
| L15 | graphe de l'offre qui monte en escalier, deux marches | `chart mode=spike label="créations de BNB · 6 oct. 2022"` |
| L16 | flux sortants depuis l'adresse vers d'autres chaînes, flèches multiples | `diagram stage=4 glitch` |
| L17 | deux jauges divergentes : "sorti de la chaîne" vs "resté bloqué" ; mention "les sources divergent" | `chart mode=range label="sorti de la chaîne : 100 à 130 M$ (premières estimations)"` |

## Scène 4 : La suspension de la chaîne

Partie : Chronologie. Lignes : L18 à L20.

| N° | Visuel (intention) | Rendu |
|---|---|---|
| L18 | timeline, troisième point : 23:51 UTC, annonce de la suspension | `timeline upto=2 glitch` |
| L19 | timeline, quatrième point : 7 octobre, redémarrage ; log de reprise | `timeline upto=3` |
| L20 | écart mesuré entre 20:43 et 23:51 : trois heures environ | `bignum big="≈ 3 h" small="entre la 2e création de jetons et l'annonce de l'arrêt"` |

## Scène 5 : La cause racine : la preuve forgée

Partie : Twist / Révélation. Lignes : L21 à L25.

| N° | Visuel (intention) | Rendu |
|---|---|---|
| L21 | écran qui se fige sur "root cause: ?" ; les deux hypothèses barrées | `quote glitch text="Pas de clé volée.\|Pas de compte administrateur compromis.\|Alors, quoi ?"` |
| L22 | le module IAVL en gros plan ; une preuve valide à côté d'une preuve forgée, identiques à l'œil | `diagram stage=5 glitch` |
| L23 | Carte « preuves de Merkle forgées », attribuée en paraphrase au cofondateur de Cosmos ; badge RAPPORTÉ | `quote text="Preuves de Merkle forgées.\|Selon Ethan Buchman, cofondateur de Cosmos\|(paraphrase, pas une citation exacte)."` |
| L24 | mention "à confirmer" sur une branche de code partagée entre projets | `quote text="Code hérité d'une base largement partagée.\|Lien avec une faille connue ailleurs :\|À CONFIRMER auprès des sources primaires."` |
| L25 | une phrase en gros, hypothèse implicite soulignée | `quote glitch text="Hypothèse implicite (notre lecture) :\|« preuve valide = verrouillage réel ».\|Une fonction. Toute la confiance du pont."` |

## Scène 6 : Les conséquences

Partie : Conséquences. Lignes : L26 à L28.

| N° | Visuel (intention) | Rendu |
|---|---|---|
| L26 | bilan à deux colonnes : gelé / sorti ; mention "les chiffres finaux dépendent des sources" | `chart mode=range label="gelé vs sorti · chiffres finaux : selon les sources"` |
| L27 | validateurs en réseau, un signal d'arrêt se propage | `diagram stage=6` |
| L28 | balance à deux plateaux : "contenir l'attaque" / "promesse de décentralisation" | `quote text="Utile contre un attaquant.\|Dérangeant pour la promesse de décentralisation.\|Les deux lectures sont défendables."` |

## Scène 7 : La leçon d'ingénierie

Partie : Leçon. Lignes : L29 à L31.

| N° | Visuel (intention) | Rendu |
|---|---|---|
| L29 | checklist technique qui se coche : audits multiples, tests adverses, plafonds par transaction | `terminal lines="[x] audits indépendants du vérificateur de preuves\|[x] tests adverses sur des preuves malformées\|[x] plafond de création par transaction\|[x] alerte sur volumes inhabituels"` |
| L30 | courbe d'alerte : seuil franchi plus tôt, fenêtre d'action réduite | `chart mode=spike label="alerte sur volumes inhabituels · fenêtre réduite"` |
| L31 | écran de fin, sobre ; "fin du journal" | `terminal lines="END OF LOG\|logs affichés : reconstitutions simulées\|faits : sources publiques, voir la description"` |
