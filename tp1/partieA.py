def ajouter_etudiant(d, nom, note):
    try:
        # On essaie de convertir la note en nombre à virgule (float)
        d[nom] = float(note)
    except:
        print("Erreur : La note doit être un nombre.")

def moyenne_classe(d):
    if len(d) == 0:
        return 0.0
    
    total = 0
    # On additionne toutes les notes une par une
    for note in d.values():
        total = total + note
        
    return total / len(d)

def meilleur_etudiant(d):
    if len(d) == 0:
        return None
    
    meilleur_nom = ""
    meilleure_note = -1
    
    # On compare chaque note pour trouver la plus grande
    for nom, note in d.items():
        if note > meilleure_note:
            meilleure_note = note
            meilleur_nom = nom
            
    return (meilleur_nom, meilleure_note)

def sauvegarder_fichier(d):
    try:
        fichier = open("etudiants.txt", "w")
        for nom, note in d.items():
            fichier.write(nom + ":" + str(note) + "\n")
        fichier.close()
    except:
        print("Erreur lors de la sauvegarde.")

def charger_fichier():
    d = {}
    try:
        fichier = open("etudiants.txt", "r")
        lignes = fichier.readlines()
        fichier.close()
        
        for ligne in lignes:
            elements = ligne.split(":") # Sépare le nom et la note
            if len(elements) == 2:
                nom = elements[0].strip()
                note = float(elements[1].strip())
                d[nom] = note
    except:
        print("Fichier introuvable ou vide. Création d'un nouveau dictionnaire.")
    return d

# --- Test du programme ---
classe = charger_fichier()
ajouter_etudiant(classe, "Alice", 12)
ajouter_etudiant(classe, "Bob", 15)
ajouter_etudiant(classe, "Claire", 9.5)

print("Moyenne :", moyenne_classe(classe))
print("Meilleur :", meilleur_etudiant(classe))

sauvegarder_fichier(classe)