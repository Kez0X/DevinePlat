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
    # On va générer le jeu du J1
    print("Bienvenue sur DevinePlat...\nLancement du programme...\nChargement des ingrédients...\n\nVoici une liste des plats, choisissez en un parmi tous cela :\n")
    affichage(categories)
    # Initialisation du dictionnaire avec pandas
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
    rep = "Votre plat est : " + str(list(dicoPlat.keys())[0])
    return rep 
    
print(start())