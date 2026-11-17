# Architecture

Deux étages : la sentinelle (cœur du projet) et le module de coordination (deuxième étage, déclenché par la sentinelle). Chaque étage produit un **score expliqué indice par indice** et des **objets STIX 2.1**.

## Étage 1 : la sentinelle des faux médias

### Entrées

- **Nouveaux domaines** : journaux Certificate Transparency (temps réel + historique), éventuellement données ouvertes Afnic pour le `.fr`.
- **Liste de référence** des médias et institutions français : médias nationaux, presse régionale et locale, domaines `gouv.fr`, avec leur nom, leur domaine et leur logo.
- **Corpus de référence** : flux RSS de ces médias, archivés en continu.

### Indices

| # | Indice | Méthode | Technique DISARM associée |
|---|---|---|---|
| 1 | **Ressemblance du nom** | Distance d'édition, homoglyphes, changement d'extension (`.ltd`, `.pics`, `.co.com`…), ajout de lettres (`spiegelr`, `20minuts`), génération des variantes à la manière de dnstwist | T0099.004 *Impersonate Existing Media Outlet*, T0099.002 *Spoof/Parody Account/Site* |
| 2 | **Ressemblance visuelle** | Capture d'écran (navigateur sans interface), comparaison au site légitime ; modèle de vision ouvert pour détecter un logo ou une charte imités | T0099.004 |
| 3 | **Contenu reformulé** | Articles du site suspect comparés au corpus RSS avec **D3lta** (modes reformulation et traduction) : un site qui republie la presse locale en la réécrivant est un signal fort | T0084.002 *Plagiarize Content*, T0085.003 *Develop Inauthentic News Articles* |
| 4 | **Infrastructure** | Domaines créés en rafale (cf. les dates de création RRN), même hébergeur ou même bureau d'enregistrement, mêmes certificats | T0098.001 *Create Inauthentic News Sites*, T0013 *Create Inauthentic Websites* |

Le **filtrage est séquentiel** pour rester léger : l'indice 1, peu coûteux, filtre le flux ; les indices 2 à 4 ne sont calculés que pour les candidats retenus.

### Score

1. Version 0 : règles pondérées et lisibles (chaque indice contribue de façon explicite).
2. Version 1 : régression logistique calibrée, entraînée avec les domaines RRN et Portal Kombat comme positifs et des domaines tirés au hasard du flux de certificats comme négatifs. L'objectif reste l'**explicabilité** : on affiche la contribution de chaque indice.

### Sorties

- Fiche par domaine : score, indices, captures, extraits de contenu reformulé mis en regard de l'original.
- Objets STIX : `domain-name`, `url`, `indicator`, `infrastructure`, relations vers les `attack-pattern` DISARM, `x_opencti_score`.

## Étage 2 : le module de coordination

### Déclenchement

Uniquement à partir d'un **domaine signalé** par l'étage 1 (ou d'une liste fournie par l'analyste). C'est à la fois un choix d'efficacité et de conformité : pas de surveillance large des réseaux sociaux.

### Collecte

- **Telegram** : chaînes publiques (Telethon). Terrain de test : les 27 chaînes Portal Kombat du STIX de VIGINUM.
- **Bluesky** : flux Jetstream filtré sur les URL des domaines signalés.
- X et Facebook : hors périmètre (accès coûteux ou réservé aux chercheurs agréés par le DSA).

### Indices

| # | Indice | Méthode | Technique DISARM associée |
|---|---|---|---|
| 1 | **Co-partage synchronisé** | Deux comptes sont reliés s'ils partagent la même URL dans une fenêtre de quelques secondes (méthode CooRnet / *coordinated link sharing*) ; seuil de fenêtre estimé sur les données | T0049.003 *Bots Amplify via Automated Forwarding and Reposting*, T0119 *Cross-Posting* |
| 2 | **Copier-coller** | D3lta sur les textes des publications | T0084.001 *Use Copypasta* |
| 3 | **Création en rafale** | Distribution des dates de création des comptes d'un même groupe | T0090 *Create Inauthentic Accounts* |
| 4 | **Rôle dans le graphe** | Centralité et détection de communautés : super-diffuseurs, nœuds-ponts entre plateformes | — |

### Sorties

- Graphe interactif des groupes de comptes, avec score de coordination par groupe.
- Objets STIX : `user-account` / `channel`, relations `related-to` vers les domaines amplifiés.
- **Identifiants pseudonymisés dans l'interface** (voir [conformite-cnil.md](conformite-cnil.md)).

## Bonus (si le temps le permet)

- **Assistant d'analyse** : à partir des sorties des deux étages, un modèle de langage ouvert rédige une fiche d'analyse avec les techniques DISARM-FR et cite ses preuves. Évaluation possible sur les techniques des 4 bundles STIX (petit échantillon).
- **Suivi des narratifs traduits** : mode traduction de D3lta appliqué aux sites Portal Kombat (russe → français).

## Choix techniques (proposition)

| Besoin | Proposition | Remarque |
|---|---|---|
| Langage | Python | Écosystème D3lta, STIX, NLP |
| Ressemblance de noms | `rapidfuzz`, génération de variantes à la dnstwist | — |
| Captures d'écran | Playwright (Chromium sans interface) | Sandboxer les visites de sites suspects |
| Modèle de vision / langage | Modèles ouverts exécutables sur place (ex. famille Mistral) | Argument de souveraineté |
| Plongements multilingues | `sentence-transformers` (ex. `paraphrase-multilingual-mpnet-base-v2`, cité par D3lta) | — |
| Duplication | `d3lta` | Brique VIGINUM |
| Graphe | `networkx` ou `igraph` | — |
| Export | `stix2` (OASIS) | Vérifier l'import dans une instance OpenCTI de test |
| Interface | Streamlit (rapide) ou FastAPI + front léger | À trancher selon l'équipe |
| Déploiement | Docker Compose | Démo reproductible sur place |
