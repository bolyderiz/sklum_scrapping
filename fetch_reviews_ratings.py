# Importer BeautifulSoup pour analyser le contenu HTML, requests pour envoyer des requêtes HTTP,
# time pour ajouter des pauses entre les requêtes, et json pour manipuler les fichiers JSON
from bs4 import BeautifulSoup
import requests
import time
import json

# Charger les liens des produits depuis un fichier texte "all_product_links.txt".
# Chaque lien est filtré pour s'assurer qu'il commence par "http" (pour éviter les lignes vides ou non valides).
with open("all_product_links.txt", "r") as file:
    product_links = [line.strip() for line in file.readlines() if line.strip().startswith("http")]

# Afficher le nombre total de liens de produits à traiter
print(f"Nombre total de liens produits à traiter : {len(product_links)}")

# Créer une liste vide pour stocker les avis de chaque produit
all_reviews = []

# Définir une fonction pour extraire les avis et les notes d'un produit donné
def fetch_reviews(url):
    """
    Récupère les avis et les notes pour un produit à partir de son URL.

    Args:
        url (str): Lien du produit.

    Returns:
        dict: Dictionnaire contenant l'URL, la note moyenne et la liste des avis.
    """
    # Définir les en-têtes pour la requête HTTP pour simuler un navigateur
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
    
    try:
        # Envoyer une requête GET à l'URL du produit avec les en-têtes définis
        response = requests.get(url, headers=headers)
        
        # Vérifier si la requête a réussi (code de statut 200)
        if response.status_code == 200:
            # Utiliser BeautifulSoup pour analyser le contenu HTML de la page du produit
            soup = BeautifulSoup(response.text, 'html.parser')

            # Initialiser une liste pour stocker les avis de ce produit
            reviews = []
            
            # Trouver l'élément HTML qui contient la note moyenne du produit
            rating_element = soup.find("span", class_="c-product-review__avg")
            # Extraire le texte de la note moyenne si elle existe, sinon afficher "Pas de note"
            rating = rating_element.text.strip() if rating_element else "Pas de note"

            # Trouver tous les éléments HTML qui contiennent les avis (commentaires des utilisateurs)
            review_elements = soup.find_all("span", class_="c-product-review-card__text")
            # Parcourir chaque élément de commentaire et extraire le texte de l'avis
            for review in review_elements:
                reviews.append(review.get_text(strip=True))

            # Retourner un dictionnaire contenant l'URL, la note moyenne et la liste des avis
            return {
                "url": url,
                "rating": rating,
                "reviews": reviews
            }
        else:
            # Si le code de statut n'est pas 200, afficher un message d'erreur
            print(f"Erreur lors de la requête pour l'URL {url} : {response.status_code}")
            return None
    except Exception as e:
        # Gérer les erreurs possibles (par exemple, problème de connexion) et afficher un message
        print(f"Erreur lors de la connexion à {url} : {e}")
        return None

# Parcourir tous les liens de produits pour extraire leurs avis
for idx, url in enumerate(product_links, start=1):
    # Afficher le numéro de l'URL en cours de traitement et l'URL elle-même
    print(f"Traitement de l'URL {idx}/{len(product_links)} : {url}")
    
    # Appeler la fonction fetch_reviews pour extraire les avis du produit actuel
    review_data = fetch_reviews(url)
    
    # Si des avis ont été extraits, les ajouter à la liste all_reviews
    if review_data:
        all_reviews.append(review_data)
        # Afficher un message de confirmation avec la note moyenne et le nombre d'avis
        print(f"✔ Avis récupérés pour {url} - Note moyenne : {review_data['rating']} - Nombre d'avis : {len(review_data['reviews'])}")
    else:
        # Si aucun avis n'a été récupéré, afficher un message d'erreur
        print(f"✘ Aucun avis récupéré pour {url}")
    
    # Ajouter une pause d'une seconde entre chaque requête pour ne pas surcharger le serveur
    time.sleep(1)

# Sauvegarder tous les avis récupérés dans un fichier JSON appelé "product_reviews.json"
with open("product_reviews.json", "w", encoding="utf-8") as f: 
    # Écrire la liste all_reviews dans le fichier JSON avec une indentation pour faciliter la lecture
    json.dump(all_reviews, f, ensure_ascii=False, indent=4)

# Afficher un message indiquant que l'extraction est terminée et où les données sont stockées
print("Extraction terminée ! Les avis des produits ont été stockés dans product_reviews.json")

