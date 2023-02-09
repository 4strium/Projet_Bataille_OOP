from random import *

class Main:
    """
    Représente une main d'un joueur de la bataille.
    """
    
    def __init__(self, etiquette = ''):
        self.cartes = []
        self.etiquette = etiquette
        
    def add_cartes(self, list_paquet):
        self.cartes = list_paquet
        
    def get_paquet(self):
        return self.cartes
    
    def inserer_une_carte(self, carte_a_inserer):
        index = randint(0, len(self.cartes))
        self.cartes.insert(index, carte_a_inserer)