import random

"""EXO 1"""

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
# Lancer la fonction
#devine_le_nombre()

"""EXO 2"""

def compter_mots_python():
    tentatives = 0
    max_tentatives = 3
    mot_a_compter = "python"
    
    while tentatives < max_tentatives:
        try:
            # Demander à l'utilisateur le nom du fichier
            nom_fichier = input("Entrez le nom du fichier .txt (avec extension) : ")

            with open(nom_fichier, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()
                
            # Convertir tout le texte en minuscule et compter les occurrences du mot "python"
            nombre_occurences = contenu.lower().count(mot_a_compter)

            print(f"Le mot '{mot_a_compter}' apparaît {nombre_occurences} fois dans le fichier '{nom_fichier}'.")
            return
        
        except FileNotFoundError:
            tentatives += 1
            print(f"Fichier introuvable. Tentative {tentatives} sur {max_tentatives}.")
    
    # Si les 3 tentatives échouent
    print("Erreur : échec de la lecture du fichier après 3 tentatives.")
    print("Le programme va se terminer.")

# Lancer la fonction
#compter_mots_python()

"""EXO 3"""

def Fizz_Buzz(N):
    if N%3 == 0 and N%5 == 0:
        print('Fizz Buzz')
    elif N%3 ==0:
        print("Fizz")
    elif N%5 == 0:
        print ("Buzz")
    else:
        print(N)
        
#Fizz_Buzz(15)   

"""EXO 4"""

def somme_harmonique(n):
    if n == 1:
        return 1
    else:
        return 1 / n + somme_harmonique(n - 1)

#n = 4
#resultat = somme_harmonique(n)
#print(f"La somme harmonique jusqu'au terme {n} est : {resultat}")

"""EXO 5"""

# input_user.py

def obtenir_nombre_roulette():
    while True:
        try:
            nombre = int(input("Choisissez un nombre sur la roulette (entre 0 et 49) : "))
            if 0 <= nombre <= 49:
                return nombre
            else:
                print("Le nombre doit être compris entre 0 et 49.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def obtenir_mise(joueur_argent):
    while True:
        try:
            mise = int(input(f"Combien voulez-vous miser ? Vous avez {joueur_argent}€ : "))
            if 0 < mise <= joueur_argent:
                return mise
            else:
                print(f"Votre mise doit être comprise entre 1 et {joueur_argent}€.")
        except ValueError:
            print("Veuillez entrer un montant valide.")

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
        
        
        
        
    
    
    

    