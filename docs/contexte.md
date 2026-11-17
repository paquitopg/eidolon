# Contexte

## Le challenge

**Hackathon Artefact Adopt AI « Désinformation et souveraineté démocratique »**, organisé avec des acteurs publics (VIGINUM, Arcep, DINUM, Arcom, CNIL ont fourni des ressources). Format : 3 jours sur place, avec une réflexion et une préparation en amont. Jury et critères d'évaluation : non communiqués à ce jour.

**Challenge 1 : Détecter et caractériser des menaces informationnelles et cyber**

> How can we identify suspicious content or campaigns at an early stage, determine their origin and model their spread?

Exemples de projets donnés par les organisateurs :

- détecteur de deepfakes audio/vidéo en temps réel avec score de fiabilité ;
- modélisation des graphes de diffusion sur différents réseaux sociaux pour identifier les super-diffuseurs et nœuds clés ;
- outil NLP de caractérisation automatique des manœuvres coordonnées (schéma : diffusion > répétition > amplification > légitimation) ;
- score de « coordination inauthentique » fondé sur des signaux comportementaux communs aux plateformes.

## Le cadre institutionnel

**VIGINUM** (service de vigilance et de protection contre les ingérences numériques étrangères), rattaché au **SGDSN**, détecte et caractérise les ingérences numériques étrangères (INE). Son champ est défini par le décret n° 2021-922 du 13 juillet 2021, qui retient **quatre critères cumulatifs** :

1. une atteinte potentielle aux intérêts fondamentaux de la Nation ;
2. un contenu manifestement inexact ou trompeur ;
3. une diffusion artificielle ou automatisée, massive et délibérée ;
4. l'implication, directe ou indirecte, d'un acteur étranger.

**Conséquence pour eidolon :** l'outil doit produire des éléments utiles à l'analyste pour instruire ces critères, surtout le 3 (diffusion artificielle) et le 4 (indices d'origine). Il ne juge pas la véracité des opinions.

Textes de référence :

- **Stratégie nationale de lutte contre les manipulations de l'information 2026-2030**, présentée par le SGDSN le 11 février 2026.
- **Délibération CNIL n° 2025-108 du 6 novembre 2025** sur le projet de décret consolidant les missions de VIGINUM (voir [conformite-cnil.md](conformite-cnil.md)).
- Échéance politique : **élection présidentielle 2027**. Tout outil doit être irréprochable sur la neutralité.

## La menace observée

### Campagnes documentées par VIGINUM (rapports techniques publics)

| Campagne | Mode opératoire principal | Intérêt pour eidolon |
|---|---|---|
| **RRN / Doppelgänger** (2022→) | Typosquatting de médias et sites gouvernementaux européens, faux médias francophones, réseaux de comptes Facebook/X | Cas d'école de l'étage 1 ; 637 domaines publiés avec date de création |
| **Portal Kombat** (2024) | Réseau de sites « Pravda » qui republient en masse des contenus pro-russes, relais Telegram et X | Liste de 371 domaines ; ~300 comptes X et 27 chaînes Telegram dans le STIX |
| **Matriochka** (2024) | Faux contenus usurpant des médias, sollicitation des fact-checkers | Usurpation de médias (DISARM T0099.004) |
| **BIG** (2024) | Campagne visant l'outre-mer et la Corse, hashtags détournés, copier-coller | Coordination de 423 comptes X |

### Municipales des 15 et 22 mars 2026

D'après le rapport public de VIGINUM (juin 2026) et sa couverture presse :

- **4 ingérences numériques étrangères** ont visé spécifiquement le scrutin ; leur portée est jugée très limitée ;
- dont une campagne de **plus de 100 domaines en `.fr` imitant des sites de presse locale**, remplis d'**articles reformulés par IA générative** ; l'Afnic a suspendu la plupart des domaines après vérification de l'identité des titulaires → **c'est exactement le cas d'usage de l'étage 1** ;
- poursuite de l'activité de **Storm-1516** (faux reportages usurpant des médias) ;
- VIGINUM relève l'essor d'une **« économie de l'ingérence »** (prestataires qui vendent des services d'intermédiation, ingérences motivées par le profit) et une **clandestinisation** croissante des opérations ;
- le rapport mentionne un outil **« Vigiscore »**. **À lire avant de figer le périmètre**, pour ne pas reproduire un outil existant.

Lien : https://www.sgdsn.gouv.fr/viginum/publications/protection-du-debat-public-contre-les-ingerences-numeriques-etrangeres-durant (protégé contre la lecture automatique, à ouvrir dans un navigateur).
