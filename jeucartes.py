from carte import * # Il faut importer la classe Carte et les variables globales
from Player import *
import random # Nécessaire pour mélanger le jeu

symbol_dict = {1: 'CARREAU', 2: 'COEUR', 3: 'TREFLE', 4:'PIQUE'}


class JeuCartes:
    
    def __init__(self, nbCartes=52):
        """
        Le jeu doit comporter 32 ou 52 cartes, effectuer un contrôle
        """
        if nbCartes == 32 or nbCartes == 52 :
            self.nombreCarte=nbCartes
        else :
            self.nombreCarte=52 # 52 sera donc le nombre de cartes par défaut dans le paquet.
            
        self.jeu=[] # self.jeu est une liste des self.nbCartes
        self.creerJeu()

###########################################################################
################# Définition des méthodes d'instances #####################
###########################################################################
    def getTailleJeu(self):
        ''' Fonction qui retourne le nombre de cartes du jeu
        Valeur retournée: type int '''
        return self.nombreCarte

    def creerJeu(self):
        '''Créée la liste des cartes de l'attribut self.jeu '''
        if self.nombreCarte == 52 :
            for couleur in range(1,5):
                for valeur in range(1, 14):
                    carte = Carte(valeur, symbol_dict[couleur])
                    self.jeu.append(carte)
        elif self.nombreCarte == 32 :
            for couleur in range(1,5):
                for valeur in range(1, 9):
                    carte = Carte(str(valeur), symbol_dict[couleur])
                    self.jeu.append(carte)

    def getJeu(self):
        '''Renvoie la liste des cartes correspondant à l'attribut self.jeu'''
        return self.jeu

    def melanger(self): # utiliser le module random ...
        '''Mélange sur place les cartes de la liste des cartes associée au champ self.jeu'''
        random.shuffle(self.jeu)

    def distribuerCarte(self):
        ''' Cette fonction permet de distribuer une carte à un joueur. Elle retourne la carte
        Valeur retournée: Objet de type Carte '''
        return self.jeu.pop()

    def distribuerJeu(self, nbJoueurs, nbCartes):
        ''' Cette méthode distribue nbCartes à chacun des nbJoueurs, ... '''
        liste_cartes_distribuees = []
        liste_carte_one_player=[]

        if nbJoueurs*nbCartes > self.getTailleJeu() :
            print("Pas assez de cartes dans le jeu.")
            exit()
        
        else :
            for i in range(nbJoueurs):
                for j in range(nbCartes):
                    liste_carte_one_player.append(self.distribuerCarte())
                liste_cartes_distribuees.append(liste_carte_one_player)
                liste_carte_one_player = []
            return liste_cartes_distribuees
        


########################################################
############ Test de la classe JeuCartes ###############
########################################################
        
def testJeuCartes():
    
    jeu52 = JeuCartes(52)
    jeu52.melanger()

    L=jeu52.getJeu()
    carte= L[2] # la 3e carte
    print('Nom:', carte.getNom())
    print('Couleur:', carte.getCouleur())
    print('Valeur:', carte.getValeur())

    # Distribution de 4 cartes à 3 joueurs
    distribution_3j_4c = jeu52.distribuerJeu(3, 4)
    for i in range(3):
        print('\nJoueur', i+1, ':')
        listeCartes = distribution_3j_4c[i]
        for card in listeCartes:
            print(card.getNom(), 'de', card.getCouleur())

    # Distribution de 10 cartes à 6 joueurs pour générer une exception (6X10 > 52)
#    distribution_6_joueurs_10_cartes_par_joueur = jeu52.distribuerJeu(6, 10)