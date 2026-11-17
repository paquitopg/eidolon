# Données

## 1. Ressources fournies par les organisateurs

### VIGINUM : le cœur du projet

| Ressource | Contenu | Usage dans eidolon |
|---|---|---|
| [GitHub VIGINUM-FR / Rapports-Techniques](https://github.com/VIGINUM-FR/Rapports-Techniques) | Voir le détail ci-dessous | **Vérité terrain** pour l'évaluation |
| [GitHub VIGINUM-FR / D3lta](https://github.com/VIGINUM-FR/D3lta) | Détection de duplication textuelle : copier-coller, reformulation, traduction. Python, CPU, licence MIT | Indice « contenu reformulé » (étage 1) et copier-coller entre comptes (étage 2) |
| [GitHub VIGINUM-FR / DISARM-FR](https://github.com/VIGINUM-FR/DISARM-FR) | Traduction française du référentiel DISARM | Étiquetage des techniques dans l'export |
| [GitHub VIGINUM-FR / Doctrine-OpenCTI](https://github.com/VIGINUM-FR/Doctrine-OpenCTI) | Doctrine de capitalisation des menaces informationnelles dans OpenCTI (PDF FR/EN) | Format de sortie STIX 2.1 |
| [Rapport municipales 2026](https://www.sgdsn.gouv.fr/viginum/publications/protection-du-debat-public-contre-les-ingerences-numeriques-etrangeres-durant) | Bilan des 4 INE, faux sites de presse locale, Vigiscore | Cadrage du cas d'usage |
| [Ressources de sensibilisation](https://www.sgdsn.gouv.fr/viginum/academie-de-la-lmi/sensibilisation) | Guides, lexique de la menace | Vocabulaire, pitch |
| [Stratégie nationale LMI 2026-2030](https://www.sgdsn.gouv.fr/publications/strategie-nationale-de-lutte-contre-les-manipulations-de-linformation-2026-2030) | Orientations de l'État | Alignement du pitch |
| [Rapport DITP](https://www.modernisation.gouv.fr/publications/lutter-efficacement-contre-les-manipulations-de-linformation) | État de la recherche sur la désinformation | Pitch |

**Détail de `Rapports-Techniques`** (inventaire au 17/11/2026, reproductible avec `scripts/inventaire_donnees_viginum.py`) :

| Dossier | Fichiers exploitables | Contenu |
|---|---|---|
| `202306 - RRN` | `NDD_RRN.csv` + bundle STIX 2.1 | **637 domaines** avec date de création (2022 : 352 ; 2023 : 96 ; 2024 : 153 ; 2025 : 36). STIX : 352 domaines, 23 comptes (surtout Facebook), 36 techniques DISARM |
| `202402 - Portal Kombat` | CSV des domaines + bundle STIX | **371 entrées** (231 domaines, 140 sous-domaines) avec date de création et de première détection. STIX : 534 « channels », dont ~300 comptes X, 27 chaînes Telegram, 5 VK ; 21 techniques DISARM |
| `202406 - Matriochka` | Bundle STIX | 16 comptes X, 52 techniques DISARM (dont T0099.004 *Impersonate Existing Media Outlet*) |
| `202412 - BIG` | Bundle STIX | Groupe de 423 comptes X (non détaillés), 5 techniques DISARM |

Remarque : les intitulés DISARM diffèrent légèrement d'un bundle à l'autre (versions successives du référentiel, par exemple T0099). Il faudra normaliser sur la version de DISARM-FR.

### Arcep, DINUM, Arcom : secondaires pour ce challenge

Ce sont essentiellement des enquêtes (« Les Français et les fausses informations », « Les Français et l'information ») et des données sur les réseaux de télécommunication (couverture, fibre, IPv6…). **Pas utiles pour la détection.** Usage possible : une diapositive pour justifier le choix des plateformes surveillées (quels publics s'informent où).

Liste complète fournie : Ma connexion internet, Baromètre du numérique, Haut et très haut débit fixe, Mon Réseau Mobile, Ressources en numérotation, Observatoire des communications électroniques, Identifiants de communications électroniques, Qualité des réseaux fibre, Sites indisponibles, Base de population, Observatoire du courrier et du colis, Statistiques IPv6, Numérique soutenable, Expérimentations 5G, J'alerte l'Arcep (Arcep) ; mésinformation climatique dans l'audiovisuel 2025, Les Français et les fausses informations, Les Français et l'information (DINUM) ; études et bilans LMI 2026, bilans post-électoraux municipales 2026 et 2024, base des rapports DSA (Arcom).

### CNIL : le cadre de conformité

Cahier IP n°7 « Civic tech, données et Demos », dossiers LINC (IA et vote, renseignement en sources ouvertes), **délibération sur VIGINUM** (n° 2025-108), événement air 2026. Voir [conformite-cnil.md](conformite-cnil.md).

## 2. Sources externes envisagées

| Source | Usage | Accès | Points de vigilance |
|---|---|---|---|
| **Certificate Transparency** (journaux publics de certificats TLS) | Flux des nouveaux domaines (étage 1) | Historique : [crt.sh](https://crt.sh) ; temps réel : certstream | crt.sh lent → requêtes historiques **à faire avant** le hackathon ; fiabilité du serveur certstream public à tester, prévoir un serveur auto-hébergé |
| **Données ouvertes Afnic** (.fr) | Nouveaux domaines `.fr` | À vérifier : existence, fréquence, contenu | Pertinent pour les faux médias locaux |
| **Flux RSS de la presse nationale et régionale** | Corpus de référence pour D3lta (contenu reformulé) | Public | Constituer la liste en amont |
| **Liste de référence des médias et institutions** | Base de comparaison des noms de domaine | À constituer (médias nationaux, presse régionale, `gouv.fr`) | Travail de préparation clé |
| **Telegram** (chaînes publiques) | Étage 2 | Bibliothèque Telethon, identifiants d'API via my.telegram.org | Créer les identifiants en amont |
| **Bluesky** (Jetstream / firehose) | Étage 2, démo en direct | Ouvert, gratuit, temps réel | Peu de campagnes y sont documentées |
| X, Facebook | — | API X très chère ; Meta réservé aux chercheurs agréés (DSA art. 40) | **Hors périmètre**, à assumer à l'oral |
| [EUvsDisinfo](https://euvsdisinfo.eu/disinformation-cases/) | Narratifs de référence (bonus) | Public | — |
