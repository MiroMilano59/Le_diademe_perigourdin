from random import *
from Monstre import *
from Heros import *
# from Heros import *

# on demande au héros de choisir soit attaque, soit utiliser potion
# dans attaque : type attaque
# utilisation d'une seule potion à la fois

#print(hero1.__dict__)
hero1 = Heros("Fred le borgne")
monstre1 = Monstre(3)

variable = hero1
while hero1.pt_vies_heros > 0 :
    degats_du_monstre = monstre1.attaquer()
    variable.perdre_vie(degats_du_monstre)

    #print(hero1.__dict__)

    degats_du_heros = variable.attaquer()
    monstre1.perdre_vie(degats_du_heros)
    #print(monstre1.__dict__)
    monstre1.utiliser_potion()
    #hero1.utiliser_potion()
    def monstre_du_combat():
        generateur = randint(0,2)
        monstre_du_combat =  liste_de_monstres[generateur]
print (monstre_du_combat())
    
