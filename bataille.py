from jeucartes import *
from Player import *
import time

class Bataille:
    
    def __init__(self, NbJoueurs_Partie, nbCartes_paquet, nbCartes_par_player):
        self.nb_player = NbJoueurs_Partie
        self.nbCartes = nbCartes_paquet
        self.nbCartes_par_player = nbCartes_par_player
        self.list_player = {}
        self.generate_paquet()
        self.generate_player()
        self.distribuer_cartes()
     
    def generate_paquet(self):
        self.Jeu = JeuCartes(self.nbCartes)
        
    def generate_player(self):
        
        for i in range(self.nb_player):
            print("\nSaisissez le nom du joueur",i+1,":")
            name_of_player = str(input())
            self.list_player["Joueur {0}".format(i)] = Joueur(name_of_player, self.nbCartes_par_player)
                        
    def distribuer_cartes(self):
        self.Jeu.melanger() # On mélange entièrement le paquet
        distribution = self.Jeu.distribuerJeu(self.nb_player, self.nbCartes_par_player)
        
        for i in range(self.nb_player):
            self.list_player["Joueur {0}".format(i)].setMain(distribution[i])
            # Obtenir le paquet de cartes en main du joueur -> self.list_player["Joueur {0}".format(i)].getpaquet_Main()
    
    def Jouer(self):
        
        while True :
        
            tour_courant = {}
        
            for i in range(self.nb_player):
                tour_courant["Joueur {0}".format(i)] = self.list_player["Joueur {0}".format(i)].jouerCarte()
            
            carte_temp_one = list(tour_courant.values())[0]
            carte_temp_two = list(tour_courant.values())[1]
        
#        print(carte_temp_one.getNom())
#        print(carte_temp_one.getCouleur())
            print(carte_temp_one.getValeur())
        
#        print(carte_temp_two.getNom())
#        print(carte_temp_two.getCouleur())
            print(carte_temp_two.getValeur())
        
            if carte_temp_one.estSuperieureA(carte_temp_two) == True :
                self.list_player["Joueur 0"].insererMain(carte_temp_two)
            elif carte_temp_one.estInferieureA(carte_temp_two) == True :
                self.list_player["Joueur 1"].insererMain(carte_temp_one)
        
    def __str__(self):
        res = []
        res.append(self.list_player)
        return str(res)

partie0 = Bataille(2, 52, 5)
partie0.Jouer()