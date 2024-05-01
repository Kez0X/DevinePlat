from categories import categories

total_possibilites = len(categories)

# Nombre de métiers répertoriés
nb_metiers = sum(len(options) for options in categories.values())

# Vérification
if nb_metiers == total_possibilites:
    print("Oui, il y a un métier pour chaque possibilité associée.")
else:
    print("Non, il manque des métiers pour certaines possibilités.")

from itertools import combinations

# Liste des plats
plats = list(categories.keys())

# Liste des combinaisons d'arguments
combinaisons = []
for plat in plats:
    for comb in combinations(categories[plat].items(), 2):
        combinaisons.append(comb)

# Vérification des doublons
doublons = [comb for comb in combinaisons if combinaisons.count(comb) > 1]

if doublons:
    print("Il existe des doublons de combinaisons d'arguments :\n", doublons)
else:
    print("Il n'y a pas de doublons de combinaisons d'arguments.")
