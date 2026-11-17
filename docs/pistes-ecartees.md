# Pistes étudiées

Toutes les idées envisagées pendant le cadrage, avec la décision prise et sa raison.

| Piste | Décision | Raison |
|---|---|---|
| **Sentinelle des faux médias** (domaines imitant des médias, alerte précoce) | ✅ **Retenue : cœur du projet** | Répond à « détecter tôt » et au volet cyber ; données de référence VIGINUM (RRN, Portal Kombat) ; cas réel des municipales 2026 ; quasiment pas de données personnelles |
| **Score de coordination inauthentique** (co-partage, copier-coller, comptes en rafale) | ✅ **Retenue : deuxième étage** | Répond à « modéliser la propagation » ; s'intègre naturellement en aval de la sentinelle. Limite : accès aux données (Telegram et Bluesky uniquement) |
| **Détection des fausses vidéos aux couleurs de vrais médias** (type Matriochka / Storm-1516) : logo, texte incrusté, vérification dans les archives du média | ⏸️ Reportée | Bonne idée, centrée sur la provenance plutôt que sur la détection de deepfake. Peut devenir un indice supplémentaire si le temps le permet |
| **Suivi des narratifs** (diffusion > répétition > amplification > légitimation, traduction russe → français) | ⏸️ Bonus | Mode traduction de D3lta sur les sites Portal Kombat ; volet « légitimation » difficile à mesurer en 3 jours |
| **Assistant d'analyse DISARM** (fiche rédigée par un modèle de langage) | ⏸️ Bonus | Faible risque technique, forte valeur en démo ; dernière brique de la chaîne. Évaluation limitée (4 bundles STIX) |
| **Test des chatbots contre les narratifs du réseau Pravda** (contamination des modèles de langage) | ⏸️ Idée de prolongement | Sujet d'actualité ; hors du cœur du challenge 1 |
| **Détecteur de deepfakes audio/vidéo pur** | ❌ Écartée | Les détecteurs généralisent mal ; impossible de dépasser l'état de l'art en 3 jours ; aucune donnée fournie ; les empreintes vocales de candidats seraient des données biométriques |
| **Coordination sur X et Facebook** | ❌ Hors périmètre | API X très coûteuse ; accès Meta réservé aux chercheurs agréés (DSA art. 40). À assumer explicitement à l'oral |
| **Exploitation des données Arcep / DINUM / Arcom** | ❌ Pas pour la détection | Enquêtes et données réseau ; au mieux une diapositive pour justifier le choix des plateformes |
| **« Détecteur de fake news »** (classer des contenus vrai / faux) | ❌ Écartée | Hors mandat VIGINUM (qui caractérise des comportements et l'origine) ; politiquement risqué avant la présidentielle 2027 |
