from main import *
from categories import categories
from generationData import *
from main import *
from trouveCategories import *
from trouveMetier import *

def start():
    """
    Fonction : Pour lancer le programme
    Entrée : ///
    Sortie : ///
    """
    # On va générer le jeu du J1
    print("Bienvenue sur DevineJob...\nLancement du programme...")
    # On génère le fichier csv
    generationCsv(categories)
    # On propose à l'utilisateur de rajouter un métier
    reponse = str(input("Souhaitez vous rajouter un métier ?"))
    while verificationReponse(reponse):
        metier = str(input("Quel métier souhaitez vous rajouter ?"))
        categorie = str(input("À quelle catégorie appartient votre métier ?"))
        # On ajoute le métier au fichier csv et au dictionnaire
        categories[categorie] = ajoutMetier(metier, categorie)
        reponse = str(input("Souhaitez vous rajouter un métier ?"))
    # On affiche le contenu du fichier csv
    affichageCsv('metiers.csv')
    print("Choisissez votre métier... Je vais essayer de le deviner")
    # Le J1 a choisit son métier, maintenant nous devons trouver la catégorie et le métier
    types, data = main()
    cat = [elements for elements in types]
    categorieTrouve = trouveCategories(cat)
    metierTrouve = trouveMetier(data,categorieTrouve)
    return metierTrouve

print(start())