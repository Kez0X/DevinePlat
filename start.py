from categories import categories
from questions import questions
from verificationReponse import *
from affichage import *

def start():
    """
    Fonction : Pour lancer le programme
    Entrée : ///
    Sortie : ///
    """
    print("Bienvenue sur DevinePlat...\nLancement du programme...\nChargement des ingrédients...\n\nVoici une liste des plats, choisissez en un parmi tous cela :\n")
    # On affiche les categories pour que l'utilisateur puisse faire un choix
    affichage(categories)
    # On initilise le dictionnaire à la copie du dictionnaires des catégories
    dicoPlat = categories.copy()
    # On va parcourir les différentes questions de notre dictionnaires de questions 
    # On va poser nos questions une par une
    for question in questions:
        reponse = str(input(questions[question]))
        # On initilise la liste des elements qu'on devra supprimer
        listeSupp = []
        # Si la réponse à la question est positive alors on a juste à supprimer toutes les lignes ou la reponse est négative donc False
        if verificationReponse(reponse):
            for keys in dicoPlat:
                if dicoPlat[keys][question]==False:
                    # On supprime la ligne entière grâce à la clé qu'on va ajouter dans la liste pour supprimer cela plus tard
                    # On fait ça pour éviter d'avoir une erreur de modification de la boucle au niveau du dictionnaire
                    listeSupp.append(keys)
        # On fait de même dans le cas contraire
        else:
            for keys in dicoPlat:
                if dicoPlat[keys][question]:
                    listeSupp.append(keys)
        # On n'a plus qu'à supprimer les elements dans listeSupp
        for eltToSup in listeSupp:
            del dicoPlat[eltToSup]
    # Si notre dictionnaire est bien fait alors il n'est censé resté qu'un seul élément
    # Au cas où nous prévoyons tout de même les autres cas
    if len(list(dicoPlat.keys())) == 0:
        rep = "Votre plat est : " + str(list(dicoPlat.keys())[0])
    else:
        rep = "Une erreur s'est produite, une mise à jour au niveau du dictionnaire est requise"

    return rep 
    
print(start())