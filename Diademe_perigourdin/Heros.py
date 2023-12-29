from random import randint
from Monstre import *

class Heros:
    def __init__ (self, nom = "Hero", pt_vies_heros = 100, nb_potions = 3):
        self.nom = nom
        self.pt_vies_heros = pt_vies_heros
        self.nb_potions = nb_potions

    def attaquer(self):
        degats_de_lattaque = randint(3,20)
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

    def diademe(self):


    def drop(self):
        liste_equipement = ["epee_magique", "diademe", "bouclier_miroir"]
        inventaire_hero = []
        if monstre1.perdre_vie == 0:
            chance_drop = randint(1,30)
            if chance_drop <= 10:
                chance_drop_item = randint(1, len(liste_equipement))

        elif 



hero1 = Heros("Fred le borgne")
hero2 = Heros("Max l'ami des plantes")
hero3 = Heros("Will corps de crevette")
