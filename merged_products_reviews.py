import json
import csv

# Étape 1 : Charger les données des fichiers JSON
try:
    with open("all_products_unique.json", "r", encoding="utf-8") as file:
        products_data = json.load(file)
        print(f"Chargement réussi de all_products_unique.json : {len(products_data)} produits trouvés.")
except Exception as e:
    print("Erreur lors du chargement de all_products_unique.json :", e)

try:
    with open("product_reviews.json", "r", encoding="utf-8") as file:
        reviews_data = json.load(file)
        print(f"Chargement réussi de product_reviews.json : {len(reviews_data)} reviews trouvées.")
except Exception as e:
    print("Erreur lors du chargement de product_reviews.json :", e)

# Étape 2 : Créer un dictionnaire des reviews avec les URLs comme clés
reviews_dict = {review["url"]: review for review in reviews_data}
print("Dictionnaire des reviews créé avec succès.")

# Étape 3 : Fusionner les données de reviews avec les données de produits
merged_data = []
for product in products_data:
    product_url = product["item"]["url"]
    # Si des reviews existent pour ce produit, les ajouter
    if product_url in reviews_dict:
        product["reviews"] = reviews_dict[product_url]["reviews"]
        product["rating"] = reviews_dict[product_url]["rating"]
    merged_data.append(product)

print(f"Fusion réussie : {len(merged_data)} produits fusionnés.")

# Étape 4 : Sauvegarder les données fusionnées dans un nouveau fichier JSON
try:
    with open("merged_products_reviews.json", "w", encoding="utf-8") as file:
        json.dump(merged_data, file, ensure_ascii=False, indent=4)
    print("Les données fusionnées ont été sauvegardées dans merged_products_reviews.json")
except Exception as e:
    print("Erreur lors de la sauvegarde du fichier JSON fusionné :", e)

# Étape 5 : Convertir le JSON fusionné en CSV
try:
    with open("merged_products_reviews.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    with open("merged_products_reviews.csv", "w", encoding="utf-8", newline="") as csv_file:
        fieldnames = ["url", "name", "price", "rating", "reviews"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for product in data:
            row = {
                "url": product["item"]["url"],
                "name": product["item"]["name"],
                "price": product["offers"]["price"],
                "rating": product.get("rating", "Pas de note"),
                "reviews": " | ".join(product.get("reviews", []))
            }
            writer.writerow(row)

    print("Conversion en CSV réussie : merged_products_reviews.csv")
except Exception as e:
    print("Erreur lors de la conversion en CSV :", e)
