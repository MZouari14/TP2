
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


###########################################################################################################################################################         
############################################################__Main__#######################################################################################
###########################################################################################################################################################  

# Lancer la fonction
compter_mots_python()