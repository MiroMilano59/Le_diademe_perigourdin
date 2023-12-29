from random import *
from Heros import *

class Monstre:
    
    def __init__ (self, niveau, nom = "Monstre", pt_vies_monstre = 100):
        self.niveau = niveau
        self.nom = nom
        self.pt_vies_monstre = pt_vies_monstre

    def attaquer(self):
        degats_de_lattaque = randint(1,10)
        #print(degats_de_lattaque)
        return degats_de_lattaque
        

    def utiliser_potion(self):
        pass

    def perdre_vie(self, degats):
        self.pt_vies_monstre = self.pt_vies_monstre - degats
        # self.pt_vies_heros -= 1
        print(f"il reste {self.pt_vies_monstre} vies au {self.nom}")


monstre1 = Monstre(5)