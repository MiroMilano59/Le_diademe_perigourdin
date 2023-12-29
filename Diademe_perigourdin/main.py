from random import *
from Monstre import *
from Heros import *
# from Heros import *


# dans attaque : type attaque
# utilisation d'une seule potion à la fois

hero1 = Heros("Héros 1", 20)
hero2 = Heros("Héros 2", 100)
hero3 = Heros("Héros 3", 100)
#print(hero1.__dict__)
monstre1 = Monstre(5,"Monstre1", 100)

def choix_du_heros() :  # fonction permettant à l'utilisateur de choisir son héros
    choix_heros_nb = input(f"quel héros veux-tu choisir ? \n 1) {hero1.nom} \n 2) {hero2.nom} \n 3) {hero3.nom} \n ")
    if int(choix_heros_nb) == 1:
        choix_heros = hero1
    elif int(choix_heros_nb) == 2:
        choix_heros = hero2
    elif int(choix_heros_nb) == 3:
        choix_heros = hero3
    else : print("choisir un nombre entre 1 et 3 pour choisir le héros")
    print(f"salut à toi {choix_heros.nom} ! le combat démarre !")

    return choix_heros

# on propose à l'utilisateur de choisir un héros
heros_choisi = choix_du_heros()

while heros_choisi.pt_vies_heros > 0 :
    #monstre_du_combat = monstre_du_combat()
    monstre_du_combat = monstre1
    while monstre_du_combat.pt_vies_monstre > 0 :
        if heros_choisi.pt_vies_heros <= 0 :
            print("game over")
            break
        else :
        # le monstre attaque
            degats_du_monstre = monstre_du_combat.attaquer()
            heros_choisi.perdre_vie(degats_du_monstre)
        # on propose au héros le choix entre "attaquer" ou "prendre une potion"
            choix_attaque_ou_potion = input(f"que veux tu faire {heros_choisi.nom} ? \n 1) attaquer \n 2) prendre une potion (il t'en reste {hero1.nb_potions})\n")
            if choix_attaque_ou_potion == "1" :
                degats_du_heros = heros_choisi.attaquer()
                monstre_du_combat.perdre_vie(degats_du_heros)
            elif choix_attaque_ou_potion == "2" :
                heros_choisi.utiliser_potion()
            else : print("veuillez choisir une option")
            #print("ce combat est gagné !")
    print(f"{monstre_du_combat.nom} est mort")
    break

   

            
        
        
    #print(monstre1.__dict__)

    #
    # try:
    # except ValueError:
    #     print("Erreur: vous devez rentrer un chiffre entre 1 et 3")

    
