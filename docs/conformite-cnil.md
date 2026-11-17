# Conformité et éthique

Les ressources fournies par la CNIL indiquent que la protection des données et des libertés sera regardée. Cette page fait le lien entre la **délibération CNIL n° 2025-108 du 6 novembre 2025** (avis sur le projet de décret consolidant les missions de VIGINUM) et les choix d'eidolon. Elle doit servir de base à une diapositive du pitch.

Texte : https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053459708

## Ce que dit la délibération (résumé)

- VIGINUM collecte et analyse de façon automatisée des contenus **publiquement accessibles** et les comptes qui les diffusent.
- La minimisation des données s'applique **tout au long du traitement**, y compris pour la réutilisation des données afin d'entraîner des outils d'IA.
- Les outils automatisés doivent **filtrer la collecte selon des critères précis**, et leur usage doit être couvert par une analyse de risques.
- Les modèles destinés à être publiés doivent d'abord être **testés contre l'extraction de données personnelles et contre les biais**.
- Durées de conservation encadrées : les données collectées sont conservées un an au maximum.
- Le comité d'éthique et scientifique (CES) reçoit **chaque semaine les journaux de collecte**.

## Comment eidolon s'y conforme

| Exigence | Mise en œuvre dans eidolon |
|---|---|
| Collecte filtrée par critères précis | Étage 1 : domaines et sites web, quasiment aucune donnée personnelle. Étage 2 : collecte **déclenchée uniquement** par un domaine signalé, limitée aux publications qui contiennent ses URL |
| Minimisation | On conserve uniquement ce qui sert aux indices : identifiant, horodatage, URL, texte. Pas de photo de profil, pas de liste d'abonnés |
| Pseudonymisation | Identifiants de comptes hachés (avec sel) dans l'interface et les exports de démonstration ; la réidentification reste réservée à l'analyste habilité |
| Journal des collectes | Chaque collecte est tracée (déclencheur, période, plateforme, volume), dans un format exportable pour un contrôle de type CES |
| Conservation | Durée paramétrable, purge automatique |
| Entraînement de modèles | Le score de la sentinelle est entraîné sur des **domaines**, pas sur des données personnelles |
| Pas de décision automatique | Le score est une aide à l'analyste ; aucune action (signalement, retrait) n'est déclenchée automatiquement |

## Neutralité

- eidolon **ne juge pas la véracité des contenus** ni les opinions exprimées : il caractérise l'**usurpation d'identité** (faux médias) et la **diffusion artificielle** (coordination).
- Pas de profilage de citoyens : les opinions politiques sont des données sensibles (RGPD, article 9).
- Les seuils et la liste de référence des médias doivent être **documentés et publics**, pour éviter tout soupçon de ciblage politique, a fortiori avant la présidentielle 2027.

## Sécurité opérationnelle

- Les sites suspects sont visités dans un environnement isolé (conteneur jetable, sans identifiants).
- Aucune interaction avec les comptes observés (ni abonnement, ni réponse).
