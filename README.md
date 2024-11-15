# Sklum Product Scraping Project

Ce projet consiste à extraire des informations de produits, y compris les avis et les notes, du site Sklum. L'objectif est de récupérer les données de produits pour une analyse et une utilisation ultérieure dans des projets de data science ou d'analyse de marché.

## Table des matières
- [Aperçu du projet](#aperçu-du-projet)
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure des fichiers](#structure-des-fichiers)
- [Exemples de données](#exemples-de-données)
- [Auteurs](#auteurs)

## Aperçu du projet

Le projet utilise Python, avec les bibliothèques `requests` pour l'envoi de requêtes HTTP et `BeautifulSoup` pour l'analyse HTML, afin de collecter les informations suivantes :
- Nom du produit
- Prix
- Note moyenne
- Nombre d'avis
- Texte des avis des utilisateurs

Les données extraites sont stockées dans des fichiers JSON pour une analyse ultérieure.

## Fonctionnalités

- Extraction des liens de produits depuis une page source.
- Récupération des détails pour chaque produit, y compris les avis et notes des utilisateurs.
- Filtrage et stockage des données dans un fichier JSON.
- Suppression des doublons pour garantir des données uniques.

## Installation

1. Clonez le dépôt GitHub :

   ```bash
   git clone https://github.com/bolyderiz/sklum_scrapping.git
   cd sklum_scrapping

2. Installez les dependecies requises :
    pip install requests beautifulsoup4

## Utilisation

1. Exécutez le script principal main_final.py pour extraire les informations produits et les avis :

2. Les avis et informations des produits seront sauvegardés dans le fichier product_reviews.json une fois l'extraction terminée.


## Structure des fichiers
all_product_links.txt : Contient tous les liens des produits extraits.
fetch_reviews_ratings.py : Script pour récupérer les avis et les notes des produits.
main_final.py : Script principal pour exécuter l'extraction complète.
merged_products_reviews.json : Fichier JSON fusionné contenant les informations de produits et les avis.
README.md : Documentation du projet.
.gitignore : Exclut les fichiers générés et non nécessaires au dépôt (fichiers JSON, HTML, Excel).


## Exemples de données
Voici un exemple de structure des données extraites, stockées dans product_reviews.json :

[
    {
        "url": "https://www.sklum.com/fr/acheter-chaises-salle-a-manger/152433-chaise...",
        "rating": "4.8",
        "reviews": [
            "Belle table. Grande et de bonne qualité.",
            "Très satisfaite, facile à monter."
        ]
    },
    ...
]

## Auteurs
bolyderiz - GitHub Profile
N'hésitez pas à contribuer, poser des questions ou faire des suggestions pour améliorer ce projet.

### Explication des sections ajoutées

- **Fonctionnalités** : Décrit ce que le projet peut faire, pour donner une vue d'ensemble rapide.
- **Installation** : Donne des instructions claires pour installer le projet.
- **Utilisation** : Montre comment exécuter le script principal.
- **Structure des fichiers** : Explique les fichiers principaux du projet pour faciliter la navigation.
- **Exemples de données** : Fournit un exemple du format des données extraites pour une meilleure compréhension des résultats.






