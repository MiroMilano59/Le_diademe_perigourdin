from random import randint
from Monstre import *

class Heros:
    def __init__ (self, nom = "Hero", pt_vies_heros = 100, degat_max = 20, nb_potions = 3):
        self.nom = nom
        self.pt_vies_heros = pt_vies_heros
        self.nb_potions = nb_potions
        self.degat_max = degat_max
        self.liste_equipement = ["epee_magique", "diademe", "bouclier_miroir", "potion"]
        self.inventaire_hero = []

    def attaquer(self):
        degats_de_lattaque = randint(3,self.degat_max)
        if "epee_magique" in self.inventaire_hero:
            degats_de_lattaque = randint(15,30)
        return degats_de_lattaque

    def utiliser_potion(self):
        if "potion" in self.inventaire_hero:
            self.nb_potions += 1
        self.nb_potions -= 1
        self.pt_vies_heros += 50
        #print(f"tu as {self.pt_vies_heros} vies et il te reste {self.nb_potions} potions")

    def perdre_vie(self, degats):
        if "bouclier_miroir" in self.inventaire_hero:
            degats *= 0.8
        self.pt_vies_heros -= degats
        #print(f"tu as {self.pt_vies_heros} vies et il te reste {self.nb_potions} potions")

    def drop(self, monstre_afronte):
        if monstre_afronte <= 0:
            chance_drop = randint(1,20)
            if chance_drop <= 10:
                chance_drop_item = randint(0-1, len(self.liste_equipement))
                self.inventaire_hero.append(self.liste_equipement[chance_drop_item])
                self.liste_equipement.remove(self.liste_equipement[chance_drop_item])
                print(self.liste_equipement)
                print(self.inventaire_hero)
            else:
                pass

hero1 = Heros("Fred le borgne", 30, 18)
hero2 = Heros("Max l'ami des plantes", 20, 17)
hero3 = Heros("Will corps de crevette", 40, 20)
