import re

def genererQuestion(mot):
    """
    Génère une question pertinente en fonction du mot donné en entrée.
    Entrée : mot : str Le mot à partir duquel générer la question.
    Sortie : str : La question générée.
    """
    return f"Travaillez-vous dans le domaine de {mot.lower()} ?"

def genererQuestionMetier(mot):
    """
    Génère une question pertinente en fonction du mot donné en entrée.
    Entrée : mot : str Le mot à partir duquel générer la question.
    Sortie : str : La question générée.
    """
    return f"Êtes vous {mot.lower()} ?"

def verificationReponse(reponse):
    """
    Vérifie si la réponse à la question est positive.
    Entrée :reponse : str La réponse donnée par l'utilisateur.
    Sortie : bool : True si la réponse est positive, False sinon.
    """
    # Utilisation d'une expression régulière pour rechercher les réponses positives
    return bool(re.match(r'^\s*(oui|en effet)', reponse, re.IGNORECASE))