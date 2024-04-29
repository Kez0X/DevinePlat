import csv
import random

def generationCsv(categories):
    # Générer 40 métiers aléatoirement à partir du jeu de donnée
    # On va toujours faire en sorte d'avoir un jeu de donnée différents
    metiers = []
    for _ in range(40):
        categorie = random.choice(list(categories.keys()))
        metier = random.choice(categories[categorie])
        # Pour éviter d'avoir des doublons
        while {"Catégorie": categorie, "Métier": metier} in metiers:
            categorie = random.choice(list(categories.keys()))
            metier = random.choice(categories[categorie])
        metiers.append({"Catégorie": categorie, "Métier": metier})

    # Écrire les métiers dans un fichier CSV
    with open("metiers.csv", "w", newline="", encoding="utf-8") as csvfile:
        csvfile.truncate(0)
        fieldnames = ["Catégorie", "Métier"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for metier in metiers:
            writer.writerow(metier)
    return "Le fichier metiers.csv a été créé avec succès."

def affichageCsv(fichier_csv):
    """
    Entrée : le chemin du fichier
    Sortie : le plateau du J1
    Fonction : Creer un affichage de plateau pour le J1
    """
    # Ouvrir le fichier CSV en mode lecture
    with open(fichier_csv, mode='r', newline='', encoding='utf-8') as csvfile:
        # Créer un lecteur CSV
        lecteur_csv = csv.reader(csvfile)
        # Lire chaque ligne du fichier CSV
        print("Vous pouvez choisir parmis ces 40 métiers")
        for ligne in lecteur_csv:
            # Afficher la ligne (chaque ligne est une liste)
            print(ligne[1])
                