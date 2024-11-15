# Importer les bibliothèques nécessaires
# BeautifulSoup pour analyser le contenu HTML,
# requests pour envoyer des requêtes HTTP,
# json pour manipuler les fichiers JSON,
# time pour ajouter des pauses entre les requêtes
from bs4 import BeautifulSoup
import requests
import json
import time

# Fonction pour récupérer les informations des produits d'une page spécifique
def fetch_products_from_page(page_num):
    # Construire l'URL pour accéder à une page spécifique de la catégorie "Mobilier"
    url = f'https://www.sklum.com/fr/524-acheter-mobilier/search/stars-all?p={page_num}'
    
    # Définir l'en-tête pour simuler une requête provenant d'un navigateur
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
    
    # Envoyer la requête HTTP GET pour obtenir le contenu HTML de la page
    response = requests.get(url, headers=headers)
    
    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        # Extraire le texte du contenu HTML de la page
        html_content = response.text
        
        # Utiliser BeautifulSoup pour analyser le contenu HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Trouver toutes les balises <script> de type "application/ld+json" contenant des données JSON
        script_tags = soup.find_all('script', type='application/ld+json')
        
        # Vérifier qu'il y a bien des balises script pour éviter les erreurs d'index
        if len(script_tags) > 2:
            # Charger le contenu JSON de la troisième balise <script> en tant qu'objet Python
            json_obj = json.loads(script_tags[2].get_text())
            
            # Extraire la liste des produits de l'objet JSON
            products = json_obj.get("itemListElement", [])
            
            # Retourner la liste des produits pour cette page
            return products
    else:
        # Afficher un message d'erreur si la requête a échoué
        print(f"Erreur lors de la requête pour la page {page_num}")
    
    # Retourner une liste vide si la requête échoue ou si aucun produit n'est trouvé
    return []

# Initialiser une liste pour stocker les informations de tous les produits de toutes les pages
all_products = []

# Boucle pour récupérer les produits de toutes les pages (32 pages de 50 produits + 1 page de 38 produits)
for i in range(1, 34):  # Pages de 1 à 33
    # Appeler la fonction fetch_products_from_page pour récupérer les produits de la page courante
    products = fetch_products_from_page(i)
    
    # Ajouter les produits de la page courante à la liste totale des produits
    all_products.extend(products)
    
    # Pause d'une seconde pour éviter de surcharger le serveur avec des requêtes trop rapides
    time.sleep(1)

# Extraire les URLs des produits pour vérifier les doublons
urls = [product["item"]["url"] for product in all_products if "item" in product and "url" in product["item"]]
# Utiliser un ensemble (set) pour ne conserver que les URLs uniques
unique_urls = set(urls)

# Afficher le nombre total d'URLs, le nombre d'URLs uniques et le nombre de doublons détectés
print(f"Nombre total d'URLs : {len(urls)}")
print(f"Nombre d'URLs uniques : {len(unique_urls)}")
print(f"Nombre de doublons détectés : {len(urls) - len(unique_urls)}")

# Filtrer les produits pour ne conserver que les uniques par URL
# En utilisant un dictionnaire pour éviter les doublons (les clés du dictionnaire sont les URLs)
unique_products = {product["item"]["url"]: product for product in all_products if "item" in product and "url" in product["item"]}

# Convertir le dictionnaire en liste pour obtenir la liste finale des produits uniques
all_products = list(unique_products.values())

# Afficher le nombre total de produits uniques récupérés
print(f"Nombre total de produits uniques récupérés : {len(all_products)}")

# Sauvegarder les produits uniques dans un fichier JSON
with open("all_products_unique.json", "w", encoding="utf-8") as file:
    # Écrire les produits dans le fichier JSON avec une indentation pour faciliter la lecture
    json.dump(all_products, file, ensure_ascii=False, indent=4)

# Afficher un message de confirmation une fois les produits sauvegardés
print("Les produits uniques ont été stockés dans all_products_unique.json")
