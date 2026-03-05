import random
from unidecode import unidecode
import os

# Assurez-vous que le chemin d'accès correspond à l'emplacement de votre fichier de mots.
os.chdir(r"c:\Users\M8 Sora\Downloads\sutom-main\sutom-main\SUTOM_v1")

def liste_mots():
    with open("liste_francais.txt", 'r') as fichier:
        contenu = fichier.readlines()
    return [unidecode(mot.strip().lower()) for mot in contenu if len(mot.strip()) <= 6]

def reponse_hypothetique(devinette, mot_secret):
    reponse = []
    mot_temp = list(mot_secret)
    for i, lettre in enumerate(devinette):
        if lettre == mot_secret[i]:
            reponse.append('correct')
            mot_temp[i] = None
        elif lettre in mot_temp:
            reponse.append('mal_place')
            mot_temp[mot_temp.index(lettre)] = None
        else:
            reponse.append('incorrect')
    return reponse

def filtre_mots(mots, premiere_lettre, positions_connues, mal_places, lettres_incorrectes, longueur_mot):
    mots_filtrés = []
    for mot in mots:
        if len(mot) != longueur_mot or not mot.startswith(premiere_lettre):
            continue
        valide = True
        for i, char in enumerate(mot):
            if positions_connues[i]:
                if positions_connues[i] != char:
                    valide = False
                    break
            elif char in lettres_incorrectes:
                valide = False
                break
            elif char in mal_places and i in mal_places[char]:
                valide = False
                break
        if valide:
            mots_filtrés.append(mot)
    return mots_filtrés

def devine_automatique(mot_secret, max_essais=6):
    mots = liste_mots()
    essais = 0
    positions_connues = [''] * len(mot_secret)
    positions_connues[0] = mot_secret[0]  # La première lettre est toujours correcte
    lettres_correctes = set([mot_secret[0]])
    mal_places = {}
    lettres_incorrectes = set()

    while essais < max_essais:
        mots_possibles = filtre_mots(mots, mot_secret[0], positions_connues, mal_places, lettres_incorrectes, len(mot_secret))
        devinette = random.choice(mots_possibles) if mots_possibles else random.choice([mot for mot in mots if mot.startswith(mot_secret[0]) and len(mot) == len(mot_secret)])

        reponse = reponse_hypothetique(devinette, mot_secret)
        print(f"Tentative {essais + 1}: {devinette} - Réponse: {reponse}")

        for i, (g, r) in enumerate(zip(devinette, reponse)):
            if r == 'correct':
                positions_connues[i] = g
            elif r == 'mal_place':
                mal_places[g] = {j for j in range(len(mot_secret)) if j != i}
            elif r == 'incorrect' and g not in positions_connues:
                lettres_incorrectes.add(g)

        essais += 1
        if all(r == 'correct' for r in reponse):
            print("Mot deviné correctement !")
            break
    else:
        print("Échec à deviner le mot.")

# Exemple d'utilisation
mot_aleatoire = random.choice([w for w in liste_mots() if len(w) == 5])  # Assure une longueur de mot cohérente
print("Mot secret:", mot_aleatoire)
devine_automatique(mot_aleatoire)
