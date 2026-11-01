# INCIDENT LOG · 6 octobre 2022 : Binance, le pont qui a cru une fausse preuve

Titres YouTube proposés (date + sujet clair + accroche ; la date est toujours dans le titre) :
1. **[INCIDENT LOG · 6 oct. 2022] Binance : le pont qui a cru une fausse preuve, 2 millions de BNB créés de nulle part**
2. **[INCIDENT LOG · 6 oct. 2022] « Preuve valide » : comment BNB Chain a été piratée sans voler une seule clé**
3. **[INCIDENT LOG · 6 oct. 2022] 570 M$ en 2 transactions : autopsie de l'exploit du pont BSC Token Hub (Binance)**

Convention de la branche `incident_log` : un dossier `episodes/incident_<AAAA-MM-JJ>_<sujet>/` par vidéo, et un titre qui contient toujours « INCIDENT LOG », la date de l'incident et le sujet.

Incident log rétrospectif, quatre ans après (épisode produit en novembre 2026). Durée visée : 5 à 8 min (≈ 6 min 20 avec la voix de repère). Registre : enquêteur qui reconstitue les faits à partir de logs et de preuves, première personne du pluriel (« nous avons reconstitué »), ton neutre, analytique, immersif. Pas de morale simpliste.

Règles de rigueur (incident réel, public, sans mise en cause de personne) :
- **CONFIRMÉ** : faits repris par plusieurs analyses publiques indépendantes (exploit du pont BSC Token Hub, deux millions de BNB créés, suspension de la chaîne par les validateurs le 6 octobre, reprise le 7).
- **RAPPORTÉ** : détails d'une seule source ou d'un suivi on-chain (heure exacte de la seconde transaction, financement de 100 BNB la veille, paraphrase d'Ethan Buchman).
- **HYPOTHÈSE** : toute lecture personnelle (« hypothèse implicite »). L'auteur n'est pas identifié ici et n'est pas nommé.
- Les montants divergent selon les sources : la voix donne des fourchettes et le dit.
- **Les extraits de logs affichés sont des reconstitutions pédagogiques simulées, jamais des journaux réels** (dit dans L04 et L31).

## Description de la voix

> Voix masculine française de France, grave, neutre, un rythme soutenu mais pas précipité. Style « enquêteur qui reconstitue » : il lit les preuves, il ne dramatise pas. Vraies pauses avant les chutes (L03, L25). Prudent dès qu'une source est unique (« selon »). Son studio propre, sans effet. *(Enregistrée en local par l'auteur ; la voix de repère Piper « tom » sert uniquement à caler le montage.)*

## Script

### Scène 0 : Cold open : le pont dit oui

*Partie narrative : Hook*

| N° | Expression | Texte | Écran |
|---|---|---|---|
| L01 | lent, voix basse, glaçant | Jeudi six octobre deux mille vingt-deux. Un pont entre deux blockchains reçoit une demande de retrait. Il vérifie la preuve. Il dit oui. | écran noir, un curseur clignote ; la ligne de log "proof OK" apparaît en vert |
| L02 | sobre, détache les chiffres | Deux millions de BNB apparaissent de nulle part. Environ cinq cent soixante-dix millions de dollars, selon les estimations de l'époque. | compteur géant 2 000 000 BNB, la valeur en dollars apparaît en dessous |
| L03 | posé, appuie sur « cru » | Personne n'a volé de clé. Personne n'a cassé de mot de passe. Le système a simplement cru ce qu'on lui montrait. | deux cases barrées "clé privée volée" et "mot de passe cassé", puis "preuve acceptée" en rouge |

### Scène 1 : Le contexte : un pont entre deux chaînes

*Partie narrative : Contexte*

| N° | Expression | Texte | Écran |
|---|---|---|---|
| L04 | neutre, transparent sur la méthode | Nous avons reconstitué cet incident à partir des analyses publiques de chercheurs en sécurité et des données de la chaîne. Les extraits de logs affichés sont des reconstitutions pédagogiques, pas des journaux réels. | bandeau "RECONSTITUTION" sur fond de grille, sources listées |
| L05 | pédagogique, posé | Binance exploite deux blockchains. La Beacon Chain, bâtie sur le code de Cosmos, et la Smart Chain, compatible avec Ethereum. Pour déplacer des jetons de l'une à l'autre, il existe un pont : le Token Hub. | deux blocs, Beacon Chain et Smart Chain, reliés par un pont "Token Hub" |
| L06 | explicatif, rythme régulier | Le principe est simple. D'un côté, les jetons sont verrouillés. De l'autre, un contrat en crée autant. Verrouiller ici, créer là-bas. Le total ne change jamais. | cadenas sur la Beacon Chain, jetons créés sur la Smart Chain, total constant |
| L07 | pédagogique, ralentit sur « preuve » | Mais la Smart Chain ne voit pas la Beacon Chain. Pour croire qu'un verrouillage a eu lieu, elle exige une preuve cryptographique, vérifiée par un module dédié, écrit pour un format précis, appelé I A V L. | la Smart Chain "aveugle", une preuve Merkle arrive, module IAVL en surbrillance |
| L08 | structuré, énumère | Situation normale, donc : un utilisateur verrouille des jetons, un relais transmet la preuve, le module la vérifie, et seulement alors, les jetons sont créés. | séquence de quatre étapes qui s'allument : verrouiller, relayer, vérifier, créer |
| L09 | calme, presque ennuyé : tout est normal | Ce mécanisme tourne depuis des mois. Aucune alerte. Aucun incident connu. C'est la ligne de base. | courbe d'activité plate et verte, mention "aucune alerte" |

### Scène 2 : Avant l'attaque : le bruit de fond

*Partie narrative : Chronologie*

| N° | Expression | Texte | Écran |
|---|---|---|---|
| L10 | factuel, prudent (« selon ») | Mercredi cinq octobre. Selon les analyses de traçage publiées après coup, une adresse inconnue reçoit une petite somme, environ cent BNB, depuis un service d'échange. De quoi payer des frais de transaction. | timeline, premier point : 5 octobre, petite somme reçue par une adresse neuve |
| L11 | posé, léger sous-entendu | Rien d'anormal. Des milliers d'adresses font la même chose chaque jour. Le premier signe avant-coureur est invisible, parce qu'il ressemble au bruit de fond. | log banal, rien ne bouge, une ligne se surligne doucement |

### Scène 3 : La soirée du 6 octobre

*Partie narrative : Chronologie*

| N° | Expression | Texte | Écran |
|---|---|---|---|
| L12 | la tension monte, débit un peu plus serré | Jeudi six octobre, dans la soirée, heure U T C. Une première transaction arrive au pont. Elle contient une demande de retrait, accompagnée d'une preuve. | timeline, deuxième point : jeudi 6 octobre, soirée UTC ; le log s'accélère |
| L13 | froid, détache chaque étape | Le module de vérification examine la preuve. Elle est valide, au sens du code. Un million de BNB sont créés sur la Smart Chain. | log, "verify_proof ... OK" en vert, puis "mint 1 000 000 BNB" en rouge |
| L14 | sobre, précis sur l'heure | Puis une seconde transaction, identique dans sa forme. Vingt heures quarante-trois, U T C, selon un des suivis publics. Un million de BNB supplémentaires. | horodatage 20:43:xx UTC en gros, second mint |
| L15 | grave, chiffres détachés | En quelques minutes, deux millions de BNB, valant environ cinq cent soixante-dix millions de dollars, appartiennent à une seule adresse. | graphe de l'offre qui monte en escalier, deux marches |
| L16 | rythmé, énumération | Et la suite est une course. L'attaquant ne garde pas les fonds sur place. Il les échange, il les envoie vers d'autres chaînes, par d'autres ponts. | flux sortants depuis l'adresse vers d'autres chaînes, flèches multiples |
| L17 | prudent, nuancé : les sources divergent | Les chiffres divergent selon les sources. Les premières estimations parlaient d'environ cent à cent trente millions de dollars sortis de la chaîne. Le reste serait demeuré bloqué sur la Smart Chain. | deux jauges divergentes : "sorti de la chaîne" vs "resté bloqué" ; mention "les sources divergent" |

### Scène 4 : La suspension de la chaîne

*Partie narrative : Chronologie*

| N° | Expression | Texte | Écran |
|---|---|---|---|
| L18 | factuel, grave | Vingt-trois heures cinquante et une, U T C. Le patron de Binance, Changpeng Zhao, annonce que les validateurs ont été priés de suspendre la chaîne. Le problème est, dit-il, contenu. | timeline, troisième point : 23:51 UTC, annonce de la suspension |
| L19 | factuel, soulagement contenu | Le lendemain, vendredi sept octobre, vers six heures quarante U T C, la Smart Chain redémarre, avec une mise à jour qui bloque l'adresse de l'attaquant. | timeline, quatrième point : 7 octobre, redémarrage ; log de reprise |
| L20 | analytique, pause avant « long » | Environ trois heures se sont écoulées entre la seconde création de jetons et l'annonce de l'arrêt. Dans un système qui tourne en continu, c'est long. | écart mesuré entre 20:43 et 23:51 : trois heures environ |

### Scène 5 : La cause racine : la preuve forgée

*Partie narrative : Twist / Révélation*

| N° | Expression | Texte | Écran |
|---|---|---|---|
| L21 | question ouverte, lent | Alors, que s'est-il passé ? Pas de clé volée. Pas de compte administrateur compromis. | écran qui se fige sur "root cause: ?" ; les deux hypothèses barrées |
| L22 | grave, détache « fabriquées » | Les analyses publiques convergent sur un défaut dans la vérification des preuves I A V L. Le module acceptait des preuves que l'attaquant avait fabriquées de toutes pièces. | le module IAVL en gros plan ; une preuve valide à côté d'une preuve forgée, identiques à l'œil |
| L23 | analytique, attribue clairement | Autrement dit, l'attaquant pouvait écrire sa propre version de la réalité, et le pont la validait comme authentique. Selon le cofondateur de Cosmos, Ethan Buchman, il avait forgé des preuves de Merkle. | Carte « preuves de Merkle forgées », attribuée en paraphrase au cofondateur de Cosmos ; badge RAPPORTÉ |
| L24 | prudent, refuse de trancher | Ce format vient d'une base de code largement partagée. Certaines analyses évoquent une faille connue ailleurs, mais ce point reste à confirmer auprès des sources primaires. Nous ne le tranchons pas. | mention "à confirmer" sur une branche de code partagée entre projets |
| L25 | lent, voix basse, la chute de l'épisode | La cause racine n'est donc pas une erreur de saisie. C'est une hypothèse implicite : si le module dit que la preuve est valide, alors le verrouillage a eu lieu. Une seule fonction portait toute la confiance du pont. | une phrase en gros, hypothèse implicite soulignée |

### Scène 6 : Les conséquences

*Partie narrative : Conséquences*

| N° | Expression | Texte | Écran |
|---|---|---|---|
| L26 | sobre, honnête sur l'incertitude | Conséquences. Une partie des fonds a été gelée. Une autre est partie. Les pertes finales dépendent des sources, et nous ne les tranchons pas ici. | bilan à deux colonnes : gelé / sorti ; mention "les chiffres finaux dépendent des sources" |
| L27 | posé, ouvre un débat | Mais un autre fait est resté dans les mémoires. Une chaîne présentée comme décentralisée a pu être arrêtée en quelques heures, parce que ses validateurs ont répondu à une demande. | validateurs en réseau, un signal d'arrêt se propage |
| L28 | nuancé, équilibré | C'est utile contre un attaquant. C'est dérangeant pour la promesse de décentralisation. Les deux lectures sont défendables. | balance à deux plateaux : "contenir l'attaque" / "promesse de décentralisation" |

### Scène 7 : La leçon d'ingénierie

*Partie narrative : Leçon*

| N° | Expression | Texte | Écran |
|---|---|---|---|
| L29 | ferme, pédagogique | Côté ingénierie, la leçon est plus étroite et plus durable. Un pont ne vaut que par son vérificateur de preuves. Ce code mérite des audits multiples, des tests adverses, et des plafonds par transaction. | checklist technique qui se coche : audits multiples, tests adverses, plafonds par transaction |
| L30 | analytique, conclusif | Et il faut surveiller le bruit de fond. Une alerte sur les volumes de création inhabituels aurait réduit la fenêtre d'action de l'attaquant. | courbe d'alerte : seuil franchi plus tôt, fenêtre d'action réduite |
| L31 | neutre, sec, fin de journal | Fin du journal. Les logs affichés étaient des reconstitutions. Les faits, eux, sont publics. Les sources sont dans la description. | écran de fin, sobre ; "fin du journal" |

## Sources

- Immunefi : [Hack Analysis: Binance Bridge, October 2022](https://immunefi.com/blog/bug-fix-reviews/hack-analysis-binance-bridge-october-2022/)
- Halborn : [Explained: the BNB Chain hack (October 2022)](https://www.halborn.com/blog/post/explained-the-bnb-chain-hack-october-2022)
- SlowMist : [An analysis of the attack on BNB cross-chain bridge](https://slowmist.medium.com/slowmist-an-analysis-of-the-attack-on-bnb-cross-chain-bridge-f7411f33bb2)
- Merkle Science : [Hack Track: Analysis of the BNB Smart Chain exploit](https://www.merklescience.com/blog/hack-track-analysis-of-the-bnb-smart-chain-exploit)
- Numen Cyber Labs : [BSC cross-chain bridge hacking analysis](https://medium.com/numen-cyber-labs/bsc-chain-cross-chain-bridge-hacking-analysis-24338f9a80)
- The Block : [BNB Chain resumes service after hacker siphons at least $100 million](https://www.theblock.co/post/175437/biance-bnb-chain-is-back-up-after-bridge-exploit)
- ChainCatcher : [Cosmos co-founder: hackers forged Merkle proofs through RangeProof](https://chaincatcher.com/en/article/2080778)
- Beosin : [BNB Chain's $850 million hack, trace investigation](https://beosin.com/resources/bnb-chain%E2%80%99s-850-million-hack-beosin-trace-investigation)

## À vérifier avant enregistrement

Les faits viennent d'extraits de recherche, pas de la lecture des articles complets ni du post-mortem officiel de BNB Chain (accès réseau limité). Avant de publier, revérifier : l'heure de la seconde création (20:43 UTC, une seule source), l'heure de l'annonce de CZ (23:51 UTC) et de la reprise (≈ 06:40 UTC le 7 octobre), le financement de 100 BNB la veille (traçage secondaire), la fourchette « 100 à 130 M$ sortis » (The Block ; Beosin parle de 143 M$ de actifs pontés et de 850 M$ au total, définitions différentes), et le chiffre de 570 M$ (autres sources : 566 à 600 M$). Deux affirmations vues dans des synthèses secondaires ne sont **pas** utilisées : « faille déjà corrigée dans le SDK Cosmos en août 2022 » et « clé de vérification compromise » (contredit la version dominante). Le propos d'Ethan Buchman est une paraphrase rapportée, pas une citation exacte. Toute la partie « 4 ans après » (leçons, plafonds, alertes) est une lecture d'ingénierie, pas un fait publié.
