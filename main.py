from random import randint
from unidecode import unidecode


def dico():
    fichier = open("liste_francais.txt", 'r')
    contenu_du_fichier = fichier.readlines()
    fichier.close()


    l_mots = []

    for mot in contenu_du_fichier:
        mot = mot.strip().lower()  # Supprimer les espaces et met en minuscules
        mot = unidecode(mot)  # Enlever les accents
        if len(mot) <= 6:  # Ajouter le mot uniquement s'il a 6 lettres ou moins
            l_mots.append(mot)

    return l_mots



def main():
    n_try = 6
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    contenu_du_fichier = dico()
    word_rand = word(contenu_du_fichier)

    while n_try != 0:
        saisie(word_rand, alphabet)
        n_try -= 1
    
    if n_try == 0:
        print("PERDU !!!")
    



def word(contenu_du_fichier):
    nb = randint(0, len(contenu_du_fichier) - 1)
    word = contenu_du_fichier[nb]
    return word

## termninale affichage saisie lance verif
def saisie(w, a):

    mots = len(w) - 1 #pour gérer le \0 si y en à un
    l_saisie = []
    l_play = []
    l_play.append(w[0])
    l_saisie.append(w[0])


    while mots != 0:

        for i in range(len(a)):
            print(a[i], " -- ", i)



        for i in range(len(w) - 1):
            l_play.append(".")

        print("GRID: ", l_play)

        print(w)
        for i in range(mots):
            print(l_saisie)
            num = int(input("\nséléctionner une lettre: "))
            l_saisie.append(a[num])
            mots -= 1

            for i in range(len(a)):
                print(a[i], " -- ", i)
            

            
            print("GRID: ", l_play)
        

        cor_place = verif(l_saisie, w, a)
        print(cor_place) # affiche liste element correct placé

            


def verif(l, w, a):
    print("---------")
    okk = len(w)
    correct_placement = []


    for j in range(len(w)):
        if l[j] == w[j]:
            okk -= 1
            correct_placement.append(l[j])
            print(f"{w[j]} est présent dans le mot à la bonne place.")
        elif okk == 0:
            print("Félicitations ! Vous avez gagné !")
            exit()  
        elif l[j] in w:
            print(f"{l[j]} est présent dans le mot mais mal placé.")
            correct_placement.append(".")
        else:
            print(f"{l[j]} n'est pas présent dans le mot.")
            if l[j] in a:
                a.remove(l[j])
                correct_placement.append(".")
    return correct_placement


main()

    
