import csv

def main():
    """
    Fonction : récupère un set des catégories et un dictionnaire avec les métiers
    Entrée: ///
    Sortie : categories : set des catégories, data : dictionnaire avec les métiers
    """
    with open('metiers.csv', mode='r', newline='', encoding='utf-8') as csvfile:
        lecteur_csv = csv.DictReader(csvfile)
        data = {row['Métier']: row['Catégorie'] for row in lecteur_csv}
        categories = set(data.values())

    return categories, data