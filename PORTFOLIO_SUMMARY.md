# FIGHT ATLAS
> "Une interface moderne pour consulter les statistiques MMA."

## Concept & Visual
L'objectif est d'offrir une expérience utilisateur fluide et agréable pour la consultation de statistiques de combat. Le design mise sur un thème sombre avec des accents dorés et une navigation intuitive.

## Tech Stack
*   **Frontend** : React 19, Tailwind CSS
*   **Animations** : Framer Motion, GSAP
*   **Données** : JSON local, Fuse.js
*   **Outils** : Vite, Lenis (Scroll Smooth)

## Highlights Techniques

### > Data & Performance
Gestion d'une base de données locale JSON avec optimisation des tris et filtres via `useMemo`. Chargement instantané sans dépendance au réseau externe pour les requêtes.

### > Fonctionnalités Clés
*   **Comparateur** : Visualisation côte-à-côte avec calcul des différences (allonge, taille, âge) et graphiques comparatifs (striking, grappling).
*   **Indice de Danger** : Calcul algorithmique basé sur le taux de finition et l'activité.
*   **Recherche Optimisée** : Utilisation de Fuse.js pour tolérer les fautes de frappe et rechercher par critères multiples.
*   **Filtres Intelligents** : Détection automatique des "Prospects" (jeunes talents) et des séries de victoires ("Hype").

### > Qualité du Code
*   Composants modulaires et réutilisables.
*   Structure claire des props et gestion des états.
*   Séparation logique entre traitement des données et affichage.

## TL;DR
Un dashboard interactif et réactif développé avec **React et Tailwind**. Il intègre un système de **comparaison de combattants**, une **recherche floue** et une **visualisation de données claire** dans une interface soignée.
