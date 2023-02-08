# Variables Globales
couleurs = ('CARREAU', 'COEUR', 'TREFLE', 'PIQUE')
noms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}
str_val_dict = {1: 'As', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Valet', 12: 'Dame', 13: 'Roi'}


class input_symbol_error(Exception):
    """
    Erreur personnalisée informant l'utilisateur d'une mauvaise saisie.
    """
    pass

class input_name_error(Exception):
    """
    Erreur personnalisée informant l'utilisateur d'une mauvaise saisie.
    """
    pass


class Carte:
    
    def __init__(self, nom, couleur):
        """
        Affectation de l'attribut nom et de l'attribut couleur.
        """
        try :
            if couleur.upper() in couleurs :
                self.color = couleur.upper()  # On formate en FULL MAJ
            else :
                raise input_symbol_error
        except input_symbol_error :
            print("Le symbole de la carte est incorrect :",couleur)
            exit()
            
        try:
            try :
                if nom.capitalize() in noms:
                    self.name = nom.capitalize()  # On formate en majuscule seulement sur la première lettre
                    self.value = valeurs[self.name]
            except :
                pass
            if str_val_dict[nom] in noms :
                self.name = str_val_dict[nom]
                self.value = valeurs[self.name]
            else :
                raise input_name_error
        except input_name_error :
            print("Le Numéro/Nom de la carte est invalide :",nom)
            exit()
        
    
    def setCouleur(self, couleur):
        """
        Mutateur de l'attribut couleur (de la liste couleurs)
        """
        try :
            if couleur.upper() in couleurs :
                self.color = couleur.upper()  # On formate en FULL MAJ
            else :
                raise input_symbol_error
        except input_symbol_error :
            print("Le symbole de la carte est incorrect :",couleur)
            exit()
    
    def setNom(self, nom):
        """
        Mutateur de l'attribut nom (de la liste noms)
        """
        try:
            try :
                if nom.capitalize() in noms:
                    self.name = nom.capitalize()  # On formate en majuscule seulement sur la première lettre
                    self.value = valeurs[self.name]
            except :
                pass
            if str_val_dict[nom] in noms :
                self.name = str_val_dict[nom]
                self.value = valeurs[self.name]
            else :
                raise input_name_error
        except input_name_error :
            print("Le Numéro/Nom de la carte est invalide :",nom)
            exit()
        
    def getNom(self):
        """
        Renvoie le nom de la carte (de la liste noms): Accesseur
        """
        return self.name
        
    def getCouleur(self):
        """
        Renvoie la couleur de la carte (de la liste couleur)
        """
        return self.color
    
    def getValeur(self):
        """
        Renvoie la valeur de la carte (du dictionnaire valeurs) : Accesseur
        """
        return self.value
    
    def getAttributs(self):
        "Permet d'accéder aux valeurs des attributs"
        return (self.value,self.color)
        
    def egalite(self, carte):
        """
        Renvoie True si les cartes self et carte ont la même valeur,
        Renvoie False si ce n'est pas le cas.
        carte: Un autre Objet de type Carte
        """
        
        if self.value == carte.value :
            return True
        else :
            return False
    
    def estSuperieureA(self, carte):
        """
        Renvoie True si la valeur de self est supérieure à celle de carte,
        Renvoie False si ce n'est pas le cas.
        carte: Objet de type Carte
        """
        
        if self.value > carte.value :
            return True
        else :
            return False
        
    def estInferieureA(self, carte):
        """
        Renvoie True si la valeur de self est inféreure à celle de carte,
        Renvoie False si ce n'est pas le cas.
        carte: Objet de type Carte
        """
        
        if self.value < carte.value :
            return True
        else :
            return False
        

########################################################
############## Test de la classe Carte #################
########################################################

def testCarte():
    valetCoeur = Carte('Valet', 'COEUR')
    print('Nom:', valetCoeur.getNom())
    print('Couleur:', valetCoeur.getCouleur())
    print('Valeur:', valetCoeur.getValeur())
    valetCoeur.setNom('Dame')
    print('Nom modifie:', valetCoeur.getNom())
    print('Valeur modifiee:', valetCoeur.getValeur())
    
    # Essai des exceptions: cette instruction conduit à une erreur
    dameCarreau = Carte('Dame', 'COooEUR')
    print('Nom:', dameCarreau.getNom())
    print('Couleur:', dameCarreau.getCouleur())
    print('Valeur:', dameCarreau.getValeur())