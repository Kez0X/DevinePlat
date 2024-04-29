import csv

class Noeud:
    def __init__(self, question=None, oui=None, non=None):
        self.question = question
        self.oui = oui
        self.non = non

def construire_arbre_questions(data, categories):
    racine = Noeud()

    for categorie in categories:
        sous_arbres = {}
        for metier in data:
            if data[metier] == categorie:
                sous_arbres[metier] = data[metier]

        if sous_arbres:
            question = f"Travaillez-vous dans le domaine de {categorie.lower()} ?"
            if racine.question is None:
                racine.question = question
                racine.oui = Noeud()
                racine.non = Noeud()
            else:
                construire_arbre_questions_rec(racine.oui, sous_arbres, categories)

    return racine

def construire_arbre_questions_rec(noeud, data, categories):
    for categorie in categories:
        sous_arbres = {}
        for metier in data:
            if data[metier] == categorie:
                sous_arbres[metier] = data[metier]

        if sous_arbres:
            question = f"Travaillez-vous dans le domaine de {categorie.lower()} ?"
            if noeud.question is None:
                noeud.question = question
                noeud.oui = Noeud()
                noeud.non = Noeud()
            else:
                if noeud.oui is None:
                    noeud.oui = Noeud()
                if noeud.non is None:
                    noeud.non = Noeud()
                construire_arbre_questions_rec(noeud.oui, sous_arbres, categories)
                construire_arbre_questions_rec(noeud.non, sous_arbres, categories)


def poser_questions(noeud, historique=[]):
    while True:
        if noeud.question is None:
            print("Impossible de déterminer le métier.")
            return
        reponse = input(noeud.question + " (oui/non): ").lower()
        if reponse == 'oui':
            if noeud.oui is None:
                print(f"Le métier auquel vous pensez est {noeud.question.lower()}")
                return
            else:
                historique.append((noeud, True))
                noeud = noeud.oui
        elif reponse == 'non':
            if noeud.non is None:
                print(f"Le métier auquel vous pensez est {noeud.question.lower()}")
                return
            else:
                historique.append((noeud, False))
                noeud = noeud.non
        else:
            print("Veuillez répondre par 'oui' ou 'non'.")

        # Si on atteint une feuille sans avoir trouvé le métier,
        # on remonte dans l'arbre en explorant les autres possibilités
        while noeud.question is None and historique:
            dernier_noeud, derniere_reponse = historique.pop()
            if derniere_reponse:
                dernier_noeud = dernier_noeud.non
            else:
                dernier_noeud = dernier_noeud.oui
            if dernier_noeud is not None:
                poser_questions(dernier_noeud, historique)
                return


def main():
    with open('metiers.csv', mode='r', newline='', encoding='utf-8') as csvfile:
        lecteur_csv = csv.DictReader(csvfile)
        data = {row['Métier']: row['Catégorie'] for row in lecteur_csv}
        categories = set(data.values())

    arbre_questions = construire_arbre_questions(data, categories)
    poser_questions(arbre_questions)
