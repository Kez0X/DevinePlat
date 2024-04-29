from questionReponse import *

def trouveCategories(categories):
    """
    Entrée : categories, une liste de categories
    Sortie : la catégorie de l'utilisateur
    """
    a_chercher = []
    deja_chercher = []
    trouve = False
    indice = 0
    categorieTrouve = "Aucune des catégories ne correpond !"
    while trouve==False and len(deja_chercher)!=len(categories):
        if categories[indice] not in deja_chercher:
            a_chercher.append(categories[indice])
            reponse = str(input(genererQuestion(a_chercher[0])))
            if verificationReponse(reponse):
                trouve = True
                categorieTrouve = a_chercher[0]
            else:
                deja_chercher.append(a_chercher.pop(0))
                indice = indice +1
    print("Vous travaillez dans le domaine suivant : ", categorieTrouve)
    return categorieTrouve