# 🛍️ Sklum Product Scraping Project

Ce projet consiste à extraire des informations de produits, y compris les avis et les notes, du site Sklum. L'objectif est de récupérer les données de produits pour une analyse et une utilisation ultérieure dans des projets de data science ou d'analyse de marché.

## Table des matières
- [📖 Aperçu du projet](#aperçu-du-projet)
- [🛠️ Prérequis](#prérequis)
- [🔑 Fonctionnalités Clés](#fonctionnalités-clés)
- [📥 Installation](#installation)
- [▶️ Utilisation](#utilisation)
- [📁 Structure des fichiers](#structure-des-fichiers)
- [📊 Exemples de données](#exemples-de-données)
- [👤 Auteurs](#auteurs)

## 📖 Aperçu du projet

Le projet utilise Python 🐍 et les bibliothèques `requests` et `BeautifulSoup` pour :
- 🛒 Extraire des informations produits.
- ⭐ Collecter des avis et notes.
- 📊 Analyser les données extraites pour des visualisations.

Les données sont sauvegardées dans des fichiers JSON pour une analyse ultérieure.

## 🛠️ Prérequis

- **Python 3.x** 🐍 : Téléchargeable depuis [python.org](https://www.python.org/).
- **Power BI** 📊 : Téléchargeable depuis [powerbi.microsoft.com](https://powerbi.microsoft.com/).

## 🔑 Fonctionnalités Clés

- 📊 **Histogramme de Distribution des Prix** : Analyse de la répartition des prix.
- ⭐ **Analyse des Notes des Produits** : Distribution des notes par produit.
- 📈 **Comparaison Prix et Note** : Identifier si les produits coûteux sont mieux notés.

## 📥 Installation

1. Clonez le dépôt GitHub :

   ```bash
   git clone https://github.com/bolyderiz/sklum_scrapping.git
   cd sklum_scrapping

2. Installez les dependecies requises :

   ```bash
   pip install requests beautifulsoup4

## ▶️ Utilisation

1. Exécutez le script principal main_final.py pour extraire les informations produits et les avis :

2. Les avis et informations des produits seront sauvegardés dans le fichier product_reviews.json une fois l'extraction terminée.

3. Visualisation dans Power BI : Une fois les données extraites, vous pouvez les charger dans Power BI pour créer des visuels basés sur les informations produits et les avis.


## 📁 Structure des fichiers

- `all_product_links.txt` : Contient tous les liens des produits extraits.
- `fetch_reviews_ratings.py` : Script pour récupérer les avis et les notes des produits.
- `main_final.py` : Script principal pour exécuter l'extraction complète.
- `merged_products_reviews.json` : Fichier JSON fusionné contenant les informations de produits et les avis.
- `README.md` : Documentation du projet.
- `.gitignore` : Exclut les fichiers générés et non nécessaires au dépôt (fichiers JSON, HTML, Excel).


## 📊 Exemples de données
Voici un exemple de structure des données extraites, stockées dans product_reviews.json :

```json
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
```

## 👤 Auteurs
bolyderiz - GitHub Profile

N'hésitez pas à contribuer, poser des questions ou faire des suggestions pour améliorer ce projet.






