import random

def charger_mots():
    # Retourne une petite liste de mots par défaut
    return ["PYTHON", "CLAVIER", "RESEAU", "ROUTEUR"]

def choisir_mot(liste):
    # Choisit un mot au hasard dans la liste fournie
    return random.choice(liste)

def masque(mot):
    # Crée une liste contenant autant de '_' qu'il y a de lettres dans le mot
    resultat = []
    for i in range(len(mot)):
        resultat.append("_")
    return resultat