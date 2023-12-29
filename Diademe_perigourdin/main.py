from Monstre import *
from Heros import *


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

def diademe(heros_a_definir):
    if "diademe" in heros_a_definir.inventaire_hero :
        monstre_choisi.pt_vies_monstre /= 2


# on propose à l'utilisateur de choisir un héros
heros_choisi = choix_du_heros()

while heros_choisi.pt_vies_heros > 0 :
    monstre_choisi = monstre_du_combat() # on génère le monstre du combat de manière aléatoire
    diademe(heros_choisi)
    while monstre_choisi.pt_vies_monstre > 0 :
        if heros_choisi.pt_vies_heros <= 0 :
            print("game over")
            break
        else :
        # le monstre attaque
            print("attention à l'attaque !")
            degats_du_monstre = monstre_choisi.attaquer()
            heros_choisi.perdre_vie(degats_du_monstre)
            print(f"tu as {heros_choisi.pt_vies_heros} vies et il te reste {heros_choisi.nb_potions} potions")
            
        # on propose au héros le choix entre "attaquer" ou "prendre une potion"
            choix_attaque_ou_potion = input(f"que veux tu faire {heros_choisi.nom} ? \n 1) attaquer \n 2) prendre une potion (il t'en reste {heros_choisi.nb_potions})\n")
            if choix_attaque_ou_potion == "1" :
                degats_du_heros = heros_choisi.attaquer()
                monstre_choisi.perdre_vie(degats_du_heros)
            elif choix_attaque_ou_potion == "2" :
                heros_choisi.utiliser_potion()
            else : print("veuillez choisir une option")

    print(f"{monstre_choisi.nom} est mort")
    break


    
