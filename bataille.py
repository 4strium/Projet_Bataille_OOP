from jeucartes import *
from Player import *
import time

class Bataille:
    
    def __init__(self, nbCartes_paquet, nbCartes_par_player):
        self.nbCartes = nbCartes_paquet
        self.nbCartes_par_player = nbCartes_par_player
        self.generate_paquet()
        self.generate_player()
        self.distribuer_cartes()
     
    def generate_paquet(self):
        self.Jeu = JeuCartes(self.nbCartes)
        
    def generate_player(self):
        
        print("Saisissez le nom du joueur 1 :")
        name_of_player_1 = str(input())
        self.player1 = Joueur(name_of_player_1, self.nbCartes_par_player)
        print("\nSaisissez le nom du joueur 2 :")
        name_of_player_2 = str(input())
        self.player2 = Joueur(name_of_player_2, self.nbCartes_par_player)
        
                        
    def distribuer_cartes(self):
        self.Jeu.melanger() # On mélange entièrement le paquet
        distribution = self.Jeu.distribuerJeu(2, self.nbCartes_par_player)
        
        self.player1.setMain(distribution[0])
        self.player2.setMain(distribution[1])
    
    def Jouer(self):
        
        while True :
            
            if len(self.player1.getpaquet_Main()) == 0 :
                print("\n ---------- ", self.player2.getNom(), "a gagné, BRAVO A LUI !!!  ---------- ")
                exit()
            if len(self.player2.getpaquet_Main()) == 0 :
                print("\n ---------- ", self.player1.getNom(), "a gagné, BRAVO A LUI !!!  ---------- ")
                exit()
            
            pile_egalite = []
            carte_temp_one = self.player1.jouerCarte()
            carte_temp_two = self.player2.jouerCarte()
            
            print("\n ----- ",self.player1.getNom()," ----- ")
            print("Nombre de cartes dans sa main =",len(self.player1.getpaquet_Main())+1)
            print(carte_temp_one.getNom(),"de", carte_temp_one.getCouleur(), "Valeur =",carte_temp_one.getValeur())
            
        
            print("\n ----- ",self.player2.getNom()," ----- ")
            print("Nombre de cartes dans sa main =",len(self.player2.getpaquet_Main())+1)
            print(carte_temp_two.getNom(),"de", carte_temp_two.getCouleur(), "Valeur =",carte_temp_two.getValeur())
            
        
            if carte_temp_one.estSuperieureA(carte_temp_two) == True :
                self.player1.insererMain(carte_temp_one) # Il reprend sa carte
                self.player1.insererMain(carte_temp_two) # Il prend la carte gagnée !
            elif carte_temp_one.estInferieureA(carte_temp_two) == True :
                self.player2.insererMain(carte_temp_one) # Il prend la carte gagnée !
                self.player2.insererMain(carte_temp_two) # Il reprend sa carte
            elif carte_temp_one.egalite(carte_temp_two) == True :
                
                while carte_temp_one.egalite(carte_temp_two) == True :
                    pile_egalite.append(carte_temp_one)
                    pile_egalite.append(carte_temp_two)
                    
                    if len(self.player1.getpaquet_Main()) == 0 :
                        print("\n ---------- ", self.player2.getNom(), "a gagné, BRAVO A LUI !!!  ---------- ")
                        exit()
                    if len(self.player2.getpaquet_Main()) == 0 :
                        print("\n ---------- ", self.player1.getNom(), "a gagné, BRAVO A LUI !!!  ---------- ")
                        exit()
                    
                    carte_temp_one = self.player1.jouerCarte()
                    carte_temp_two = self.player2.jouerCarte()
                    
                    print("\n ----- ",self.player1.getNom()," ----- ")
                    print("Nombre de cartes dans sa main =",len(self.player1.getpaquet_Main())+1)
                    print(carte_temp_one.getNom(),"de", carte_temp_one.getCouleur(), "Valeur =",carte_temp_one.getValeur())
                    
                    print("\n ----- ",self.player2.getNom()," ----- ")
                    print("Nombre de cartes dans sa main =",len(self.player2.getpaquet_Main())+1)
                    print(carte_temp_two.getNom(),"de", carte_temp_two.getCouleur(), "Valeur =",carte_temp_two.getValeur())
                    
                
                if carte_temp_one.estSuperieureA(carte_temp_two) == True :
                    self.player1.insererMain(carte_temp_one) # Il reprend sa carte
                    self.player1.insererMain(carte_temp_two) # Il prend la carte gagnée !
                        
                    for i in range(len(pile_egalite)) :
                        self.player1.insererMain(pile_egalite[i])
                        # Il prend tout le paquet entassé depuis le début des égalités.
                        
                elif carte_temp_one.estInferieureA(carte_temp_two) == True :
                    self.player2.insererMain(carte_temp_one) # Il prend la carte gagnée !
                    self.player2.insererMain(carte_temp_two) # Il reprend sa carte
                    
                    for i in range(len(pile_egalite)) :
                        self.player2.insererMain(pile_egalite[i])
                        # Il prend tout le paquet entassé depuis le début des égalités.
                    
                           
            time.sleep(0.5) # Laisser le temps à l'utilisateur de voir les différents échanges
                

partie0 = Bataille(52, 6)
partie0.Jouer()