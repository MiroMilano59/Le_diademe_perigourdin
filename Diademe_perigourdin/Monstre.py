from random import *

diademe = 0 

class Monstre:
    
    def __init__ (self, niveau, nom = "Monstre", pt_vies_monstre = 100):
        self.niveau = niveau
        self.nom = nom
        self.pt_vies_monstre = pt_vies_monstre

    def attaquer(self):
        if self.niveau == 1 or self.niveau == 3:
            degats_de_lattaque = randint(1,10)
        elif self.niveau == 2:
            degats_de_lattaque = randint(5,13)
        #print(degats_de_lattaque)
        return degats_de_lattaque
        

    def utiliser_potion(self):
        aleatoire = randint (0,100)
        if self.niveau == 3 and aleatoire > 25:
            attaquer(self)
        else:
            self.pt_vies_monstre += 10

    # def diademe(self):
    #     hasard = randint(0,100)
    #     if self.pt_vies_monstre =< 0 and hasard < 10:
    #         diademe += 1
    #         self.pt_vies_monstre in liste_de_monstres :
    #             self.pt_vies_monstre /= 2               

    def perdre_vie(self, degats):
        self.pt_vies_monstre = self.pt_vies_monstre - degats
        # self.pt_vies_heros -= 1
        print(f"il reste {self.pt_vies_monstre} vies au {self.nom}")


