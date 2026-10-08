import random

rejouer = "o"

while rejouer == "o":
    print("--- DEVINE LE NOMBRE ---")
    
    minimum = int(input("Entrez le nombre minimum : "))
    maximum = int(input("Entrez le nombre maximum : "))
    secret = random.randint(minimum, maximum)
    
    essais = 10
    gagne = False
    
    while essais > 0:
        print("Il vous reste", essais, "essais.")
        choix = int(input("Votre proposition : "))
        
        essais = essais - 1
        
        if choix < secret:
            print("Trop petit !")
        elif choix > secret:
            print("Trop grand !")
        else:
            print("Gagné !")
            gagne = True
            break # On sort de la boucle si on a gagné
            
    if gagne == False:
        print("Perdu... Le nombre secret était", secret)
        
    rejouer = input("Voulez-vous rejouer ? (o/n) : ")