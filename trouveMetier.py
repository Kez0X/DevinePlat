from questionReponse import *
from ajoutMetier import *

def trouveMetier(data,categorie):
    """
    Entrée : categories, une liste de categories
    Sortie : la catégorie de l'utilisateur
    """
    metiers = []
    for keys in data:
        if data[keys]==categorie:
            metiers.append(keys)
    a_chercher = []
    deja_chercher = []
    trouve = False
    indice = 0
    metierTrouve = None
    while trouve==False and len(deja_chercher)!=len(metiers):
        if metiers[indice] not in deja_chercher:
            a_chercher.append(metiers[indice])
            reponse = str(input(genererQuestionMetier(a_chercher[0])))
            if verificationReponse(reponse):
                trouve = True
                metierTrouve = a_chercher[0]
            else:
                deja_chercher.append(a_chercher.pop(0))
                indice = indice +1
    if metierTrouve == None:
        reponse = str(input("Souhaitez vous rajouter un métier ?"))
        if verificationReponse(reponse):
            metier = str(input("Quel métier souhaitez vous rajouter ?"))
            ajoutMetier(metier)
    print("Vous êtes : ", metierTrouve)
    return metierTrouve