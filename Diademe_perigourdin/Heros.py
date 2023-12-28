from random import *

class Heros:
    nb_potions = 3
    def __init__ (self, nom = "Hero", pt_vies_heros = 100):
        self.nom = nom
        self.pt_vies_heros = pt_vies_heros

    def attaquer(self):
        degats_de_lattaque = randint(1,10)
        #print(degats_de_lattaque)
        return degats_de_lattaque

    def utiliser_potion(self):
        self.nb_potions -= 1
        self.pt_vies_heros += 50
        print(f"tu as {self.pt_vies_heros} vies et il te reste {self.nb_potions} potions")

    def perdre_vie(self, degats):
        self.pt_vies_heros -= degats
        # self.pt_vies_heros -= 1
        print(f"il te reste {self.pt_vies_heros} vies")

