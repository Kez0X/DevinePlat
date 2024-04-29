import csv
from categories import *

def ajoutMetier(metier, categorie):
    """
    Ajoute un métier avec sa catégorie dans le fichier CSV.
    Entrée : metier : str Le nom du métier à ajouter. categorie : str La catégorie du métier.
    """
    # Nom du fichier CSV
    fichier_csv = 'metiers.csv'

    # Ajout du métier dans le fichier CSV
    with open(fichier_csv, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([categorie, metier])
    
    categories[categorie] = metier

    print(f"Le métier '{metier}' a été ajouté à la catégorie '{categorie}'.")
    return categories