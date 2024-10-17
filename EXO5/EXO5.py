import random
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def obtenir_nombre_roulette():
    while True:
        try:
            nombre = int(input("Choisissez un nombre sur la roulette (entre 0 et 49) : "))
            if 0 <= nombre <= 49:
                return nombre
            else:
                print("Le nombre doit être compris entre 0 et 49.")
        except ValueError:
            logging.error("Veuillez entrer un nombre valide.", exc_info=True)
    

def obtenir_mise(joueur_argent):
    while True:
        try:
            mise = int(input(f"Combien voulez-vous miser ? Vous avez {joueur_argent}€ : "))
            if 0 < mise <= joueur_argent:
                return mise
            else:
                print(f"Votre mise doit être comprise entre 1 et {joueur_argent}€.")
        except ValueError:
            logging.error("Veuillez entrer un montant valide.", exc_info=True)


def calculer_gains(nombre_joueur, nombre_roulette, mise):
    if nombre_joueur == nombre_roulette:
        # Si le joueur a choisi le nombre exact
        return mise * 3
    elif nombre_joueur%2 == nombre_roulette%2:
        # Si le joueur a misé sur la même couleur
        return mise * 0.5
    else:
        # Si le joueur perd
        return 0


def Jeu_Casino():
    joueur_argent = 100  # Montant initial du joueur
    print("Bienvenue au ZCasino ! Vous commencez avec 100€.")
    
    while joueur_argent>0:
        # Nombre choisi par la roulette
        nombre_roulette = random.randint(0, 49)
        # Demander à l'utilisateur d'entrer un nombre
        nombre_joueur = obtenir_nombre_roulette()
        # Demander à l'utilisateur d'entrer sa mise
        mise = obtenir_mise(joueur_argent)
        # Calculer les gains du joueur
        joueur_argent = calculer_gains(nombre_joueur, nombre_roulette, mise)
        print('Il vous reste :', joueur_argent)
        # Demander à l'utilisateur si veut rejouer
        reponse = str(input("Voulez vous rejouer (o/n):")).lower()
        if reponse == 'o':
            if joueur_argent>0:
                mise = obtenir_mise(joueur_argent)
            else:
                print("Vous n'avez plus d'argent ! ")
        elif reponse == 'n':
            break
        else:
            print('Veuillez entrer une reponse valide !')

###########################################################################################################################################################         
############################################################__Main__#######################################################################################
###########################################################################################################################################################  
    
Jeu_Casino()        