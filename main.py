import csv

def main():
    with open('metiers.csv', mode='r', newline='', encoding='utf-8') as csvfile:
        lecteur_csv = csv.DictReader(csvfile)
        data = {row['Métier']: row['Catégorie'] for row in lecteur_csv}
        categories = set(data.values())

    return categories, data