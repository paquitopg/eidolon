# Questions ouvertes

## À obtenir des organisateurs
- [ ] Composition du jury et critères d'évaluation
- [ ] Format du rendu (dépôt public obligatoire ? licence imposée ? durée du pitch ?)
- [ ] Ressources de calcul sur place (GPU ?) et accès réseau (restrictions ?)
- [ ] Possibilité d'échanger avec VIGINUM pendant le hackathon

## À trancher dans l'équipe
- [ ] Composition de l'équipe et répartition (voir [plan.md](plan.md))
- [ ] Périmètre de l'étage 2 : module complet ou bonus (dépend de la taille de l'équipe)
- [ ] Ce que fait exactement **Vigiscore**, et comment s'en démarquer
- [ ] Interface : Streamlit ou FastAPI + front
- [ ] Modèle de vision et de langage retenu (taille compatible avec le matériel disponible)
- [ ] Licence du dépôt (open source : MIT comme D3lta ? EUPL ?)
- [ ] Visibilité du dépôt : **public tant qu'il ne contient que la documentation** (pour GitHub Pages), à repasser en privé au début du développement. Sur un compte gratuit, le site GitHub Pages sera alors dépublié

## À vérifier techniquement
- [ ] Les données ouvertes de l'Afnic permettent-elles de suivre les nouveaux `.fr` ?
- [ ] Fiabilité du serveur certstream public
- [ ] Proportion des domaines RRN qui ont émis un certificat TLS (sinon, l'étage 1 ne les verrait pas par ce canal)
- [ ] Import effectif des objets STIX produits dans OpenCTI (le README RRN indique OpenCTI 5.9.6 pour l'import de ses bundles)
