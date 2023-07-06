# afficher la lettre o

for ligne in range(7):
    for colonne in range(5):
        if ((colonne == 0 or colonne == 4) and (0 < ligne < 6)) or ((ligne == 0 or ligne == 6) and (colonne > 0 and colonne < 4)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()


