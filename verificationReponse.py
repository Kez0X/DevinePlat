import re

def verificationReponse(reponse):
    """
    Vérifie si la réponse à la question est positive.
    Entrée :reponse : str La réponse donnée par l'utilisateur.
    Sortie : bool : True si la réponse est positive, False sinon.
    """
    # Utilisation d'une expression régulière pour rechercher les réponses positives
    return bool(re.match(r'^\s*(oui|en effet)', reponse, re.IGNORECASE))