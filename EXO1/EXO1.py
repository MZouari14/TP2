import random

def devine_le_nombre():
    # L'ordinateur choisit un nombre aléatoire entre 1 et 100
    nombre_a_deviner = random.randint(1, 100)

    nombre_devine = None
    essais = 0
    
    print("Bienvenue dans le jeu 'Devine le nombre' !")
    print("L'ordinateur a choisi un nombre entre 1 et 100.")
    
    # Boucle jusqu'à ce que l'utilisateur trouve le bon nombre
    while nombre_devine != nombre_a_deviner:
        try:
            # Demander à l'utilisateur d'entrer un nombre
            nombre_devine = int(input("Devinez le nombre : "))
            essais += 1
            
            # Donner des indices
            if nombre_devine < nombre_a_deviner:
                print("Trop petit ! Essayez encore.")
            elif nombre_devine > nombre_a_deviner:
                print("Trop grand ! Essayez encore.")
            else:
                print(f"Bravo ! Vous avez deviné le bon nombre ({nombre_a_deviner}) en {essais} essais.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            
###########################################################################################################################################################         
############################################################__Main__#######################################################################################
###########################################################################################################################################################              
# Lancer la fonction
devine_le_nombre()