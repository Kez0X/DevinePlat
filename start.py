# Dans notre Arbre la gauche correspondra à non et la droite correspondra à oui
from main import *
from categories import categories
from generationData import *
from main import *
from trouveCategories import *
from trouveMetier import *

def start():
    """
    Fonction : Pour lancer le programme
    """
    # On va générer le jeu du J1
    print("Lancement du programme...")
    generationCsv(categories)
    reponse = str(input("Souhaitez vous rajouter un métier ?"))
    while verificationReponse(reponse):
        metier = str(input("Quel métier souhaitez vous rajouter ?"))
        categorie = str(input("À quelle catégorie appartient votre métier ?"))
        categories[categorie] = ajoutMetier(metier, categorie)
        reponse = str(input("Souhaitez vous rajouter un métier ?"))
    affichageCsv('metiers.csv')
    print("Choisissez votre métier... Je vais essayer de le deviner")
    # Le J1 a choisit son métier, maintenant nous devons trouver la catégorie et le métier
    types, data = main()
    cat = [elements for elements in types]
    categorieTrouve = trouveCategories(cat)
    metierTrouve = trouveMetier(data,categorieTrouve)
    return metierTrouve

print(start())