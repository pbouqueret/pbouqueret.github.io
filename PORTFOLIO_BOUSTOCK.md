# Application de gestion de stock - Système de gestion d'inventaire et de flux de stock

## État d'avancement
**Preuve de Concept (PoC) fonctionnelle.**
L'application est opérationnelle en local avec persistance des données.

## TL;DR
Application web mobile-first permettant aux artisans bouchers de gérer leur stock en temps réel et de générer instantanément des commandes fournisseurs par SMS/presse-papier.

## Fonctionnalités Opérationnelles
- **Gestion des stocks** : Ajout/Retrait rapide avec calcul automatique des seuils d'alerte.
- **Tableau de Bord** : Indicateurs visuels pour les ruptures de stock et les DLC courtes.
- **Recherche Avancée** : Moteur de recherche floue (Fuzzy Search) pour trouver rapidement les produits.
- **Génération de Commande** : Création automatique de listes de courses basées sur les stocks bas et ruptures.
- **Mode "Appel"** : Interface dédiée pour le pointage des produits lors des commandes téléphoniques.
- **Persistance** : Sauvegarde locale des données (LocalStorage) pour une continuité de service sans backend.

## Architecture & Ingénierie
> - **Stack** : React 19, Vite, TailwindCSS, Fuse.js

### Gestion d'État (State Management)
L'application utilise les **Hooks React natifs (`useState`, `useReducer`, `useMemo`)** pour la gestion d'état local. La cohérence des données est assurée par une synchronisation systématique avec le `localStorage` via des effets de bord (`useEffect`), garantissant la persistance entre les sessions.

### Structure du code
Le projet suit une structure simple adaptée au prototypage rapide :
- **Modularité** : Séparation claire entre la logique (Hooks), les données statiques (`products.json`) et l'interface (`App.jsx`).
- **Composants** : Utilisation de composants fonctionnels et de TailwindCSS pour le styling atomique.
- **Logique Métier** : Centralisation des règles métier (calcul des DLC, seuils) dans des fonctions utilitaires au sein du composant principal.

### Qualité
- **UX Mobile** : Interface tactile avec zones de clic larges et retours visuels immédiats.
- **Performance** : Optimisation des rendus et des recherches via `useMemo` et `Fuse.js`.
- **Résilience** : Gestion des cas d'erreur lors du chargement des données.

## Perspectives d'évolution
- **Backend Dédié** : Implémentation d'une base de données réelle (PostgreSQL/Supabase) pour la synchronisation multi-postes.
- **Authentification** : Ajout d'une couche de sécurité pour gérer plusieurs utilisateurs/boutiques.
- **Typage Strict** : Migration progressive vers TypeScript pour renforcer la fiabilité du code.
