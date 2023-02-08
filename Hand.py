
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