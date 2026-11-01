# INCIDENT LOG · 29 octobre 2026 : Binance, la nuit où les portefeuilles ont signé leur propre vol

Chaîne : artificiel-intelligence · Animateur : L'Inspecteur · Durée visée : 30 à 45 min (6 728 mots de narration : 45 min 38 s estimées à 150 mots/min avec pauses, ≈ 43 min à 160 mots/min) · Toutes les heures : **heure de La Mecque (UTC+3)**. Pour passer en UTC, retire 3 h.

Titres YouTube proposés :
1. **[INCIDENT LOG · 29 oct. 2026] Binance : 6 milliards 257 millions de dollars en 28 minutes, minute par minute**
2. **[INCIDENT LOG · 29 oct. 2026] « Signature valide » : autopsie du piratage des portefeuilles chauds de Binance (EIP-7702)**
3. **[INCIDENT LOG · 29 oct. 2026] Qui signait pour Binance cette nuit-là ? Le dossier, heure par heure**

Règles de rigueur (l'enquête est en cours, les chiffres bougent encore) :
- **CONFIRMÉ** : recoupé par plusieurs sources indépendantes (Wikipedia, Bitquery, Hackenproof, Crystal Intelligence, Threat Landscape, Blockaid via la presse crypto).
- **RAPPORTÉ** : une seule source, ou un relevé on-chain relayé que nous n'avons pas pu relire nous-mêmes. C'est marqué « selon » à l'oral.
- **ATTRIBUTION** : l'avis d'un cabinet d'analyse (TRM, Chainalysis, ZachXBT). Jamais une preuve, jamais une décision de justice.
- **Ce que ce script n'affirme pas** : nous n'avons pas refait le traçage on-chain nous-mêmes. La méthodologie dit « nous avons recoupé les relevés publiés », pas « nous avons tout retracé ». Les hash de transaction sont à renseigner depuis un explorateur (voir `sources.md`) : aucun hash n'est inventé.
- Les montants divergent (6,3 Md$ chez Binance, 6 milliards 257 millions dans le décompte huit chaînes que nous reprenons ; gelé : de 2,4 à 3 Md$ selon les sources). La voix le dit à chaque fois.

Format d'un bloc : `#### Bxx`, puis `[VISUEL]`, `[TEXTE À L'ÉCRAN]`, `[SFX]`, `[MUSIQUE]`, `[PAUSE]`, `[RÉF. ON-CHAIN]` (pour tout montant supérieur à 10 M$), et la narration (les lignes sans crochet). `tools/build_meta.py` compte les mots, recalcule `chapters.json` sur les durées réelles de la voix (`assets/voice/Bxx.wav`) et écrit `voice_lines.md` (texte à enregistrer). `assets/timeline.json` est la chronologie des événements, réutilisable pour les animations.

---

## A. COLD OPEN (0:00 – 1:30)

#### B01 · Cold open
[VISUEL: écran noir ; un curseur clignote ; un log monospace cyan apparaît ligne par ligne : "BINANCE 14 · IN · 200 000 000 USDT"]
[TEXTE À L'ÉCRAN: "00:42:59 UTC+3 — 200 000 000 USDT"]
[SFX: notification discrète, puis silence]
[MUSIQUE: drone sombre, très bas]
[RÉF. ON-CHAIN: transfert entrant de 200 M USDT vers Binance 14, 00:42:59 UTC+3 (21:42:59 UTC) — hash à renseigner, voir sources.md S-04]
Il est 00 h 42 min 59 s, heure de La Mecque, dans la nuit du 29 au 30 octobre. Un portefeuille de Binance, celui que les explorateurs appellent « Binance 14 », reçoit 200 millions d'USDT. Soixante-douze secondes plus tard, ils ont disparu.
[PAUSE: 1s]

#### B02 · Le détail qui cloche
[VISUEL: le compteur de 72 secondes qui défile à l'envers ; à côté, une transaction de 2 529 000 000 $ barrée "il y a 1 h 18"]
[TEXTE À L'ÉCRAN: "T-1 h 18 min — 2 529 000 000 $ déjà sortis"]
[SFX: glitch bref]
[MUSIQUE: tension qui monte lentement]
[RÉF. ON-CHAIN: balayage de Binance 14, 23:24 UTC+3, environ 2,529 Md$, 64 transferts — hash à renseigner, S-05]
Voici le détail qui cloche. Ce portefeuille a déjà été vidé. Une heure et dix-huit minutes plus tôt, plus de 2 milliards 529 millions de dollars en sont sortis, en une seule transaction. Et pourtant, il continue de fonctionner. Il reçoit. Il envoie. Comme si de rien n'était.

#### B03 · Il ne sait pas
[VISUEL: un portefeuille représenté par une silhouette de coffre ; une main inconnue pose une fiche devant lui ; le coffre s'ouvre]
[TEXTE À L'ÉCRAN: "Pour lui, celui qui demande, c'est son propriétaire."]
[SFX: clic de verrou]
[MUSIQUE: nappe suspendue]
Parce que ce portefeuille ne sait pas qu'il est en train d'être volé. Pour lui, la personne qui réclame l'argent, c'est son propriétaire légitime. Il obéit.
[PAUSE: 1s]

#### B04 · Sept réseaux, vingt-huit minutes
[VISUEL: carte des sept réseaux qui s'allument un à un (XRP Ledger, Optimism, Bitcoin, Ethereum, Tron, Arbitrum, Avalanche) avec un chronomètre 28:18]
[TEXTE À L'ÉCRAN: "28 min 18 s · 7 réseaux · 6 257 000 000 $ (huit réseaux, décompte final)"]
[SFX: whoosh à chaque réseau]
[MUSIQUE: pulsation régulière]
Et il n'est pas seul. En 28 minutes et 18 secondes, des portefeuilles répartis sur sept réseaux ont signé, de leur propre main, le transfert de leurs fonds vers le même attaquant. Un seul a demandé une ruse. Les autres ont simplement signé. Cette nuit-là, 6 milliards 257 millions de dollars ont quitté les portefeuilles associés à Binance, selon le décompte on-chain que nous reprenons, sur huit réseaux au total. Binance, elle, parle d'environ 6,3 milliards.

#### B05 · La question
[VISUEL: l'écran se vide ; reste une seule ligne : "qui signait ?"]
[TEXTE À L'ÉCRAN: "Qui signait pour Binance cette nuit-là ?"]
[SFX: aucun]
[MUSIQUE: coupe nette, silence deux secondes]
Alors voici la question qui ne nous lâche plus depuis trois jours. Dans un monde où l'argent ne bouge que sur signature, qui signait pour Binance, cette nuit-là ?
[PAUSE: 2s]

---

## B. MISE EN PLACE DE L'ENQUÊTE (1:30 – 3:00)

#### B06 · Le dossier est ouvert
[VISUEL: un dossier numérique qui s'ouvre, la date 29 octobre 2026 tamponnée en rouge, "INCIDENT LOG" en filigrane]
[TEXTE À L'ÉCRAN: "DOSSIER OUVERT · 29 octobre 2026 · ENQUÊTE EN COURS"]
[SFX: tampon, whoosh discret]
[MUSIQUE: ambiance sombre, entrée du thème]
Je suis L'Inspecteur. Le dossier qu'on a ouvert, l'encre n'est même pas encore sèche. Les faits ont trois jours. Binance a publié une première version de l'histoire, puis une seconde, et certains chiffres changent encore d'une source à l'autre. Alors on va faire ça proprement : on revient sur la nuit du 29 octobre, minute par minute, avec les heures au fil de l'eau.

#### B07 · Heure de La Mecque
[VISUEL: horloge à deux cadrans, UTC+3 et UTC, avec une flèche "−3 h"]
[TEXTE À L'ÉCRAN: "Toutes les heures : UTC+3 (La Mecque)"]
[SFX: tic d'horloge]
[MUSIQUE: nappe stable]
Une précision, et elle compte. Toutes les heures que tu vas entendre sont à l'heure de La Mecque, UTC plus trois. Si tu veux les comparer avec un explorateur ou avec un rapport d'analyse, retire trois heures. Quand je te dis 23 h 20 min 59 s, l'horloge de la blockchain, elle, affiche 20 h 20 min 59 s.

#### B08 · Méthodologie
[VISUEL: trois colonnes : "relevés on-chain publiés" / "explorateurs" / "communiqués" ; les chiffres divergents sont encadrés en orange]
[TEXTE À L'ÉCRAN: "Quand deux sources divergent : on donne les deux."]
[SFX: clics de tri]
[MUSIQUE: pulsation légère]
La méthode, maintenant. Les chiffres qu'on va te donner, on ne les a pas pris dans les gros titres. Nous sommes partis des relevés on-chain publiés par les équipes d'analyse, avec leurs adresses, leurs horodatages, leurs blocs, et nous avons recoupé. Quand deux sources divergent, on te donne les deux chiffres. Et ce qu'on n'a pas pu relire nous-mêmes, on te le dit avec le mot « selon ».

#### B09 · Au programme
[VISUEL: sommaire animé en lignes de log : "01 le vol / 02 la faille / 03 la riposte / 04 qui ?"]
[TEXTE À L'ÉCRAN: "Programme : la préparation · la frappe · la faille · la riposte · l'attribution"]
[SFX: notification]
[MUSIQUE: montée douce]
Au programme : la préparation de l'attaquant, pendant trente-six heures. La frappe, en trois phases. Le mécanisme technique qui a permis à une seule de ces portefeuilles de signer son propre vol. La course entre l'attaquant et ceux qui ont des boutons d'urgence. Et enfin, ceux qui disent savoir qui se cache derrière. On posera aussi, à la fin, cinq questions auxquelles personne n'a répondu.

#### B10 · CTA
[VISUEL: bouton "S'abonner" discret en bas à droite ; cloche qui s'agite une fois]
[TEXTE À L'ÉCRAN: "Abonne-toi · active la cloche"]
[SFX: ping]
[MUSIQUE: stable]
Si tu veux les détails avant qu'ils refroidissent, abonne-toi et active la cloche. Ce dossier va bouger, et on reviendra dessus. Et même si tu débutes en crypto, reste : à la fin de cette vidéo, tu auras compris ce qui s'est passé, parce que je vais tout poser dans l'ordre.

---

## C. PÉDAGOGIE PRÉALABLE (3:00 – 8:00)

*Avant de comprendre le vol, comprenons ce qui a été volé.*

#### B11 · Le grand livre
[VISUEL: un grand livre de comptes ouvert, dont les lignes s'écrivent toutes seules ; des mains du monde entier le lisent]
[TEXTE À L'ÉCRAN: "Blockchain = un grand livre de comptes public"]
[SFX: plume sur papier, très doux]
[MUSIQUE: ambiante, neutre]
Imagine la blockchain comme un grand livre de comptes que n'importe qui, dans le monde, peut lire. Chaque opération y est écrite à la suite des autres. Rien ne s'efface, aucune ligne. Et il n'y a pas un seul livre, il y en a plusieurs : Bitcoin, Ethereum, Tron, XRP Ledger, et d'autres. On appelle chacun un réseau, avec sa monnaie et ses règles.

#### B12 · Jetons et stablecoins
[VISUEL: un réseau (Ethereum) sur lequel flottent de petits jetons ; l'USDT est entouré d'un cercle "1 $"]
[TEXTE À L'ÉCRAN: "USDT : un dollar numérique, émis par Tether"]
[SFX: tintement léger]
[MUSIQUE: neutre]
Sur certains réseaux, d'autres monnaies existent, construites au-dessus : on les appelle des jetons. Les plus connus sont les stablecoins, des dollars numériques. L'USDT, émis par une société qui s'appelle Tether. L'USDC, émis par Circle. Un USDT vaut un dollar, parce que l'émetteur promet de le maintenir.

#### B13 · Le portefeuille n'est pas un portefeuille
[VISUEL: un coffre de verre transparent avec une adresse en monospace "0x…", et une clé qui flotte à côté]
[TEXTE À L'ÉCRAN: "Adresse = le coffre · Clé privée = le droit de signer"]
[SFX: clé qui tourne dans une serrure]
[MUSIQUE: nappe stable]
Un portefeuille, dans ce monde, n'est pas une pochette de billets. C'est une adresse sur le grand livre, plus une clé privée. Celui qui a la clé peut signer. Celui qui peut signer peut déplacer l'argent. Il n'y a pas d'employé qui te rappelle pour vérifier, pas d'agence bancaire qui appelle ton téléphone. La signature, c'est l'identité. Retiens cette phrase : c'est le fil rouge de tout ce dossier.

#### B14 · Chaud et froid
[VISUEL: deux coffres : l'un en glace, hors ligne ("froid") ; l'autre branché aux serveurs, en orange ("chaud")]
[TEXTE À L'ÉCRAN: "Froid : hors ligne · Chaud : connecté en permanence"]
[SFX: souffle de glace / bourdonnement électrique]
[MUSIQUE: tension légère]
Les grandes plateformes séparent leurs fonds en deux familles. Les portefeuilles froids : leurs clés restent hors ligne, ils contiennent l'essentiel de l'argent, ils sont lents et sûrs. Et les portefeuilles chauds : connectés en permanence aux systèmes de la plateforme, pour que tes retraits partent en quelques minutes. Les chauds sont rapides. C'est aussi pour ça qu'ils sont les plus exposés.

#### B15 · Binance 14
[VISUEL: capture simulée d'un explorateur : "Binance 14", un solde, un compteur de transactions]
[TEXTE À L'ÉCRAN: "Binance 14 · portefeuille chaud · Ethereum"]
[SFX: clic]
[MUSIQUE: stable]
Le soir du 29 octobre, l'un de ces portefeuilles chauds est un gros portefeuille de Binance sur Ethereum. Les explorateurs l'étiquettent « Binance 14 ». Un portefeuille qui ne dort jamais.

#### B16 · Le nonce
[VISUEL: un carnet de chèques ; le dernier chèque numéroté 18 914 808 ; un tampon "interdit de réutiliser un numéro"]
[TEXTE À L'ÉCRAN: "Nonce 18 914 808"]
[SFX: déchirement de chèque]
[MUSIQUE: neutre]
Jusqu'à cette nuit, Binance 14 avait envoyé 18 millions 914 mille 808 transactions. Autrement dit, près de dix-neuf millions de fois, elle a dit « d'accord ». Ce nombre a un nom : le nonce. Pense aux numéros de chèques dans un carnet : chaque transaction qui sort du portefeuille prend le numéro suivant, et un numéro ne peut jamais servir deux fois. Retiens bien ce mot. On va le retrouver, et c'est là que ça devient intéressant.

#### B17 · Qui signe dix-neuf millions de fois ?
[VISUEL: un système de retraits : demande client → vérification → signature → diffusion ; une boucle automatique]
[TEXTE À L'ÉCRAN: "Un système de retraits : demande → vérification → signature → envoi"]
[SFX: boucle mécanique douce]
[MUSIQUE: pulsation]
Qui a signé dix-neuf millions de fois ? Pas un humain. Un système de retraits : il reçoit la demande d'un client, vérifie, signe, diffuse. Quand le solde du portefeuille chaud baisse, d'autres portefeuilles viennent le réalimenter, sans que personne n'appuie sur un bouton. Une machine qui sert des millions de clients, et qui ne pose qu'une question : la signature est-elle valide, oui ou non. Garde cette question en tête.

#### B18 · Les contrats intelligents
[VISUEL: un petit programme qui vit dans le réseau, s'exécute seul ; un diagramme "adresse → code"]
[TEXTE À L'ÉCRAN: "Contrat intelligent : du code qui s'exécute sur le réseau"]
[SFX: clavier discret]
[MUSIQUE: neutre]
Un dernier mot de vocabulaire. Sur Ethereum, il existe deux types de comptes : le compte ordinaire, une adresse commandée par une clé, qui sait faire une seule chose, envoyer ; et le contrat intelligent, du code qui vit sur le réseau et fait tout ce qu'on y a écrit. Deux espèces différentes. On va voir qu'une mise à jour récente a brouillé la frontière.

#### B19 · Transition
[VISUEL: retour au tableau de chronologie ; la ligne "28 octobre, 10 h 39" clignote]
[TEXTE À L'ÉCRAN: "Mercredi 28 octobre · 10:39"]
[SFX: whoosh]
[MUSIQUE: tension légère qui revient]
Maintenant tu as les mots. Clé, signature, portefeuille chaud, nonce, boutons d'urgence. Alors remontons trente-six heures avant l'attaque, parce que ce qui s'est passé à 23 h 20 n'est pas un coup de chance : c'est un coup préparé.

---

## D. CONTEXTE & PRÉPARATION DE L'ATTAQUE (8:00 – 12:00)

#### B20 · Mercredi 28 octobre, 10 h 39
[VISUEL: nouvelle adresse "0x…" en cyan ; une petite fleur de fonds arrive depuis un nœud "Tornado Cash · pool 0,1 ETH"]
[TEXTE À L'ÉCRAN: "Mer. 28 oct. · 10:39 — < 0,1 ETH depuis Tornado Cash"]
[SFX: notification]
[MUSIQUE: ambiance sombre]
Mercredi 28 octobre, 10 h 39 du matin, sur Ethereum. Une adresse neuve reçoit moins de 0,1 Ether. D'où vient cet argent ? D'un mélangeur, Tornado Cash : tu y déposes tes fonds avec ceux des autres, tu les retires de l'autre côté, et personne ne peut relier l'entrée à la sortie. Ici, le plus petit bassin du mélangeur, celui de 0,1 Ether.

#### B21 · Pourquoi si peu ?
[VISUEL: un compteur d'essence "gas" ; une petite pompe ; un cadenas sur le nom du payeur]
[TEXTE À L'ÉCRAN: "Gas : les frais de transaction, payés en ETH"]
[SFX: pompe]
[MUSIQUE: stable]
Pourquoi si peu ? Pour les frais. Chaque transaction sur Ethereum coûte du « gas », payé en Ether. Même un voleur doit payer la route, mais il ne veut pas que quelqu'un sache qui a payé. Trois retraits du même bassin, le dernier le jeudi 29 octobre, à 11 h 23 du matin.

#### B22 · Jeudi, 5 h 28 : le prototype
[VISUEL: un éditeur de code simulé ; un nouveau contrat apparaît avec un identifiant tronqué ; étiquette "prototype"]
[TEXTE À L'ÉCRAN: "Jeu. 29 oct. · 05:28 — premier contrat déployé"]
[SFX: frappe de touches]
[MUSIQUE: pulsation grave]
Le jeudi 29 octobre, à 5 h 28 du matin, la même adresse publie son premier programme sur le réseau : un contrat, un prototype. Du code qui vivra sur la blockchain, visible de tous, et qui s'exécutera sans qu'on le surveille.

#### B23 · Les trois portefeuilles d'essai
[VISUEL: trois portefeuilles factices alignés, étiquetés "essai 1, 2, 3" ; chacun reçoit le même enchaînement ; chrono 16:51 → 19:47]
[TEXTE À L'ÉCRAN: "16:51 → 19:47 — trois portefeuilles factices, répétitions"]
[SFX: clics rythmés]
[MUSIQUE: tension]
Entre 16 h 51 et 19 h 47, quelque chose d'étrange. Trois portefeuilles d'essai, sous contrôle de l'attaquant. Pour chacun, la même série de gestes : le relier à son contrat, puis lancer deux fonctions, l'une qui s'appelle « sweep », balayer, et l'autre qui retire l'Ether. Une répétition générale, avec de fausses victimes.

#### B24 · La liste de nonces
[VISUEL: trois listes d'autorisations : "[n]" ; "[n, n+1]" ; "[n, n+1, n+2]" ; la dernière entourée]
[TEXTE À L'ÉCRAN: "Chaque essai : une liste de nonces différents, dans la même demande"]
[SFX: glitch discret]
[MUSIQUE: montée]
À chaque essai, il n'envoie pas une seule autorisation au portefeuille. Il en envoie une liste : deux, trois nonces différents dans la même demande. Il s'entraîne à tirer plusieurs numéros à la fois. Ce détail est minuscule. Il va tout expliquer plus tard.

#### B25 · 18 h 59 : la version finale
[VISUEL: le code final du contrat avec ses quatre fonctions ; un cadenas sur chacune ; une adresse unique surlignée en rouge]
[TEXTE À L'ÉCRAN: "18:59 — contrat final · 4 fonctions · 1 seul propriétaire"]
[SFX: tampon]
[MUSIQUE: pulsation grave]
À 18 h 59, il publie la version finale. Quatre fonctions seulement : balayer, retirer l'Ether, retirer les jetons, exécuter une commande. Les quatre verrouillées sur une seule adresse, écrite en dur dans le code : celle de l'attaquant. Un programme qui ne reconnaît qu'un seul maître.

#### B26 · Les détails qui ne trompent pas
[VISUEL: trois fiches "preuve" qui se posent sur une table : mélangeur / essais / adresse en dur]
[TEXTE À L'ÉCRAN: "Trois détails qui ne trompent pas"]
[SFX: tampon x3]
[MUSIQUE: stable]
Notons trois détails qui ne trompent pas. Un : le financement par un mélangeur, donc quelqu'un qui anticipe qu'on remontera sa trace. Deux : des répétitions sur des portefeuilles factices, donc quelqu'un qui teste avant de frapper. Trois : un propriétaire gravé en dur, donc quelqu'un qui sait exactement où l'argent doit atterrir.

#### B27 · Trente-six heures
[VISUEL: ligne de temps : 28 oct 10:39 → 29 oct 23:04:52, chronomètre 36:25:52]
[TEXTE À L'ÉCRAN: "36 h 25 min 52 s de préparation"]
[SFX: tic prolongé]
[MUSIQUE: tension qui monte]
Ce qu'on peut donc dire, c'est que l'attaquant a passé 36 heures, 25 minutes et 52 secondes à se préparer avant le premier geste visible contre Binance. Le premier geste, ce n'est pas sur Ethereum. C'est sur un tout autre réseau.

---

## E. CHRONOLOGIE MINUTE PAR MINUTE (12:00 – 22:00)

#### B28 · Phase 1 : le test (23 h 04 min 52 s)
[VISUEL: écran partagé : à gauche "XRP Ledger" ; log "payment 42 750 000 RLUSD → compte inconnu" ; réponse en rouge "tecNO_DST_INSUF_XRP"]
[TEXTE À L'ÉCRAN: "PHASE 1 · LE TEST · 23:04:52 — 42 750 000 $ (RLUSD)"]
[SFX: alerte brève]
[MUSIQUE: tension]
[RÉF. ON-CHAIN: paiement XRP Ledger de 42 750 000 RLUSD, 23:04:52 UTC+3 (20:04:52 UTC), échec — hash à renseigner, S-06]
Phase 1 : le test. 23 h 04 min 52 s, sur le XRP Ledger. Un compte associé à Binance tente d'envoyer 42 millions 750 mille dollars de RLUSD vers un compte qui n'existe pas encore. La transaction échoue. Sur ce réseau, un compte n'existe qu'à partir du moment où il a reçu un petit montant de la monnaie de base, le XRP. L'attaquant a oublié la règle. Il a pressé.

#### B29 · Huit secondes plus tard
[VISUEL: un paiement de 185 millions de XRP qui active le compte ; le compte passe de "fantôme" à "actif"]
[TEXTE À L'ÉCRAN: "23:05:00 — 185 000 000 XRP · le compte existe"]
[SFX: déclic, puis whoosh]
[MUSIQUE: pulsation]
[RÉF. ON-CHAIN: paiement XRP Ledger de 185 000 000 XRP (activation + envoi), 23:05:00 UTC+3 — hash à renseigner, S-06]
Huit secondes plus tard, 23 h 05 min 00 s, le correctif : un paiement de 185 millions de XRP qui donne vie au compte. Le premier geste de l'histoire de cette nuit a raté à cause d'une règle de base, et il a été réparé en huit secondes.

#### B30 · Les cinq comptes XRP
[VISUEL: cinq comptes XRP qui se vident un à un vers une même adresse ; un compteur qui monte à 297 M$]
[TEXTE À L'ÉCRAN: "23:05 → 23:09 — 5 comptes · ≈ 297 000 000 $"]
[SFX: whoosh x5]
[MUSIQUE: tension]
[RÉF. ON-CHAIN: cinq comptes XRPL → une adresse, 297 M$ en XRP, 4 min 10 s — hashes à renseigner, S-06]
En quatre minutes et dix secondes, cinq comptes envoient à la même adresse environ 297 millions de dollars de XRP. Tu vois le rythme : on teste, on corrige, on enchaîne.

#### B31 · Phase 2 : la frappe (23 h 18)
[VISUEL: carte des réseaux ; Optimism s'allume ; une flèche vers une adresse "0x5227…" qu'on appellera Adresse 1]
[TEXTE À L'ÉCRAN: "PHASE 2 · LA FRAPPE · 23:18 — Optimism → Adresse 1"]
[SFX: whoosh]
[MUSIQUE: pulsation rapide]
Phase 2 : la frappe. À 23 h 18, sur Optimism, environ 5 millions de dollars partent vers une adresse qui commence par 0x5227. Appelons-la l'Adresse 1, pour ne pas répéter les chiffres. C'est elle que tu vas voir revenir toute la nuit.

#### B32 · Bitcoin : 11 transactions, un seul bloc
[VISUEL: un bloc Bitcoin ; onze transactions s'y alignent ; compteur de 18 000 BTC qui monte à 1 467 000 000 $]
[TEXTE À L'ÉCRAN: "23:20 — 11 transactions · 1 seul bloc · 1 467 000 000 $"]
[SFX: impact grave]
[MUSIQUE: tension forte]
[RÉF. ON-CHAIN: 11 transactions Bitcoin dans un même bloc, 23:20 UTC+3 environ, > 18 000 BTC, ≈ 1,467 Md$ — hashes à renseigner, S-07]
À 23 h 20, sur Bitcoin : onze transactions, toutes écrites dans la même page du livre. Plus de 18 000 bitcoins. 1 milliard 467 millions de dollars en un seul bloc.

#### B33 · Ethereum : la recharge
[VISUEL: une adresse "recharge" envoie 7 000 ETH à Binance 14 ; la jauge de Binance 14 remonte]
[TEXTE À L'ÉCRAN: "23:19 — +7 000 ETH · ≈ 16 000 000 $ · recharge automatique"]
[SFX: notification]
[MUSIQUE: stable]
[RÉF. ON-CHAIN: transfert d'environ 7 000 ETH (≈ 16 M$) vers Binance 14, 23:19 UTC+3 — hash à renseigner, S-08]
Pendant ce temps, sur Ethereum, à 23 h 19, Binance 14 reçoit environ 7 000 Ether, soit 16 millions de dollars. L'adresse qui envoie a plus de 256 000 transactions derrière elle : c'est un portefeuille de recharge, d'une routine ordinaire. La machine a fait son travail : le portefeuille chaud manquait de carburant, on l'a rempli.

#### B34 · Quatre-vingt-quatre secondes plus tard
[VISUEL: une transaction arrive à Binance 14, mais l'expéditeur est inconnu ; le chrono montre 84 s]
[TEXTE À L'ÉCRAN: "+84 s — 23:20:59 — une demande qui ne vient pas de Binance"]
[SFX: glitch]
[MUSIQUE: coupe, silence, impact]
Quatre-vingt-quatre secondes plus tard, une deuxième demande arrive au même portefeuille. Cette fois, elle ne vient pas de Binance. Le rapport de Blockaid l'horodate à 20 h 20 min 59 s UTC, donc 23 h 20 min 59 s chez nous.

#### B35 · La transaction à zéro
[VISUEL: une transaction Ethereum : valeur "0 ETH" ; à l'intérieur, une liste de 50 lignes "authorization n°…" qui défile]
[TEXTE À L'ÉCRAN: "23:20:59 — valeur : 0 $ — 50 autorisations"]
[SFX: glitch bref]
[MUSIQUE: tension]
[RÉF. ON-CHAIN: transaction de type 4 (EIP-7702), 50 autorisations visant Binance 14, 23:20:59 UTC+3 — hash à renseigner, S-09]
Cette transaction transporte une valeur de zéro. Aucun ordre visible. À l'intérieur : cinquante petites feuilles d'autorisation, toutes signées avec la clé de Binance 14, qui disent toutes la même chose : « emprunte le code de ce contrat ». Le contrat, c'est celui de l'attaquant. La seule différence entre les cinquante feuilles, c'est un numéro : le nonce. Cinquante numéros qui se suivent.

#### B36 · Pourquoi cinquante ?
[VISUEL: un carnet de chèques ; une feuille du bon numéro surlignée ; les 49 autres s'effacent]
[TEXTE À L'ÉCRAN: "50 feuilles · 1 seule bonne : nonce …809"]
[SFX: déclic]
[MUSIQUE: stable, curieuse]
Pourquoi cinquante ? Parce qu'une feuille ne fonctionne que si son numéro correspond exactement au numéro du portefeuille à l'instant où elle entre dans le réseau. Binance 14 continuait d'envoyer des retraits, donc son nonce bougeait en permanence. L'attaquant ne savait pas quel numéro serait le bon : il en a tendu cinquante. Un seul a pris : celui qui suivait la dernière transaction du portefeuille.

#### B37 · Le code change
[VISUEL: l'adresse Binance 14 dans l'explorateur ; le champ "code" passe de vide à "0xef0100… → contrat attaquant"]
[TEXTE À L'ÉCRAN: "Binance 14 n'est plus un simple portefeuille. Elle a du code."]
[SFX: serrure qui change de côté]
[MUSIQUE: coupe sèche]
À cet instant, le code du portefeuille change. Il pointe désormais vers le contrat de l'attaquant. Binance 14 n'est plus un simple portefeuille : elle porte du code. Un code qui ne connaît qu'un seul maître. Il restait à l'attaquant 3 minutes et 24 secondes avant de vider.

#### B38 · Tron
[VISUEL: Tron ; un compte vieux de 72 secondes reçoit sa première monnaie ; puis un montant de 612 M$ USDT]
[TEXTE À L'ÉCRAN: "23:21 — Tron · compte vieux de 72 s · 612 000 000 $ USDT"]
[SFX: whoosh]
[MUSIQUE: pulsation]
[RÉF. ON-CHAIN: transferts USDT sur Tron, ≈ 612 M$, 23:21–23:23 UTC+3 — hashes à renseigner, S-10]
23 h 21, sur Tron. Un compte qui existe depuis 72 secondes reçoit sa première pièce de monnaie du réseau. Une minute et demie plus tard, 612 millions de dollars d'USDT arrivent dessus. Un compte qui n'existait pas trois minutes plus tôt.

#### B39 · 23 h 24 : le balayage
[VISUEL: l'ordre "sweep" part vers Binance 14 ; une longue liste de 64 transferts défile ; compteur 2 529 000 000 $]
[TEXTE À L'ÉCRAN: "23:24 — SWEEP — 64 transferts — 2 529 000 000 $"]
[SFX: impact grave, whoosh long]
[MUSIQUE: pic de tension]
[RÉF. ON-CHAIN: appel « sweep » sur Binance 14, 23:24 UTC+3, 64 transferts dont ≈ 1,615 Md$ d'USDT, total ≈ 2,529 Md$ — hash à renseigner, S-05]
23 h 24. L'attaquant parle à Binance 14. Elle répond avec le nouveau code. Un seul ordre : « sweep », balaie. Avec la liste de ce qu'il faut envoyer, et à qui. En une seule transaction, 64 transferts : plus de 1 milliard 615 millions de dollars en USDT, de l'or numérique, d'autres jetons. Total : 2 milliards 529 millions de dollars. Le contrat laisse dans le portefeuille un seul Ether. Certaines sources parlent de 2,8 milliards pour ce seul portefeuille : les définitions de ce qui est compté diffèrent, et on garde le chiffre que nous avons recoupé.

#### B40 · Pourquoi aucune alarme ?
[VISUEL: un système d'alarme qui surveille la case "valeur envoyée" ; elle affiche 0 ; l'alarme reste au vert]
[TEXTE À L'ÉCRAN: "Valeur visible : 0 $ · valeur réelle : 2 529 000 000 $"]
[SFX: silence]
[MUSIQUE: nappe suspendue]
Pourquoi aucune alarme à ce stade ? Parce que si tu ouvres cette transaction, sa valeur apparente est zéro. L'Ether n'est pas sorti avec la transaction : il est sorti de l'intérieur, par du code qui s'exécutait. Comme un chèque de zéro euro, avec des ordres de virement cachés au dos. Un système qui surveille seulement la valeur affichée ne voit rien.

#### B41 · Binance 16
[VISUEL: une deuxième adresse, "Binance 16", envoie 9 transactions vers l'Adresse 1 ; compteur 174 M$]
[TEXTE À L'ÉCRAN: "23:24:47 — Binance 16 · 9 transactions · 174 000 000 $"]
[SFX: notification]
[MUSIQUE: stable]
[RÉF. ON-CHAIN: 9 transactions de Binance 16 vers l'Adresse 1, 23:24:47 UTC+3 — ≈ 28 000 ETH, 55 M USDT, or numérique ; ≈ 174 M$ — hashes à renseigner, S-11]
Vingt-quatre secondes plus tard, à 23 h 24 min 47 s, une deuxième adresse de Binance sur Ethereum, « Binance 16 », envoie à la même Adresse 1 neuf transactions de suite : 28 000 Ether, 55 millions d'USDT, de l'or numérique, d'autres jetons. 174 millions de dollars. Un second portefeuille vidé, et celui-là, on y reviendra, parce qu'il ne porte aucune trace de la ruse.

#### B42 · Arbitrum, Avalanche
[VISUEL: Arbitrum puis Avalanche s'allument ; quatre portefeuilles chacun]
[TEXTE À L'ÉCRAN: "23:30 Arbitrum ≈ 32 000 000 $ · 23:33:00 Avalanche"]
[SFX: whoosh x2]
[MUSIQUE: pulsation]
[RÉF. ON-CHAIN: Arbitrum 23:30 UTC+3 ≈ 32 M$ (4 portefeuilles) ; Avalanche 23:33:00 (4 portefeuilles, AVAX et USDT) — hashes à renseigner, S-12]
À 23 h 30, Arbitrum : quatre portefeuilles envoient environ 32 millions de dollars. À 23 h 33 min 00 s, Avalanche : quatre autres portefeuilles envoient de l'AVAX et de l'USDT. Où vont-ils tous ? À la même adresse. L'Adresse 1, sur Optimism, sur Ethereum, sur Arbitrum, sur Avalanche. Une seule adresse, une seule clé, dans la main de l'attaquant.

#### B43 · Le décompte
[VISUEL: chronomètre qui s'arrête sur 28:18 ; carte des sept réseaux ; somme > 5 000 000 000 $]
[TEXTE À L'ÉCRAN: "23:05:00 → 23:33:18 = 28 min 18 s · 7 réseaux · plus de 5 milliards"]
[SFX: tic final]
[MUSIQUE: coupe]
Faisons le décompte. Premier geste réussi, 23 h 05 min 00 s. Dernier de cette vague, 23 h 33 min 18 s. 28 minutes et 18 secondes. Sept réseaux. Plus de 5 milliards de dollars sortis de portefeuilles associés à Binance. Et à ce moment, le reste du monde ne savait encore rien.

#### B44 · Le silence de Binance, et un écho
[VISUEL: un fil de messages vide, à côté d'un autre dossier de la série : "Affaire Bitget"]
[TEXTE À L'ÉCRAN: "Comme dans l'affaire Bitget il y a 5 semaines…"]
[SFX: tampon]
[MUSIQUE: stable]
Binance ne dit pas un mot, et son premier communiqué ne viendra qu'environ une heure plus tard. Si tu suis cette série d'enquêtes, tu as peut-être l'impression d'avoir déjà vu cette scène. Il y a cinq semaines, dans l'affaire Bitget, 388 millions de dollars étaient partis avec une particularité : aucune clé n'avait été volée. Ce sont les portefeuilles eux-mêmes qui avaient signé. Cette nuit, c'est la même signature, avec un chiffre seize fois plus gros.

#### B45 · Phase 3 : la fuite (23 h 38)
[VISUEL: l'Adresse 1 se vide d'un coup vers une adresse neuve ; 195 000 ETH]
[TEXTE À L'ÉCRAN: "PHASE 3 · LA FUITE · 23:38 — 195 000 ETH déplacés"]
[SFX: whoosh]
[MUSIQUE: pulsation]
[RÉF. ON-CHAIN: 195 000 ETH de l'Adresse 1 vers une adresse neuve, 23:38 UTC+3 — hash à renseigner, S-13]
Phase 3 : la fuite. 23 h 38. Le premier mouvement de l'attaquant avec l'argent qu'il vient de recevoir : 195 000 Ether de l'Adresse 1 vers une adresse neuve. L'Adresse 1, elle, reste pleine de dollars numériques, des centaines de millions d'USDT, d'USDC et d'or. Des fonds qui ont un propriétaire capable de les geler. Et ce qui se passe ensuite est la première fois, cette nuit-là, qu'un humain semble intervenir.

#### B46 · 23 h 41 : un deuxième compte obéit
[VISUEL: Binance 14 donne un ordre à un compte associé ; une flèche vers l'Adresse 1 ; 780 M$ en USDC]
[TEXTE À L'ÉCRAN: "23:41 — Binance 14 ordonne à un compte associé · 780 000 000 $ USDC"]
[SFX: déclic]
[MUSIQUE: tension]
[RÉF. ON-CHAIN: 780 M USDC d'un compte associé à Binance 14 vers l'Adresse 1, 23:41 UTC+3 — hash à renseigner, S-14]
23 h 41. Binance 14 n'a presque plus d'USDC, mais elle a quelque chose de plus utile : un compte associé, qui n'écoute qu'elle. Le code planté par l'attaquant n'avait pas servi jusqu'ici à cet usage. Il commande à Binance 14 de donner un ordre à ce compte. Et le compte obéit : 780 millions d'USDC, vers l'Adresse 1.

#### B47 · Premières questions
[VISUEL: fil de messages d'un réseau social ; des analystes commentent une liste de montants]
[TEXTE À L'ÉCRAN: "≈ 00:00 — « Migration interne ? »"]
[SFX: notifications en cascade]
[MUSIQUE: stable]
Vers minuit, sur les réseaux sociaux, des analystes qui suivent les gros portefeuilles voient des chiffres qu'on ne voit pas tous les jours : des milliards qui sortent de portefeuilles connus pour appartenir à Binance, vers une adresse vieille de quelques minutes. Première explication, plutôt rassurante : Binance déplace ses fonds d'un portefeuille à un autre. Une migration interne, ça arrive.

#### B48 · La théorie qui tient cinq minutes
[VISUEL: la même adresse ; une question : "qui a payé le gas ?" ; la réponse : "Tornado Cash"]
[TEXTE À L'ÉCRAN: "Gas payé depuis un mélangeur. Binance ne fait pas ça."]
[SFX: glitch]
[MUSIQUE: tension]
Cette théorie ne tient que quelques minutes. Quelqu'un remonte d'un cran et pose une question simple : d'où vient le gas qui a payé cette transaction ? De Tornado Cash. Et une plateforme comme Binance ne finance pas ses frais depuis un mélangeur. Peu après, Etherscan, l'explorateur le plus consulté d'Ethereum, étiquette l'Adresse 1 d'un nom qui ne laisse plus de doute : « Binance Hot Wallet Exploiter #2 », avec les marques « Exploit » et « Heist ».

#### B49 · 00 h 15 : la voix du fondateur
[VISUEL: capture simulée d'une publication de Changpeng Zhao ; texte paraphrasé]
[TEXTE À L'ÉCRAN: "00:15 — CZ : « on dirait un piratage »" (paraphrase)]
[SFX: notification]
[MUSIQUE: stable]
À 00 h 15, première voix de l'intérieur : Changpeng Zhao, le fondateur de Binance, que tout le monde appelle CZ. D'après les captures relayées, il écrit que ça ressemble à un piratage visant Binance. Il ajoute qu'il n'est plus le dirigeant, mais qu'en tant qu'actionnaire, il s'attend à ce que les fonds des utilisateurs soient couverts. On est là sur sa paraphrase, pas sur une citation exacte, et on le dit.

#### B50 · 00 h 24 : le communiqué
[VISUEL: le texte du communiqué de Binance simulé ; deux mots surlignés : "potentiel" et "enquête"]
[TEXTE À L'ÉCRAN: "00:24 — « problème de sécurité potentiel »"]
[SFX: tampon]
[MUSIQUE: stable]
Neuf minutes plus tard, à 00 h 24, premier communiqué officiel de Binance. Le ton est différent : l'équipe dit être au courant de signalements d'un problème de sécurité potentiel, et enquêter. Le fondateur parle de piratage. L'entreprise parle de potentiel. Quand ce communiqué paraît, Binance 14 est sous le contrôle de l'attaquant depuis plus de trois heures.

#### B51 · Les marchés
[VISUEL: courbes : Bitcoin sous 78 500 $, Ethereum sous 2 250 $, BNB −9 % ; une barre de liquidations de 629 M$]
[TEXTE À L'ÉCRAN: "629 000 000 $ liquidés en 1 h · dont 607 000 000 $ de positions acheteuses"]
[SFX: alerte]
[MUSIQUE: tension]
Les marchés n'ont pas attendu. Bitcoin passe sous 78 500 dollars. Ethereum casse son support à 2 250. Le BNB, la monnaie de Binance, perd 9 % dans la journée. En une heure, 629 millions de dollars de positions sont liquidées, dont 607 millions sur des paris à la hausse. Une liquidation, c'est une plateforme qui revend de force la position d'un trader qui a emprunté, quand le prix passe sous un seuil.

#### B52 · Retour au cold open
[VISUEL: l'écran de la scène 1 : "00:42:59 — 200 000 000 USDT" ; puis "00:44:11 — 0"]
[TEXTE À L'ÉCRAN: "00:42:59 → 00:44:11 — 72 secondes"]
[SFX: glitch, puis silence]
[MUSIQUE: coupe]
[RÉF. ON-CHAIN: transfert de 200 M USDT vers Binance 14 puis sortie, 00:42:59 → 00:44:11 UTC+3 — hashes à renseigner, S-04]
00 h 42 min 59 s. Une heure et dix-huit minutes après le premier balayage. Binance 14 reçoit 200 millions d'USDT. Le portefeuille a fait ce qu'il fait depuis une heure : il a répondu à son nouveau maître. Soixante-douze secondes plus tard, les 200 millions étaient chez l'attaquant. La machine n'a trahi personne. Elle a fait exactement ce pour quoi on l'avait construite.

#### B53 · Changement de bataille
[VISUEL: un duel : l'attaquant à gauche ; à droite, un tableau de boutons rouges "Tether · Circle · Ripple · Arbitrum"]
[TEXTE À L'ÉCRAN: "À partir d'ici : l'attaquant contre ceux qui ont un bouton"]
[SFX: whoosh]
[MUSIQUE: transition vers un thème plus tendu]
À partir de là, le duel change de nature. Ce n'est plus l'attaquant contre une machine. C'est l'attaquant contre des gens qui, eux, ont un bouton. Et on va y venir. Mais avant, il faut comprendre comment une seule de ces portefeuilles a pu signer l'impossible.

---

## F. TWIST / RÉVÉLATION TECHNIQUE (22:00 – 28:00)

#### B54 · EIP-7702, en une phrase
[VISUEL: un compte ordinaire (EOA) qui emprunte la silhouette d'un contrat ; le mot "EIP-7702" s'affiche en cyan]
[TEXTE À L'ÉCRAN: "EIP-7702 : un portefeuille ordinaire peut emprunter du code"]
[SFX: déclic]
[MUSIQUE: ambiante, claire]
Voici la mécanique centrale du dossier. Elle s'appelle EIP-7702. Une EIP, c'est une proposition d'amélioration d'Ethereum. Celle-ci est entrée en service avec la mise à jour de mai 2025. Retiens cette phrase : elle permet à un portefeuille ordinaire d'emprunter, temporairement, le code d'un contrat intelligent.

#### B55 · La procuration
[VISUEL: une feuille de procuration signée ; trois champs : réseau / adresse du code / numéro (nonce) ; un tampon "signée par la clé du portefeuille"]
[TEXTE À L'ÉCRAN: "Autorisation = [réseau, code à emprunter, nonce] + signature"]
[SFX: tampon]
[MUSIQUE: stable]
Comment ça marche ? Le propriétaire signe une petite feuille, comme une procuration. Trois champs : le réseau, l'adresse du code qu'on emprunte, et un numéro, notre vieux nonce, pour que la feuille ne serve qu'une fois. N'importe qui peut ensuite apporter cette feuille signée au réseau, et payer lui-même les frais.

#### B56 · Ce que le protocole garantit
[VISUEL: un cadenas au-dessus de la signature ; la phrase "signée par la clé du compte"]
[TEXTE À L'ÉCRAN: "Garantie : seule la clé du compte peut produire la feuille"]
[SFX: aucun]
[MUSIQUE: stable]
Une fois la feuille acceptée, le portefeuille change : quand on lui parle, c'est le code emprunté qui répond. Elle reste valable tant que son propriétaire ne signe pas une autre feuille pour l'annuler. Et le protocole ne transige que sur un point : cette feuille doit être signée avec la clé du compte lui-même. Personne d'autre ne peut la fabriquer. Donc une feuille qui arrive au réseau et qui passe la vérification de signature est, par construction, légitime.

#### B57 · Le raisonnement qui s'effondre
[VISUEL: un syllogisme : "Signature valide ⇒ le propriétaire a voulu" ; un point d'interrogation s'insère entre les deux]
[TEXTE À L'ÉCRAN: "Signature valide ≠ intention du propriétaire"]
[SFX: glitch]
[MUSIQUE: tension]
Et voici où tout s'effondre. Ce raisonnement est vrai pour un humain qui garde sa clé près de lui. Il est faux pour une machine qui signe tout ce qu'on lui demande. La feuille est parfaitement valide. Simplement, ce n'est pas le propriétaire qui l'a voulue : c'est quelqu'un qui avait accès à la machine qui signe.

#### B58 · Le trou dans la serrure
[VISUEL: une fonction de signature qui répond "OK" à toute demande venue de l'intérieur du système]
[TEXTE À L'ÉCRAN: "Une feuille mal formée n'est pas rejetée : elle est ignorée."]
[SFX: clic]
[MUSIQUE: stable]
Un détail du protocole joue en faveur de l'attaquant. Si une feuille a un mauvais numéro, le réseau ne fait pas échouer la transaction : il l'ignore, et passe à la suivante. C'est ce qui rend les cinquante feuilles possibles. On en tend cinquante, quarante-neuf sont ignorées, une prend. Aucun risque d'échec, aucun frais perdu pour rien.

#### B59 · Les trois détails qui tuent
[VISUEL: trois fiches "preuve" : "signatures fraîches" / "frais payés par un tiers" / "huit réseaux, une seule ruse"]
[TEXTE À L'ÉCRAN: "3 détails qui tuent"]
[SFX: tampon x3]
[MUSIQUE: montée]
Voici maintenant les trois détails que presque personne n'a remarqués. Premier détail : les cinquante signatures partent d'un numéro que le portefeuille avait environ trois minutes avant l'exécution. Elles n'ont pas été fabriquées la veille. Selon les relevés relayés, elles ont été demandées minutes avant. Cela suggère un accès vivant au système de signature, pas des signatures volées des semaines plus tôt. C'est une inférence, pas une preuve.

#### B60 · Deuxième détail
[VISUEL: une facture de frais "payé par : adresse inconnue" ; un tampon rouge]
[TEXTE À L'ÉCRAN: "Les frais ont été payés par l'attaquant, pas par Binance"]
[SFX: glitch]
[MUSIQUE: stable]
Deuxième détail : les frais de la transaction ont été payés par l'attaquant. Pas par Binance. Une plateforme dont un étranger règle les frais d'administration, c'était un signal à lire en temps réel. Personne ne l'a lu.

#### B61 · Troisième détail
[VISUEL: tableau de huit réseaux ; sur une seule ligne, la mention "7702"]
[TEXTE À L'ÉCRAN: "8 réseaux · 1 seule ruse nécessaire"]
[SFX: aucun]
[MUSIQUE: tension]
Troisième détail, celui qui tue. Sur huit réseaux, un seul portefeuille a eu besoin de cette ruse : Binance 14. Bitcoin, XRP Ledger, Tron n'ont tout simplement pas de mécanisme comme EIP-7702. Sur ces réseaux, il n'y avait aucune feuille à forger : les portefeuilles ont signé leurs transferts, un par un, de façon ordinaire. Pense à ça. S'il avait eu une seule clé volée, il aurait vidé un seul portefeuille. Là, des portefeuilles de huit réseaux, avec des types de clés différents, ont signé en moins d'une demi-heure.

#### B62 · Ce qui est commun à tous
[VISUEL: huit clés différentes qui convergent vers un même entonnoir "système de signature"]
[TEXTE À L'ÉCRAN: "Point commun : la machine qui signe"]
[SFX: aucun]
[MUSIQUE: stable]
Le seul point commun possible entre toutes ces signatures, c'est la machine qui les produit. Pas une clé, pas un réseau, pas une astuce : le système qui, pour Binance, répond « oui » à la question « cette signature est-elle valide ? ». La blockchain peut prouver que les signatures sont authentiques. Elle ne peut pas dire qui a demandé de signer.

#### B63 · Pourquoi ça n'a pas été détecté
[VISUEL: trois détecteurs en rang : valeur / nonce / destination ; les trois restent verts]
[TEXTE À L'ÉCRAN: "Valeur 0 · nonce normal · destination à l'intérieur d'un contrat"]
[SFX: silence]
[MUSIQUE: nappe suspendue]
Pourquoi cela n'a-t-il pas été détecté ? Parce que, pour un détecteur classique, tout paraissait normal. La valeur visible de la transaction : zéro. Le nonce : cohérent. Et le seul signe d'alerte, un portefeuille dont le code change, n'est pas un événement que beaucoup de systèmes surveillent pour un portefeuille qui n'a jamais eu de code.

#### B64 · La version de Binance
[VISUEL: capture simulée du communiqué du 30 octobre ; trois phrases surlignées ; un bandeau "RAPPORTÉ"]
[TEXTE À L'ÉCRAN: "30 oct. — « ordinateur portable compromis · conteneur de service »"]
[SFX: notification]
[MUSIQUE: stable]
Le 30 octobre, Binance publie ses premiers résultats. Selon l'entreprise, l'enquête préliminaire indique qu'un ordinateur portable compromis, celui d'un ingénieur, aurait permis à l'attaquant d'accéder à un conteneur de service et de soumettre des retraits non autorisés. Elle ajoute n'avoir trouvé aucune preuve de fuite d'une clé privée de portefeuille. L'ingénieur est de l'équipe DevOps, celle qui construit et exploite les systèmes eux-mêmes : serveurs, déploiement, infrastructure.

#### B65 · Un conteneur de service
[VISUEL: une pièce fermée à l'intérieur d'un grand bâtiment ; un petit programme à l'intérieur ; une porte qu'un laptop ouvre]
[TEXTE À L'ÉCRAN: "Conteneur de service = une pièce fermée dans le système"]
[SFX: porte]
[MUSIQUE: stable]
Un conteneur de service, c'est une pièce fermée à l'intérieur du système : un programme qui tourne avec des droits précis. Binance n'a pas dit quel programme se trouvait dans celui-là, ni quels étaient ses droits exacts. Seulement que l'attaquant a pu, à travers lui, soumettre des demandes de retrait. Quelques heures plus tard, l'entreprise a dit avoir trouvé des points d'intrusion supplémentaires, sans les détailler.

#### B66 · Ce que dit Richard Teng
[VISUEL: communiqué simulé ; une ligne : "opération complexe" ; une autre : "aucune responsabilité individuelle retenue"]
[TEXTE À L'ÉCRAN: "Richard Teng : opération complexe · aucun individu mis en cause"]
[SFX: aucun]
[MUSIQUE: stable]
Le co-directeur général, Richard Teng, dit que l'attaque était une opération complexe, et non l'abus des droits d'un seul ingénieur. L'enquête n'a, selon lui, imputé la responsabilité à personne. Et ça répond, à sa façon, à la question de départ : celui qui signait pour Binance cette nuit-là, c'était Binance elle-même, par une machine de son propre bâtiment.

#### B67 · Le récit a bougé
[VISUEL: une ligne de temps des déclarations, avec trois versions : "composant logiciel compromis" → "ordinateur portable" → "EIP-7702 / multi-signature"]
[TEXTE À L'ÉCRAN: "La version officielle a changé au fil des jours"]
[SFX: glitch]
[MUSIQUE: tension légère]
Une remarque d'enquêteur, puisqu'on est dans un dossier chaud. Le récit officiel a bougé en trois jours. Les premières déclarations parlaient d'un composant logiciel compromis. Puis d'un ordinateur portable. D'autres comptes rendus, de presse, ont attribué à Richard Teng une phrase sur EIP-7702 qui mélange les mécanismes. Je ne tranche pas : j'indique que le récit n'est pas stable.

#### B68 · Ce que la chaîne confirme, et ce qu'elle ne peut pas confirmer
[VISUEL: deux colonnes : "compatible" ; "non démontré"]
[TEXTE À L'ÉCRAN: "Compatible avec la version de Binance. Non prouvé."]
[SFX: aucun]
[MUSIQUE: stable]
Reste à confronter la chaîne à cette version. Les signatures fraîches, produites trois minutes avant l'exécution selon les relevés relayés, collent avec un attaquant qui demande à un système de signer en direct. La chaîne est donc compatible avec la version de Binance. Mais compatible n'est pas prouvé : un portefeuille de transactions ne dira jamais quel ordinateur a envoyé la demande.

---

## G. LA RÉPONSE / LA POURSUITE (28:00 – 35:00)

#### B69 · Les boutons d'urgence, mode d'emploi
[VISUEL: le code simplifié d'un contrat USDT : "addBlackList(user) — onlyOwner" ; un bouton rouge]
[TEXTE À L'ÉCRAN: "addBlackList(adresse) — réservé au propriétaire du contrat"]
[SFX: clic]
[MUSIQUE: ambiante]
Reprenons les boutons d'urgence, proprement. Le contrat de l'USDT contient une fonction qui ajoute une adresse à une liste noire. Seul le propriétaire du contrat, Tether, peut l'appeler. Et une adresse sur liste noire ne peut plus bouger un seul dollar d'USDT. Circle, avec l'USDC, a le même mécanisme. Un seul compte autorisé, une seule fonction.

#### B70 · Qui a le bouton pour quoi
[VISUEL: tableau : USDT → Tether ; USDC → Circle ; RLUSD → Ripple ; or numérique → Paxos ; WLFI → World Liberty ; ETH, BTC, XRP → personne]
[TEXTE À L'ÉCRAN: "Chaque jeton a son gardien. Les monnaies natives n'en ont pas."]
[SFX: aucun]
[MUSIQUE: stable]
Chaque jeton a donc son gardien. Tether pour l'USDT, Circle pour l'USDC, Ripple pour le RLUSD, Paxos pour l'or numérique. Et pour l'Ether, le Bitcoin, le XRP : personne. Et l'attaquant le savait mieux que n'importe qui d'autre cette nuit-là.

#### B71 · La stratégie : changer de monnaie
[VISUEL: l'attaquant qui échange des USDT contre de l'Ether à travers des "solveurs d'intention" ; compteur 325 M$ en 15 min]
[TEXTE À L'ÉCRAN: "23:34 → 23:49 — 325 000 000 USDT → ETH"]
[SFX: whoosh]
[MUSIQUE: tension]
[RÉF. ON-CHAIN: échanges d'environ 325 M USDT contre ETH via solveurs d'intention et Uniswap, 23:34 → ~23:49 UTC+3 — hashes à renseigner, S-15]
23 h 34, une minute après la dernière vague. L'attaquant ne garde pas ses USDT : un jeton gelable. Il utilise des « solveurs d'intention », des acteurs qui se font concurrence pour exécuter un échange à ta place, et la plateforme Uniswap. En un quart d'heure, 325 millions d'USDT se changent en Ether. L'Ether n'a pas de bouton.

#### B72 · 23 h 52 : encore 190 millions
[VISUEL: une nouvelle adresse reçoit 190 M USDT ; la flèche indique "diversion"]
[TEXTE À L'ÉCRAN: "23:52:59 — 190 000 000 USDT sur une nouvelle adresse"]
[SFX: notification]
[MUSIQUE: stable]
[RÉF. ON-CHAIN: 190 M USDT vers une nouvelle adresse, 23:52:59 UTC+3 — hash à renseigner, S-15]
À 23 h 52 min 59 s, une nouvelle adresse de l'attaquant reçoit 190 millions d'USDT. Il disperse. Chaque adresse est une cible plus petite pour le bouton de Tether, qui doit désigner les adresses une à une.

#### B73 · 23 h 57 : le premier bouton
[VISUEL: un bandeau "World Liberty Financial" ; un cadenas se ferme sur l'Adresse 1 ; 2,5 M$]
[TEXTE À L'ÉCRAN: "23:57:47 — premier gel · WLFI · ≈ 2 500 000 $"]
[SFX: cadenas]
[MUSIQUE: pulsation]
23 h 57 min 47 s. Premier bouton pressé. Pas Tether, pas Circle : World Liberty Financial, qui gèle l'Adresse 1 pour son propre jeton, le WLFI. Environ 2,5 millions de dollars. Un petit montant, mais c'est le premier signe que quelqu'un, quelque part, veille.

#### B74 · L'astuce Aave
[VISUEL: schéma du prêt : l'attaquant dépose 10 M USDT, emprunte 3 271 ETH ; une minute après, 50 M USDT, emprunte 16 490 ETH]
[TEXTE À L'ÉCRAN: "23:57:59 — Aave : 10 M$ USDT en garantie → 3 271 ETH · +1 min : 50 M$ → 16 490 ETH"]
[SFX: déclic x2]
[MUSIQUE: tension]
[RÉF. ON-CHAIN: dépôts USDT sur Aave (10 M$ puis 50 M$) et emprunts de 3 271 ETH puis 16 490 ETH, 23:57:59 → ~23:59 UTC+3 — hashes à renseigner, S-16]
Douze secondes plus tard, 23 h 57 min 59 s, l'attaquant va sur Aave, un protocole de prêt décentralisé. Tu y déposes des actifs en garantie, et tu empruntes dessus. Il dépose 10 millions d'USDT, emprunte 3 271 Ether. Une minute plus tard, 50 millions d'USDT en garantie, 16 490 Ether empruntés. Tu vois la manœuvre : les USDT qu'il détient peuvent être gelés à tout moment. Il les met en gage et ressort de l'Ether, que personne ne peut geler. Il met en gage de l'argent qu'il sait perdu.

#### B75 · Tether presse le bouton
[VISUEL: l'Adresse 1 passe sur liste noire ; 971 M$ USDT figés ; chrono 00:01:35]
[TEXTE À L'ÉCRAN: "00:01:35 — Tether : liste noire · 971 000 000 USDT figés"]
[SFX: impact, cadenas]
[MUSIQUE: pic puis retombée]
[RÉF. ON-CHAIN: mise sur liste noire de l'Adresse 1 par Tether, 00:01:35 UTC+3, 971 M USDT — hash à renseigner, S-17]
00 h 01 min 35 s. Enfin, Tether presse le bouton. L'Adresse 1 passe sur liste noire. À cet instant, elle contient 971 millions d'USDT, qui ne bougeront plus.

#### B76 · 48 secondes de trop
[VISUEL: deux horloges ; l'une montre 00:01:59 (le transfert), l'autre 00:02:47 (le gel) ; un écart de 48 s]
[TEXTE À L'ÉCRAN: "00:01:59 transfert · 00:02:47 gel · 48 s de retard"]
[SFX: tic]
[MUSIQUE: stable]
[RÉF. ON-CHAIN: transfert de 130 M USDT d'une adresse Aave à 00:01:59, gel de cette adresse par Tether à 00:02:47 UTC+3 — hashes à renseigner, S-17]
Vingt-quatre secondes plus tard, à 00 h 01 min 59 s, l'attaquant retire les 130 millions restants de son adresse Aave, vers une autre adresse. À 00 h 02 min 47 s, Tether gèle l'adresse Aave : vide. Elle arrive 48 secondes trop tard. Deux minutes après, à 00 h 04 min 59 s, c'est au tour de Circle de geler 823 millions d'USDC sur l'Adresse 1. Tous les USDC qui sont arrivés cette nuit-là sont gelés. Pas un dollar d'USDC n'est sorti.

#### B77 · L'ironie de l'adresse prisonnière
[VISUEL: l'Adresse 1 en cellule ; un robinet qui continue de couler dedans]
[TEXTE À L'ÉCRAN: "971 000 000 → 1 175 000 000 USDT sur une adresse gelée"]
[SFX: goutte]
[MUSIQUE: stable]
Un détail presque comique. L'Adresse 1 est gelée avec 971 millions d'USDT. Un peu plus tard, elle en contient 1 milliard 175 millions. D'où viennent ces 200 millions de plus ? De l'attaquant lui-même : les balayages qu'il avait programmés continuaient de verser sur une adresse qu'il ne contrôlait plus. Le système qui volait pour lui ne savait pas que sa destination était devenue une cellule.

#### B78 · Tron
[VISUEL: l'attaquant retire 300 M$ de 612 M$ ; Tether gèle à 00:09:12 ; 66 M$ rattrapés ; 234 M$ échangés sur une plateforme de Tron]
[TEXTE À L'ÉCRAN: "00:09:12 — Tether gèle le compte Tron · 300 000 000 $ déjà partis"]
[SFX: whoosh]
[MUSIQUE: tension]
[RÉF. ON-CHAIN: compte Tron à 612 M$ USDT, retraits d'environ 300 M$ avant gel à 00:09:12 UTC+3 ; 66 M$ rattrapés, 234 M$ échangés ; 638 M TRX vers un compte neuf — hashes à renseigner, S-10]
Sur Tron, le compte neuf contient 612 millions d'USDT. Quand Tether arrive, l'attaquant en a déjà sorti 300 millions. À 00 h 09 min 12 s, le compte est gelé : le reste est figé. Sur les 300 millions partis, Tether en rattrape 66 millions sur une autre adresse. Les 234 millions restants sont échangés sur des plateformes décentralisées de Tron. Et vers un nouveau compte arrivent 638 millions de TRX. Les USDT gelés sont entrés par une porte, et sont ressortis par l'autre sous forme de TRX, que personne ne peut geler.

#### B79 · Entre l'USDT et ce qui n'a pas de bouton
[VISUEL: 00:11 or numérique 50 M$ gelé ; 00:14 175 M$ USDT rattrapés après 6 min 36 s ; 00:18:59 30 M$ rattrapés après 2 min 48 s]
[TEXTE À L'ÉCRAN: "6 min 36 s · 2 min 48 s : la différence entre fuir et être rattrapé"]
[SFX: tic]
[MUSIQUE: stable]
00 h 11 : environ 50 millions de dollars d'or numérique sont gelés sur l'Adresse 1. 00 h 14 : 175 millions d'USDT sont gelés sur une adresse intermédiaire, six minutes et trente-six secondes après leur arrivée. 00 h 18 min 59 s : 30 millions sont gelés sur une autre, deux minutes et quarante-huit secondes après leur arrivée. Voilà ce que cette nuit mesure : la différence entre ce qui s'échappe et ce qui est rattrapé se compte en minutes.

#### B80 · Ripple : 321 transactions
[VISUEL: un bloc Ethereum ; la transaction de l'attaquant en position 7 ; le gel de Ripple en position 328]
[TEXTE À L'ÉCRAN: "Même bloc · position 7 contre position 328 · 321 transactions d'écart"]
[SFX: tic prolongé]
[MUSIQUE: pulsation]
[RÉF. ON-CHAIN: 88,5 M RLUSD sortis de l'Adresse 1 à 00:22 UTC+3 ; gel Ripple à 01:59 UTC+3 ; 40,5 M RLUSD gelés — hashes à renseigner, S-18]
Le moment le plus serré de la nuit, c'est le RLUSD de Ripple. L'attaquant en retire 88,5 millions sur Ethereum et les passe par trois adresses relais. Le gel de Ripple arrive. Pour comprendre, un mot sur la mécanique : les transactions ne s'écrivent pas une à une dans le grand livre, elles sont regroupées en pages, des blocs. Sur Ethereum, un nouveau bloc tous les 12 secondes environ, et à l'intérieur, les transactions sont rangées dans un ordre. La dernière transaction de l'attaquant était en position 7 de son bloc. Le gel de Ripple, dans le même bloc, en position 328. 321 transactions d'écart : tout est là. Ripple en a gelé 40,5 millions. Certaines déclarations citent un chiffre bien supérieur. Sur Ethereum, tout ce qui était sorti de l'adresse en RLUSD, c'était 88,5 millions.

#### B81 · Les autres gardiens
[VISUEL: Paxos qui gèle l'or ; Binance qui gèle son propre WBETH ; chrono 01:48 ; 74 M$]
[TEXTE À L'ÉCRAN: "01:48 — Binance gèle son propre jeton WBETH · ≈ 74 000 000 $"]
[SFX: cadenas]
[MUSIQUE: stable]
[RÉF. ON-CHAIN: gel du WBETH détenu par l'attaquant par Binance, 01:48 UTC+3, ≈ 74 M$ — hash à renseigner, S-19]
Les boutons s'enchaînent. World Liberty gèle ses dollars numériques. Paxos gèle son or. À 01 h 48, Binance elle-même presse un bouton : le WBETH, une version d'Ether que Binance émet, détenue par l'attaquant : environ 74 millions de dollars. La victime gèle l'argent de son voleur, sur son propre jeton.

#### B82 · Arbitrum : le conseil de sécurité
[VISUEL: un conseil de douze personnes en silhouette ; un bouton rouge sous verre ; un transfert « système » qui passe sans signature]
[TEXTE À L'ÉCRAN: "03:18 — Arbitrum · Security Council · 8 000+ ETH déplacés"]
[SFX: déclic]
[MUSIQUE: tension]
[RÉF. ON-CHAIN: transactions système Arbitrum déplaçant plus de 8 000 ETH et de l'ARB vers un portefeuille gelé, 03:18 UTC+3 — hash à renseigner, S-20]
À 03 h 18, un événement que presque personne n'attendait. Sur Arbitrum, l'attaquant détient plus de 8 000 Ether. L'Ether n'a pas de bouton. C'est la règle. Mais Arbitrum a un conseil de sécurité, un petit groupe élu qui possède des pouvoirs d'urgence. Il lance des transactions « système », qui n'ont pas besoin de la signature du propriétaire de l'adresse, et déplace l'Ether, avec le jeton ARB, dans un portefeuille gelé. La règle d'or de la blockchain n'a tenu que parce que personne ne s'était arrogé ce pouvoir. Là, quelqu'un l'a fait. L'attaquant a pris des milliards parce qu'il avait la signature du propriétaire. Et il a perdu de l'Ether parce que quelqu'un n'a pas eu besoin de cette signature.

#### B83 · Le bilan à 03 h 52
[VISUEL: un compteur de "gelé" qui monte de 5 M$/min ; un chiffre mesuré 2 832 M$]
[TEXTE À L'ÉCRAN: "03:52 — Binance : « ≈ 3 milliards gelés en 90 min » · mesure on-chain : 2 832 000 000 $"]
[SFX: notification]
[MUSIQUE: stable]
À 03 h 52, Binance annonce qu'environ 3 milliards de dollars ont été gelés en 90 minutes, un compteur qui montait de 5 millions de dollars par minute. Selon la mesure on-chain que nous reprenons, la somme réellement gelée chez l'attaquant s'élève à 2 milliards 832 millions de dollars. Selon les médias, la fourchette va de 2,4 milliards à environ 3 milliards, parce que les définitions de « gelé » ne sont pas les mêmes.

#### B84 · Le bouton qui a visé Binance
[VISUEL: Tether presse le bouton, mais l'adresse visée est "Binance 14" ; 01:06:23]
[TEXTE À L'ÉCRAN: "01:06:23 — Tether met Binance 14 sur liste noire"]
[SFX: cadenas, glitch]
[MUSIQUE: tension]
Au milieu de tous ces gels, un détail étrange. À 01 h 06 min 23 s, Tether place sur liste noire une adresse qui n'est pas celle de l'attaquant. C'est Binance 14. Le bouton conçu pour arrêter le voleur a aussi gelé la victime. Et ça a des conséquences, on va le voir.

#### B85 · Les retraits suspendus, mais pas le portefeuille
[VISUEL: un bouton "retraits" en rouge dans l'application Binance ; derrière, Binance 14 continue d'émettre]
[TEXTE À L'ÉCRAN: "01:15 — Binance suspend les retraits (clients) · Binance 14 : toujours délégué"]
[SFX: alerte]
[MUSIQUE: tension]
À 01 h 15, Binance suspend les retraits sur plusieurs réseaux, une heure et cinquante minutes après le premier balayage. On pourrait croire que tout est sous contrôle. Pas du tout. Le retrait qu'on suspend, c'est celui du client, le bouton de l'application. Binance 14 avait un autre maître, qui ne passait par aucun bouton : il parlait directement au code.

#### B86 · 01 h 55 : Binance signe elle-même
[VISUEL: 47 transactions de sauvetage qui défilent ; frais 5 à 8 fois plus élevés que ceux de l'attaquant]
[TEXTE À L'ÉCRAN: "01:55:35 — Binance 14 signe avec sa propre clé · 47 transactions de sauvetage"]
[SFX: notifications rapides]
[MUSIQUE: pulsation rapide]
[RÉF. ON-CHAIN: 47 transactions de sauvetage de Binance 14 vers une adresse sûre, 01:55:35 → 03:07:11 UTC+3, frais 5 à 8 fois supérieurs à ceux de l'attaquant — hashes à renseigner, S-21]
À 01 h 55 min 35 s, pour la première fois de la nuit, Binance 14 envoie une transaction avec sa propre clé. Binance, cette fois, parle à travers son propre portefeuille. Elle envoie ce qui reste vers une adresse sûre, avec des frais cinq à huit fois plus élevés que ceux de l'attaquant, pour passer devant lui. 47 transactions de sauvetage, l'une derrière l'autre. Imagine la scène : sur le même portefeuille, d'un côté son vrai propriétaire qui retire ce qu'il peut, de l'autre le code planté qui continue de balayer.

#### B87 · Le sauvetage qui échoue
[VISUEL: une transaction de 1 350 000 USDT en rouge "échec" ; la raison : "adresse sur liste noire"]
[TEXTE À L'ÉCRAN: "Sauvetage de 1 350 000 USDT : échec — liste noire Tether"]
[SFX: glitch]
[MUSIQUE: tension]
Parmi ces transactions de sauvetage, une tente de récupérer 1 million 350 mille USDT. Elle échoue. Pourquoi ? Parce que Tether a mis Binance 14 sur liste noire à 01 h 06. Le bouton qui devait protéger l'argent de Binance a empêché Binance de sauver son propre argent.

#### B88 · Huit réseaux
[VISUEL: Avalanche et Polygon s'allument : un cinquième portefeuille, puis un autre ; compteur "8 réseaux"]
[TEXTE À L'ÉCRAN: "02:04:30 Avalanche · ≈ 02:06 Polygon — 8 réseaux touchés"]
[SFX: whoosh x2]
[MUSIQUE: stable]
À 02 h 04 min 30 s, sur Avalanche, un cinquième portefeuille de Binance envoie une nouvelle fois à l'attaquant. Une minute et demie plus tard, Polygon. Le compte passe à huit réseaux, cinquante minutes environ après la suspension des retraits. Des portefeuilles continuent de signer pour l'attaquant. Qui tient la signature à ce stade ? On ne le sait pas encore. Tether, de son côté, rattrape des USDT arrivés sur Polygon 19 minutes et 44 secondes après leur arrivée. Le reste n'a pas de bouton.

#### B89 · 02 h 55 : la dernière recharge
[VISUEL: la même adresse de recharge qu'à 23:19 envoie 3 000 ETH ; compteur 6,8 M$ ; chrono +60 s ; dernier balayage]
[TEXTE À L'ÉCRAN: "02:55:47 — +3 000 ETH (≈ 6 800 000 $) · +60 s — dernier balayage"]
[SFX: notification, glitch]
[MUSIQUE: tension]
À 02 h 55 min 47 s, Binance 14 reçoit 3 000 Ether, environ 6 millions 800 mille dollars. De quelle adresse ? De la même qui l'avait rechargée à 23 h 19, 84 secondes avant la frappe. Près de quatre heures après le début, alors que toute la planète regarde, une adresse continue d'alimenter ce portefeuille. 60 secondes plus tard, ces 3 000 Ether sont balayés. C'est le dernier balayage de l'attaquant.

#### B90 · La révocation
[VISUEL: Binance 14 envoie une autorisation de type 4 vers l'adresse zéro ; le champ "code" redevient vide ; chrono 3:49:36]
[TEXTE À L'ÉCRAN: "03:10:35 — délégation révoquée · 3 h 49 min 36 s après la prise"]
[SFX: verrou]
[MUSIQUE: résolution]
[RÉF. ON-CHAIN: transaction de type 4 de Binance 14 révoquant la délégation, 03:10:35 UTC+3 — hash à renseigner, S-22]
À 03 h 04, la cofondatrice Yi He écrit que Binance couvrira toutes les pertes liées à ce piratage. À 03 h 07 min 11 s, dernière transaction de sauvetage. À 03 h 10 min 35 s, Binance 14 s'envoie à elle-même une transaction du type qui avait ouvert la porte : une autorisation neuve, qui dit non plus « emprunte le code de l'attaquant », mais « reviens vide ». Le code du portefeuille redevient zéro. La porte est refermée. 3 heures, 49 minutes et 36 secondes après son ouverture.

#### B91 · Pourquoi si long ?
[VISUEL: un compteur de 3 h 49 min ; une clé qui dort sur une table]
[TEXTE À L'ÉCRAN: "La clé était chez Binance dès la première minute."]
[SFX: aucun]
[MUSIQUE: nappe suspendue]
Pourquoi cette révocation a-t-elle pris près de quatre heures, alors que la clé était chez Binance depuis la première minute ? C'est l'une des questions ouvertes de ce dossier, et personne n'y a répondu. Environ trois minutes plus tard, Binance annonce la suspension complète de tous les dépôts et retraits. La porte était fermée. Mais fermée ne veut pas dire que la maison était sauve.

---

## H. ATTRIBUTION & QUESTIONS OUVERTES (35:00 – 40:00)

#### B92 · Binance 16, la seule sans ruse
[VISUEL: côte à côte : Binance 14 (code emprunté, 50 autorisations) / Binance 16 (rien : 9 transactions banales)]
[TEXTE À L'ÉCRAN: "Binance 16 : aucune délégation · 9 transactions ordinaires"]
[SFX: aucun]
[MUSIQUE: stable]
Revenons à Binance 16, celle de 23 h 24 min 47 s. Elle n'a aucune délégation. Pas de code emprunté, pas de feuille d'autorisation, pas de cinquante nonces. Elle a envoyé neuf transactions ordinaires, du type que n'importe quel portefeuille du monde envoie tous les jours, signées avec sa propre clé, aux mêmes frais que ceux qu'elle payait ce soir-là. Si tu l'avais regardée cette nuit, tu n'aurais rien vu d'anormal.

#### B93 · Toutes les autres
[VISUEL: sept réseaux ; chacun : « transactions ordinaires » ; la ruse n'existe que sur Ethereum]
[TEXTE À L'ÉCRAN: "Bitcoin, XRP, Tron, Optimism, Arbitrum, Avalanche, Polygon : transactions ordinaires"]
[SFX: aucun]
[MUSIQUE: stable]
Et les autres ? Nous avons recoupé, réseau par réseau, les relevés publiés : les cinq comptes du XRP Ledger, les onze transactions Bitcoin, Tron, Optimism, Arbitrum, Avalanche, Polygon. Toutes des transactions ordinaires, signées par les portefeuilles eux-mêmes. Pour le XRP Ledger, le Bitcoin et Tron, EIP-7702 n'existe tout simplement pas. Entre Binance 14 et les autres portefeuilles, rien ne les relie, sauf le système qui signe.

#### B94 · L'écho de Bitget et de Bybit
[VISUEL: trois frises : Bybit févr. 2025 (≈ 1,5 Md$) · Bitget il y a 5 semaines (388 M$) · Binance oct. 2026]
[TEXTE À L'ÉCRAN: "La signature légitime : Bybit → Bitget → Binance"]
[SFX: tampon]
[MUSIQUE: tension]
Le schéma te rappelle quelque chose. En février 2025, Bybit perdait environ un milliard et demi de dollars : un poste de développeur compromis chez le prestataire de portefeuille, et de vrais signataires qui avaient validé une transaction qu'on leur avait présentée comme saine. Il y a cinq semaines, Bitget : 388 millions de dollars, des portefeuilles qui signent leur propre vol. Une société de sécurité, Blockaid, estime que le mode opératoire sur Binance ressemble beaucoup à celui de Bybit. C'est son avis, pas un fait établi, mais la parenté saute aux yeux.

#### B95 · Qui est derrière ?
[VISUEL: trois fiches d'attribution : TRM Labs / Chainalysis / ZachXBT ; chaque fiche porte le tampon "ATTRIBUTION — pas une preuve"]
[TEXTE À L'ÉCRAN: "ATTRIBUTION ≠ PREUVE"]
[SFX: tampon]
[MUSIQUE: stable]
Qui est derrière ? Rapportons les attributions, en gardant en tête que ce sont des attributions, pas des preuves. TRM Labs, la société d'analyse blockchain, attribue l'attaque avec un haut niveau de confiance à TraderTraitor, un groupe que le gouvernement américain relie à la Corée du Nord. C'est le nom que le FBI avait utilisé pour Bybit. D'après Forbes, Chainalysis arrive à la même conclusion.

#### B96 · ZachXBT
[VISUEL: un graphe de flux qui relie "vol Binance" et "vol Bitget" à une même adresse, via un nœud THORChain]
[TEXTE À L'ÉCRAN: "Vendredi : des fonds Binance et Bitget convergent vers une même adresse"]
[SFX: glitch discret]
[MUSIQUE: stable]
Vendredi, un développement nouveau : l'enquêteur ZachXBT publie que des fonds issus du vol de Binance et des fonds issus du vol de Bitget arrivent à la même adresse Ethereum, après être passés par THORChain, une plateforme d'échange entre réseaux. Pour lui, cela indique que le même groupe est probablement derrière les deux attaques. Et selon lui, Bitget était déjà attribué à TraderTraitor. C'est donc l'avis de TRM, de Chainalysis et de ZachXBT.

#### B97 · L'Inspecteur se réserve son jugement
[VISUEL: une balance ; d'un côté "éléments qui convergent", de l'autre "éléments qui manquent"]
[TEXTE À L'ÉCRAN: "Les éléments convergent. L'enquête reste ouverte."]
[SFX: aucun]
[MUSIQUE: stable]
L'Inspecteur se réserve son jugement. Les éléments convergent, mais l'enquête reste ouverte. À l'heure où cette vidéo est écrite, aucun gouvernement n'a attribué officiellement le vol de Binance. Ce que nous avons, c'est un faisceau d'avis d'analystes, qui pointent dans la même direction, et un mode opératoire que d'autres affaires ont déjà montré. Pas un verdict.

#### B98 · Question 1
[VISUEL: une question numérotée en cyan : "1"]
[TEXTE À L'ÉCRAN: "Q1 — Comment l'ordinateur portable a-t-il été compromis ?"]
[SFX: notification]
[MUSIQUE: stable]
Cinq questions auxquelles personne n'a répondu. Première : comment l'ordinateur portable de l'ingénieur a-t-il été compromis ? Par quel chemin, depuis quand, et jusqu'où l'attaquant est-il allé dans le système ? Binance dit avoir trouvé des points d'intrusion supplémentaires, mais n'a pas dit lesquels.

#### B99 · Question 2
[VISUEL: une question numérotée : "2" ; un chronomètre qui se fige à 28:18]
[TEXTE À L'ÉCRAN: "Q2 — Pourquoi aucune surveillance n'a coupé 28 minutes de retraits ?"]
[SFX: notification]
[MUSIQUE: stable]
Deuxième : pourquoi rien n'a-t-il arrêté des retraits de plusieurs milliards en 28 minutes, sur sept réseaux ? Aucun plafond par transaction qui bloque, aucune alerte qui coupe la signature. Qu'est-ce qui, dans le système de retraits, regardait quoi, ce soir-là ?

#### B100 · Question 3
[VISUEL: question numérotée : "3" ; un chrono 3:49:36]
[TEXTE À L'ÉCRAN: "Q3 — Pourquoi 3 h 49 min pour révoquer une délégation ?"]
[SFX: notification]
[MUSIQUE: stable]
Troisième : pourquoi a-t-il fallu environ quatre heures pour révoquer une délégation, alors que la clé était entre les mains de Binance depuis la première minute ? Ce n'était qu'une transaction à envoyer.

#### B101 · Question 4
[VISUEL: question numérotée : "4" ; des balayages qui continuent après "01:15"]
[TEXTE À L'ÉCRAN: "Q4 — Qui signait après l'arrêt des retraits ?"]
[SFX: notification]
[MUSIQUE: stable]
Quatrième : qui a signé la seconde vague, après la suspension des retraits ? À 02 h 04 puis 02 h 06, des portefeuilles ont encore versé à l'attaquant. Si le système de retraits était coupé, quelle main continuait à signer ?

#### B102 · Question 5
[VISUEL: question numérotée : "5" ; un trou de 378 M$ dans un graphique en barres]
[TEXTE À L'ÉCRAN: "Q5 — Où sont passés les 378 millions manquants au bilan ?"]
[SFX: notification]
[MUSIQUE: stable]
Cinquième, et c'est une question de comptable : où sont les 378 millions de dollars qui ne rentrent dans aucune colonne du bilan ? On va t'expliquer l'arithmétique dans une minute. Un dossier honnête a des trous, et celui-ci les montre.

---

## I. BILAN CHIFFRÉ & CONCLUSION (40:00 – 43:00)

#### B103 · Le total
[VISUEL: tableau de bord : huit réseaux et leurs montants ; un total en grand]
[TEXTE À L'ÉCRAN: "TOTAL MESURÉ (8 réseaux) : 6 257 000 000 $"]
[SFX: tic]
[MUSIQUE: ambiante, sombre]
[RÉF. ON-CHAIN: décompte sur huit réseaux, 23:04:52 → 02:56:47 UTC+3 — voir assets/timeline.json et sources.md S-23]
Faisons le bilan avec tous les chiffres que nous avons pu recouper. Total volé, mesuré sur huit réseaux : 6 milliards 257 millions de dollars. Avec Solana, que nous n'avons pas pu mesurer nous-mêmes, on arrive à environ 6,35 milliards, ce qui est proche des 6,3 milliards qu'annonce Binance. D'autres sources parlent de neuf réseaux : ce sont les mêmes huit plus Solana.

#### B104 · Gelé
[VISUEL: barre qui se remplit : 2 832 000 000 $ ; légende : "mesure on-chain · autres sources : 2,4 à 3 Md$"]
[TEXTE À L'ÉCRAN: "GELÉ : 2 832 000 000 $"]
[SFX: cadenas]
[MUSIQUE: stable]
Gelé : 2 milliards 832 millions de dollars selon notre mesure on-chain. Les autres sources vont de 2,4 à environ 3 milliards, selon ce qu'elles comptent. Tether annonce plus de 1,5 milliard d'USDT gelés, Circle plus de 800 millions d'USDC.

#### B105 · Encore chez l'attaquant
[VISUEL: barre : 3 047 000 000 $ ; détail : > 500 000 ETH ; > 18 000 BTC ; ≈ 233 M XRP ; ≈ 560 M TRX]
[TEXTE À L'ÉCRAN: "CHEZ L'ATTAQUANT : 3 047 000 000 $"]
[SFX: aucun]
[MUSIQUE: tension]
Encore chez l'attaquant, au dernier relevé que nous avons fait : 3 milliards 47 millions de dollars. Plus de 500 000 Ether, plus de 18 000 bitcoins, environ 233 millions de XRP, environ 560 millions de TRX, avec des actifs de moindre importance. Et ces fonds n'ont pas de bouton.

#### B106 · L'arithmétique qui ne tombe pas
[VISUEL: une addition : 2 832 + 3 047 = 5 879 ; 6 257 − 5 879 = 378 ; la ligne 378 clignote en orange]
[TEXTE À L'ÉCRAN: "6 257 − (2 832 + 3 047) = 378 millions non expliqués"]
[SFX: glitch]
[MUSIQUE: tension légère]
Mais l'arithmétique ne tombe pas juste, et je te dois cette honnêteté. 2 milliards 832 millions gelés, plus 3 milliards 47 millions chez l'attaquant : 5 milliards 879 millions. Il manque 378 millions par rapport au total de 6 milliards 257 millions. Ces 378 millions peuvent être des fonds échangés, dispersés, comptés à des moments différents, ou simplement une différence de méthode. Nous ne le savons pas, et nous préférons te le dire plutôt que d'arrondir.

#### B107 · Ce qui n'a presque pas bougé
[VISUEL: ligne "Bitcoin : réparti sur 30 adresses · aucun mouvement" ; "XRP : immobile" ; "ETH : < 2 sortis"]
[TEXTE À L'ÉCRAN: "BTC : 30 adresses neuves · rien bougé · XRP : immobile · ETH : < 2 ETH sortis"]
[SFX: aucun]
[MUSIQUE: stable]
Fait remarquable : presque tout est encore là. Le Bitcoin est réparti sur une trentaine d'adresses neuves, et pas un satoshi n'a bougé. Le XRP n'a pas bougé non plus. Du côté d'Ethereum, moins de 2 Ether sont sortis des adresses de l'attaquant. Les mouvements notables : vendredi midi, environ quinze heures après le vol, l'AVAX resté sur Avalanche est échangé en USDC puis converti en Ether, environ 16 millions de dollars. L'USDC n'est resté sur aucune adresse plus de deux minutes environ ; Circle a placé ces adresses sur liste noire 45 minutes plus tard, elles étaient déjà vides. Sur Tron, des TRX sortent au compte-gouttes : environ 97 millions de TRX, par adresses neuves.

#### B108 · La réponse de Binance
[VISUEL: communiqué simulé ; trois puces : dépôts actifs / retraits par étapes / pertes couvertes par le fonds d'urgence et l'entreprise]
[TEXTE À L'ÉCRAN: "Binance : dépôts actifs · retraits par étapes · pertes couvertes"]
[SFX: notification]
[MUSIQUE: stable]
Et les fonds des utilisateurs ? Selon la dernière mise à jour de Binance, les dépôts fonctionnent, les retraits reprendront par étapes, et les pertes seront couvertes par le fonds d'urgence de la plateforme et par les fonds de l'entreprise. Si ta question est « mon argent est-il en sécurité », la réponse officielle est oui. Cette phrase, c'est celle de Binance. Ce que je vois dans les relevés, c'est que 3 milliards 47 millions de dollars restent en mouvement, et que la clôture du dossier n'est pas écrite.

#### B109 · La phrase-thèse
[VISUEL: écran noir ; une seule ligne apparaît lentement, en monospace cyan]
[TEXTE À L'ÉCRAN: "La signature EST l'identité."]
[SFX: silence]
[MUSIQUE: résolution, très basse]
Dans un monde où la signature est l'identité, ce n'est pas la clé qui a été volée cette nuit-là. C'est la machine qui la tenait qui a oublié de demander à qui elle parlait. Des années d'efforts à protéger des clés, et cette nuit-là, la clé n'a été ni le problème ni la protection : la machine qui la portait ne reconnaît que des signatures, jamais des visages.
[PAUSE: 2s]

#### B110 · Outro
[VISUEL: carte "Affaire Bitget" en bas à droite ; un lien dans la description ; générique sobre]
[TEXTE À L'ÉCRAN: "Dossier précédent : l'affaire Bitget · Je suis L'Inspecteur."]
[SFX: tampon final]
[MUSIQUE: thème de fin, extinction lente]
Si tu veux voir comment ce schéma a commencé, retrouve l'affaire Bitget, le lien est en description : là-bas, 388 millions de dollars, et un avertissement qui n'a pas été entendu. Je suis L'Inspecteur. Ce dossier n'est pas encore fermé. À la semaine prochaine pour une nouvelle affaire.
[PAUSE: 3s]
