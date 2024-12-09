from random import randint

fichier = "./liste_filtree.txt"
liste = []

def piche_mot():
    return liste[randint(0, len(liste) - 1)].replace("\n", "")

def constructeur_indice(mot, coup = ""):
    if coup == "":
        indice = mot[0]
        for j in range(len(mot) - 1):
            indice += " _"
    else:
        indice = ""
        for i in range(len(mot)):
            if mot[i] == coup[i]:
                indice += "\033[0;32m" + coup[i] + "\033[0;32m"
            elif coup[i] in mot:
                indice += "\033[0;33m" + coup[i] + "\033[0;33m"
            else: 
                indice += "\033[0;31m" + coup[i] + "\033[0;31m"
    return (indice + "\033[0m")

def jeu(nbMots = 1):
    global liste
    motsTrouves = 0
    coupsMax = 6
    for i in range(nbMots):
        mot = piche_mot()
        indice = constructeur_indice(mot)
        print(indice)
        print("Vous avez " + str(coupsMax) + " coups pour trouver le mot. Celui-ci a une longueur de " + str(len(mot)) + " lettres.")
        coup = ""
        nbCoups = 0
        while coup != mot and nbCoups < coupsMax:
            coup = ""
            while len(coup) != len(mot) or coup+"\n" not in liste:
                if len(coup) > 0:
                    if len(coup) != len(mot):
                        print("La longueur du mot ne correspond pas.")
                    elif coup+"\n" not in liste:
                        print("Le mot n'est pas reconnu")
                coup = input()
            indice = constructeur_indice(mot, coup)
            print(indice)
        if coup == mot:
            print("Bien joué! Tu as trouvé le mot.")
            motsTrouves += 1
        else:
            print("Le mot était: " + mot)
    print("Partie terminée!\nTu as trouvé " + str(motsTrouves) + "/" + str(nbMots) + " mots")

def main():
    fin = False
    global fichier
    global liste
    liste = open(fichier, 'r', encoding="utf-8").readlines()
    while not fin:
        print("           .---.                              ,--,              \n" + 
                "          /. ./|                       ,---,,--.'|              \n" + 
                "      .--'.  ' ;   ,---.    __  ,-.  ,---.'||  | :              \n" +
                "     /__./ \\ : |  '   ,'\\ ,' ,'/ /|  |   | ::  : '              \n" +
                " .--'.  '   \' . /   /    |'  | |' |  |   | ||  ' |      ,---.   \n" +
                "/___/ \\ |    ' '.   ; ,. :|  |   ,',--.__| |'  | |     /     \\  \n" +
                ";   \\  \\;      :'   | |: :'  :  / /   ,'   ||  | :    /    /  | \n" +
                " \\   ;  `      |'   | .; :|  | ' .   '  /  |'  : |__ .    ' / | \n" +
                "  .   \\    .\\  ;|   :    |;  : | '   ; |:  ||  | '.'|'   ;   /| \n" +
                "   \\   \\   ' \\ | \\   \\  / |  , ; |   | '/  ';  :    ;'   |  / | \n" +
                "    :   '  |--\"   `----'   ---'  |   :    :||  ,   / |   :    | \n" +
                "     \\   \\ ;                      \\   \\  /   ---`-'   \\   \\  /  \n" +
                "      '---\"                        `----'              `----'   ")
        print("[ 1 ] Mot simple\n[ 2 ] Suite de mots\n[ 0 ] Quitter")
        rep = input()
        match rep:
            case "1":
                jeu()
            case "2":
                print("Combien de mots souhaitez-vous deviner ?")
                nbMots = input()
                jeu(int(nbMots))
            case "0":
                fin = True
    
main()