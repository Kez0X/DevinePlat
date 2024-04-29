# Dans notre Arbre la gauche correspondra à non et la droite correspondra à oui
from ABR import *
from categories import *
from generationData import *

def start():
    """
    Fonction : Pour lancer le programme
    """
    # On va générer le jeu du J1
    generationCsv(categories)
    affichageCsv('metiers.csv')
    print("Choisissez votre métier... Je vais essayer de le deviner")
    # Initialisation de l'arbre de question et de choix pour la machine et lancement du processus de recherche
    return main()

print(start())