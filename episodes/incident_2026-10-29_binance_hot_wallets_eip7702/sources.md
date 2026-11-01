# Sources · INCIDENT LOG · Binance, 29 octobre 2026

Légende de confiance : **C** = recoupé par plusieurs sources indépendantes · **R** = une source ou un relevé relayé, non revérifié par nous · **A** = attribution d'un cabinet (avis, pas preuve).

## 1. Ce que nous avons vraiment fait, et ce que nous n'avons pas fait

- Nous avons recoupé des **articles, rapports d'analyse et relevés on-chain publiés** (liste ci-dessous) avec un transcript détaillé de l'enquête. Quand deux sources divergent, le script donne les deux chiffres.
- Nous n'avons **pas refait le traçage on-chain nous-mêmes** (pas d'accès à un explorateur depuis l'environnement de production). Les hash de transaction ne sont donc **pas inclus** : chaque montant supérieur à 10 M$ porte dans `script.md` une ligne `[RÉF. ON-CHAIN: … hash à renseigner, S-xx]`. Avant publication, remplir chaque `S-xx` depuis l'explorateur indiqué (colonne « où chercher »). Aucun hash n'a été inventé.
- L'événement est vieux de trois jours au moment de l'écriture : les chiffres, le récit officiel et les attributions peuvent encore bouger.

## 2. Sources publiques (niveau article / rapport)

| Réf. | Source | Contenu utilisé | Conf. |
|---|---|---|---|
| P-01 | [Wikipedia, 2026 Binance hack](https://en.wikipedia.org/wiki/2026_Binance_hack) | Cadre général, chronologie, ordres de grandeur | C |
| P-02 | [Bitquery, Binance Hack: $6.3B Drained on 9 Chains, $2.7B Frozen](https://www.bitquery.io/investigations/binance-hack) | 6,3 Md$ sur neuf chaînes ; ≈ 2,7 Md$ gelés ; analyse on-chain | C |
| P-03 | [Hackenproof, Binance Hack 2026: Inside the $6.3B Breach](https://hackenproof.com/blog/binance-hack) | Analyse de l'attaque et du flux | C |
| P-04 | [Crystal Intelligence, Binance hack: what we know](https://crystalintelligence.com/investigations/binance-hack-what-we-know-what-teams-should-do-now/) | Éléments d'enquête, réponse | C |
| P-05 | [Threat Landscape, Binance Hot Wallet Compromise: EIP-7702 Analysis](https://threatlandscape.io/blog/binance-hot-wallet-compromise-eip-7702-delegation) | Mécanisme EIP-7702, délégation | C |
| P-06 | [crypto.news, How one wallet trick led to a $6.3 billion breach](https://crypto.news/binance-hack-eip-7702-wallet-attack/) | Explication de la ruse, 50 autorisations (Blockaid, 20:20:59 UTC) | C |
| P-07 | [CryptoTicker, $2.8B drained from hot wallet via EIP-7702](https://cryptoticker.io/en/binance-hack-hot-wallet-drained/) | Premier chiffre ≈ 2,8 Md$ sur un portefeuille | R |
| P-08 | [Cryptonews, Around $2.8B drained from a hot wallet](https://cryptonews.net/news/security/33673751/) | Premières estimations | R |
| P-09 | [BeInCrypto, Is Binance being hacked?](https://beincrypto.com/is-binance-being-hacked-customer-funds/) | Premières réactions, sorties de fonds | R |
| P-10 | [Bitrue, Tether freezes $1.5B USDT linked to suspected Binance hack](https://www.bitrue.com/blog/tether-freezes-1-5b-usdt-binance-hack-bnb) | Gel Tether > 1,5 Md$ ; BNB −9 % | R |
| P-11 | Communiqués de Binance et déclarations de Richard Teng, Yi He, CZ (30 oct.) | Version officielle (ordinateur portable d'un ingénieur DevOps, conteneur de service, aucune fuite de clé) | R |
| P-12 | TRM Labs ; Chainalysis (via Forbes) ; ZachXBT | Attribution à TraderTraitor (lien avec la Corée du Nord) ; liens de flux avec l'affaire Bitget via THORChain | **A** |
| P-13 | Reprise de rapport de Blockaid sur Bybit (2025) | Parenté de mode opératoire avec Bybit | R |

## 3. Références on-chain à renseigner (une par montant > 10 M$)

Format d'un hash à ajouter dans le script : `[RÉF. ON-CHAIN: <description> — 0x…hash…]`. Heures du tableau en UTC+3 ; l'explorateur affiche l'UTC (retire 3 h).

| Réf. | Événement (UTC+3) | Montant | Où chercher |
|---|---|---|---|
| S-03 | Préparation : Tornado Cash 0,1 ETH, contrats de test, contrat final (28–29 oct.) | — | Etherscan : historique de l'adresse de l'attaquant (Etherscan : « Binance Hot Wallet Exploiter #2 » pour l'Adresse 1) |
| S-04 | 00:42:59 → 00:44:11, 200 M USDT entrants puis sortants | 200 M USDT | Etherscan : transferts USDT de Binance 14 |
| S-05 | ≈ 23:24, appel « sweep » sur Binance 14, 64 transferts | ≈ 2,529 Md$ | Etherscan : transaction de balayage (call interne) |
| S-06 | 23:04:52 échec ; 23:05:00 activation 185 M XRP ; 5 comptes → 297 M$ | 42,75 M$ ; 297 M$ | XRPScan / XRP Ledger Explorer |
| S-07 | 23:18 Optimism (5 M$) ; ≈ 23:20 Bitcoin, 11 transactions dans un bloc, > 18 000 BTC | 1,467 Md$ | Mempool.space (blocs), Optimistic Etherscan |
| S-08 | 23:19 recharge ≈ 7 000 ETH ; 02:55:47 recharge 3 000 ETH ; 02:56:47 dernier balayage | 16 M$ ; 6,8 M$ | Etherscan : adresse de recharge (> 256 000 tx) |
| S-09 | 23:20:59 transaction type 4 (EIP-7702), 50 autorisations, valeur 0 | — | Etherscan : transaction « Type 4 » vers Binance 14 (Blockaid : 20:20:59 UTC) |
| S-10 | 23:21–23:23 Tron : ≈ 612 M$ USDT ; 00:09:12 gel Tether | 612 M$ | Tronscan |
| S-11 | 23:24:47, Binance 16 → Adresse 1, 9 transactions | ≈ 174 M$ | Etherscan : Binance 16 |
| S-12 | 23:30 Arbitrum ; 23:33:00 Avalanche ; 02:04:30 Avalanche ; ≈ 02:06 Polygon | ≈ 32 M$ ; … | Arbiscan, Snowtrace, Polygonscan |
| S-13 | 23:38, 195 000 ETH hors de l'Adresse 1 | — | Etherscan |
| S-14 | 23:41, 780 M USDC vers l'Adresse 1 | 780 M$ | Etherscan |
| S-15 | 23:34 → 23:49 échanges 325 M USDT ; 23:52:59 190 M USDT | 325 M$ ; 190 M$ | Etherscan, Uniswap |
| S-16 | 23:57:47 gel WLFI ; 23:57:59 dépôts Aave 10 M$ puis 50 M$ ; emprunts 3 271 puis 16 490 ETH | 60 M$ | Etherscan, Aave |
| S-17 | 00:01:35 liste noire Tether (971 M$) ; 00:01:59 / 00:02:47 ; 00:04:59 Circle 823 M$ ; 01:06:23 Binance 14 | 971 M$ ; 823 M$ | Etherscan : événements « AddedBlackList » (USDT), blacklist (USDC) |
| S-18 | 00:11 / 00:14 / 00:18:59 gels ; 00:22 RLUSD 88,5 M ; 01:59 Ripple 40,5 M | 50 M$ ; 175 M$ ; 30 M$ ; 88,5 M$ ; 40,5 M$ | Etherscan : tx de gel, ordre dans le bloc |
| S-19 | Communiqués, prises de parole, gel du WBETH (01:48, ≈ 74 M$), bilan 03:52 | 74 M$ ; ≈ 3 Md$ | Canaux officiels de Binance, X |
| S-20 | 03:18, Security Council Arbitrum, > 8 000 ETH | ≈ 18 M$+ | Arbiscan : transactions système |
| S-21 | 01:39 redirection ; 01:55:35 → 03:07:11 : 47 transactions de sauvetage | — | Etherscan : Binance 14, nonces suivants |
| S-22 | 03:10:35, transaction de révocation (type 4, adresse zéro) | — | Etherscan |
| S-23 | Décompte huit réseaux : 6 257 M$ | 6 257 M$ | assets/timeline.json (sommes) |

## 4. À vérifier avant publication (liste de contrôle)

1. **Hash** : renseigner S-03 à S-23 depuis un explorateur ; corriger toute heure ou tout montant divergent.
2. **Total et sous-totaux** : 6 257 M$ (décompte huit réseaux) contre ≈ 6,3 Md$ (Binance) ; gelé 2 832 M$ (mesure reprise) contre 2,4 à 3 Md$ ; chez l'attaquant 3 047 M$. L'écart de **378 M$** (6 257 − 2 832 − 3 047) est **non expliqué** : le script le dit.
3. **Récit officiel** : la version de Binance a évolué (composant logiciel, ordinateur portable ; une reprise de presse attribue à Richard Teng une phrase mélangeant EIP-7702 et « multi-signature »). Relire le communiqué original avant d'attribuer une citation.
4. **Paraphrases** : la réaction de CZ (00:15) est une paraphrase d'un transcript, pas une citation. Retrouver le texte exact.
5. **Détails seulement relayés** : « signatures demandées ≈ 3 min avant l'exécution », « 50 autorisations, une seule au bon nonce (…809) », « position 7 contre 328 dans le bloc » (Ripple), « 72 s d'âge du compte Tron », « 195 000 ETH », « 780 M USDC », « 130 M / 48 s », « 321 transactions d'écart ».
6. **Attributions** (TRM, Chainalysis, ZachXBT) : avis, pas preuves ; aucune attribution gouvernementale officielle au moment de l'écriture.
7. **Affaire Bitget (388 M$, il y a 5 semaines) et Bybit (≈ 1,5 Md$, févr. 2025)** : relire les épisodes précédents de la chaîne pour caler les chiffres et le lien de description.
8. **Passages non utilisés** car non vérifiés : « Black October » et failles PHP, vente de 7,77 trillions de PEPE, certaines hypothèses de synthèses secondaires.
