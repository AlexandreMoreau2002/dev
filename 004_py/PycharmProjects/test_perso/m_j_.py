
# M
for ligne in range(6):
    for colonne in range(6):
        if (colonne==0 or colonne==5) or (ligne+colonne==5 and ligne<3)or (colonne-ligne==0 and ligne<3):
            print("*", end=" ")
        else:
            print(end="  ")
    print()


# J
for ligne in range(7):
    for colonne in range(5):
        if (colonne==3 and (0 < ligne < 6)) or (ligne==6 and (0 < colonne <3)) or (colonne==0 and ligne==5) or (ligne==0 and (1 < colonne < 5)):
            print("*", end=" ")
        else:
            print(end="  ")
    print()