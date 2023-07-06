# afficher la lettre C en python

for ligne in range(7):
    for colonne in range(5):
        if ((ligne==0 or ligne==6) and colonne>0) or (colonne==0) and (0 < ligne < 6):
            print("*",end=" ")
        else:
            print(end=" ")
    print(" ")