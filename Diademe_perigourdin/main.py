from random import *
from Monstre import *
from Heros import *
# from Heros import *

# on demande au héros de choisir soit attaque, soit utiliser potion
# dans attaque : type attaque
# utilisation d'une seule potion à la fois

hero1 = Heros("Toto", 20)
#print(hero1.__dict__)
monstre1 = Monstre(5)

while hero1.pt_vies_heros > 0 :
    degats_du_monstre = monstre1.attaquer()
    hero1.perdre_vie(degats_du_monstre)

    #print(hero1.__dict__)

    degats_du_heros = hero1.attaquer()
    monstre1.perdre_vie(degats_du_heros)
    #print(monstre1.__dict__)

    #hero1.utiliser_potion()