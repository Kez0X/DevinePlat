# Dans notre Arbre la gauche correspondra à non et la droite correspondra à oui
from ABR import *
from data import *

def start():
    Arbre = ABR("Avez vous un métier ?")
    init(data, Arbre)
    return question(Arbre)

def init(data, Arbre):
    """
    Entrée : data : un dictionnaire contennant le jeu de donnée sous la forme suivante : {'question' : "Allez-vous bien ?", 'oui' : {'question' : "Allez-vous bien ?", 'oui' : None, 'non' : None}, 'non' : {'question' : "Allez-vous bien ?", 'oui' : None, 'non' : None }}
    Sortie : L'arbre initialisé avec un jeu de donnée
    Fonction : Initialise un arbre binaire de recherche avec un jeu de donnée
    """
    if data['non'] is None and data['oui'] is None: 
        Arbre.ajouterFilsGauche(None)
        Arbre.ajouterFilsDroit(None)
    elif data['oui'] is None:
        Arbre.ajouterFilsDroit(None)
        Arbre.ajouterFilsGauche(ABR(data['non']['question']))
        init(data['non'], Arbre.filsGauche)
    elif data['non'] is None:
        Arbre.ajouterFilsGauche(None)
        Arbre.ajouterFilsDroit(ABR(data['oui']['question']))
        init(data['oui'], Arbre.filsDroit)
    else:
        Arbre.ajouterFilsDroit(ABR(data['oui']['question']))
        Arbre.ajouterFilsGauche(ABR(data['non']['question']))
        init(data['non'], Arbre.filsGauche)
        init(data['oui'], Arbre.filsDroit)

def question(Arbre):
    if Arbre.filsDroit is None and Arbre.filsGauche is None: 
        # C'est la réponse
        return Arbre.racine
    else :
        choix = str(input(Arbre.racine))
        if choix == "Oui" or choix=="oui" or choix =="o" or choix =="O":
            return question(Arbre.filsDroit)
        else :
            return question(Arbre.filsGauche)



print(start())