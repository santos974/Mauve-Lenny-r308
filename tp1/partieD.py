import partieC

def charger_scores():
    scores = {}
    try:
        fichier = open("scores.txt", "r")
        for ligne in fichier.readlines():
            parties = ligne.split(":")
            nom = parties[0].strip()
            victoires = float(parties[1].strip())
            scores[nom] = victoires
        fichier.close()
    except:
        pass
    return scores

def sauvegarder_scores(scores):
    fichier = open("scores.txt", "w")
    for nom, victoires in scores.items():
        fichier.write(nom + ":" + str(victoires) + "\n")
    fichier.close()

scores = charger_scores()
nom_joueur = input("Entrez votre nom : ")

if nom_joueur not in scores:
    scores[nom_joueur] = 0.0

rejouer = "o"

while rejouer == "o":
    # On utilise les fonctions du fichier partieC pour préparer le mot
    liste_mots = partieC.charger_mots()
    
    mode = input("Mode 2 joueurs ? (o/n) : ")
    if mode == "o":
        mot_secret = input("Joueur 1, entrez un mot pour votre voisin : ").upper()
        # On affiche 50 lignes vides pour cacher le mot
        for i in range(50):
            print("") 
    else:
        mot_secret = partieC.choisir_mot(liste_mots)
    
    mot_masque = partieC.masque(mot_secret)
    erreurs = 0
    lettres_deja_dites = []
    
    # Boucle du jeu (7 erreurs maximum)
    while erreurs < 7 and "_" in mot_masque:
        print("\nMot :", " ".join(mot_masque))
        print("Erreurs :", erreurs, "/ 7")
        
        lettre = input("Proposez une lettre : ").upper()
        
        if lettre in lettres_deja_dites:
            print("Vous avez déjà proposé cette lettre !")
        else:
            lettres_deja_dites.append(lettre)
            
            if lettre in mot_secret:
                # On remplace le '_' par la bonne lettre trouvée
                for i in range(len(mot_secret)):
                    if mot_secret[i] == lettre:
                        mot_masque[i] = lettre
            else:
                erreurs = erreurs + 1
                
    # Résultat de la partie
    if "_" not in mot_masque:
        print("\nGagné ! Le mot était", mot_secret)
        scores[nom_joueur] = scores[nom_joueur] + 1.0
    else:
        print("\nPerdu... Le mot était", mot_secret)
        
    print("Vos victoires :", scores[nom_joueur])
    sauvegarder_scores(scores)

    rejouer = input("\nRejouer ? (o/n) : ")