from Hand import *

class Joueur :
    
    def __init__(self, nom, nbCartes) :
        """
        Initiamise un objet de type Joueur.
        """
        self.nom = nom
        self.nbCartes = nbCartes
        self.mainJoueur = Main(self.nom)
        
    def setMain(self, paquet_pioche):
        """
        Définit la main du joueur, donc la liste de ses cartes au début du jeu.
        """
        self.mainJoueur.add_cartes(paquet_pioche)
    
    def getpaquet_Main(self):
        return self.mainJoueur.get_paquet()
        
    def getNom(self):
        """
        Accesseur de l’attribut nom.
        """
        return self.nom

    def getNbCartes(self):
        """
        Accesseur du champ nbCartes.
        """
        return self.nbCartes
    
    def jouerCarte(self):
        """
        Enlève et renvoie la dernière carte (objet de type Carte) de la main du joueur pour la jouer,
        ou retourne None s’il n’y a plus de cartes dans la main du joueur.
        """
        return self.getpaquet_Main().pop()
    
    def insererMain(self, win_cartes):
        """
        Fonction qui insère les cartes de la liste des cartes gagnées dans la main du Joueur.
        """
        self.mainJoueur.add_cartes(win_cartes)