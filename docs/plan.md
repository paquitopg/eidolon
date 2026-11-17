# Plan de travail

Principe : **tout ce qui est lent, risqué ou dépendant d'un accès externe se fait avant le hackathon.** Sur place, on assemble, on fiabilise la démo et on soigne le pitch.

## Avant le hackathon

### Données
- [ ] Lire le rapport VIGINUM sur les municipales 2026, en particulier la partie **Vigiscore**, pour ajuster le périmètre
- [ ] Constituer la **liste de référence** des médias (nationaux, presse régionale et locale) et des institutions (`gouv.fr`) : nom, domaine, logo
- [ ] Archiver les **flux RSS** de ces médias (corpus D3lta)
- [ ] Construire le **jeu de test historique** : domaines RRN et Portal Kombat + date d'émission de leur premier certificat (crt.sh, requêtes lentes) + dates de création et de première détection
- [ ] Constituer un échantillon de **domaines négatifs** tirés du flux de certificats
- [ ] Vérifier l'existence et le contenu des **données ouvertes Afnic** sur le `.fr`
- [ ] Créer les **identifiants d'API Telegram** et tester la collecte sur les 27 chaînes Portal Kombat
- [ ] Tester le **flux certstream** (serveur public) et préparer un plan B auto-hébergé

### Code
- [ ] Indice 1 (ressemblance du nom) + **premier chiffre de détection sur RRN**
- [ ] Encapsuler D3lta pour l'indice 3
- [ ] Export STIX 2.1 et test d'import dans une instance OpenCTI locale
- [ ] Premier graphe de co-partage hors ligne (étage 2)
- [ ] Squelette d'interface et Docker Compose

## Sur place (3 jours)

| Jour | Objectif |
|---|---|
| **J1** | Brancher les indices 1 à 4 de la sentinelle, score V0, fiches par domaine |
| **J2** | Brancher l'étage 2 sur la sortie de la sentinelle, graphe interactif, export STIX bout en bout ; démo en direct sur le flux du jour |
| **J3** | Fiabiliser la démo (rediffusion historique garantie + direct en bonus), chiffres d'évaluation, diapositives (dont conformité CNIL), répétition du pitch |

## Répartition indicative

À adapter quand l'équipe sera connue :

- **Sentinelle** : flux de domaines, ressemblance des noms, infrastructure, évaluation RRN
- **Contenu et vision** : D3lta, corpus RSS, captures et modèle de vision
- **Coordination** : collecte Telegram et Bluesky, graphe, score (au moins une personne dédiée dès la préparation ; sinon, garder ce module en bonus avec seulement la version historique)
- **Produit et pitch** : interface, export STIX / OpenCTI, conformité, diapositives

## Démo cible (5 minutes)

1. Un domaine apparaît dans le flux de certificats → la sentinelle le signale, fiche avec capture et contenu reformulé mis en regard de l'original.
2. Le module de coordination montre les comptes qui partagent ses liens et leur synchronisation.
3. Export STIX → import dans OpenCTI.
4. Chiffre clé : « sur les domaines RRN, X % auraient été repérés, en moyenne N jours avant leur signalement. »
