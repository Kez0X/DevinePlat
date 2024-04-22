class ABR():
    """
    Classe implémentant un Arbre Binaire de Recherche 
    """
    def __init__(self,r,fg=None,fd=None):
        """
        Entrées : racine (elt) x filsGauche (ABR) x filsDroit (ABR) -> Par défaut les fils sont mis à None.
        Sortie : un ABR 
        >>> ABR(4)
        <ABR.ABR object at 0x...>
        >>> ABR(4,ABR(3),ABR(2))
        <ABR.ABR object at 0x...>
        Fonction : Méthode constructrice de ma structure
        """
        self.racine = r
        self.filsGauche = fg
        self.filsDroit = fd

    def estFeuille(self):
        """
        Entrée : //
        Sortie : Un booléen
        Fonction : Renvoie True si l'arbre est une feuille, False sinon. 
        """
        return self.filsGauche == None and self.filsDroit == None

    def ajouterFilsGauche(self, fg):
        """
        Entrée : fg Le fils gauche que l'on souhaite ajouter
        Sortie : //
        Fonction : Ajoute un fils gauche à l'arbre
        """
        self.filsGauche = fg

    def ajouterFilsDroit(self, fd):
        """
        Entrée : fd Le fils droit que l'on souhaite ajouter
        Sortie : //
        Fonction : Ajoute un fils droit à l'arbre
        """
        self.filsDroit = fd

    def parcours(self):
        """
        Fonction : Parcourt l'arbre en profondeur
        """
        print(self.racine)
        if self.filsGauche:
            print("Non:")
            self.filsGauche.parcours()
        if self.filsDroit:
            print("Oui:")
            self.filsDroit.parcours()
