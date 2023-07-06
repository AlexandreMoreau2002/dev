# les fonctions : randint ; choice ; shuffle de l'import (random) permet de selection ou
# generé un caractère aléatoire parmis une liste ou une plage d'entité

# créer des lancers de dé avec randint
"""from random import randint

# 1er tir :
print("Somme de 1 jet de 3 dés :")
print(randint(1,6) + randint(1,6) + randint(1,6))
print()
print()

# 2eme tir :
print("Somme d'un jet de 3 dés 50x :")
for x in range(50):
    print(randint(1,6)+randint(1,6)+randint(1,6), end=" ")
print()
print()

# 3eme tir :
print("Somme d'un jet de 3 dés 200x :")
for x in range(200):
    print(randint(1,6)+randint(1,6)+randint(1,6), end=" ")

"""
# pour faire des [] : alt + maj + 5 ou °

# créer des listes (et en sortir aléatoirement 6 caractères :
"""from random import choice

liste = ["a","b","c","d","e","f","j","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for bite in range(6):
    print(choice(liste), end=" ")"""

# choisir aléatoirement des données d'une liste avec choice:
"""from random import choice

liste = [1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,6,6,6]
for x in range(5):
    print(choice(liste), end=" ")"""

# un programme que génère un mot de passe de 8 caractères aléatoires, choisis parmi les 26 lettres minuscules et les 10 chiffres.
"""from random import choice

liste = ["a","b","c","d","e","f","j","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",1,2,3,4,5,6,7,8,9,0]
for y in range(8):
    print(choice(liste),end="")"""

# melanger des données d'une liste avec shuffle (créer une liste aléatoire numeroté):
"""from random import shuffle

liste = ['Wade Barrett', 'Daniel Bryan', 'Sin Cara', 'John Cena', 'Antonio Cesaro', 'Brodus Clay',
         'Bo Dallas', 'The Godfather', 'Goldust', 'Kane', 'The Great Khali', 'Chris Jericho',
         'Kofi Kingston', 'Jinder Mahal', 'Santino Marella', 'Drew McIntyre', 'The Miz', 'Rey Mysterio',
         "Titus O'Neil", 'Randy Orton', 'David Otunga', 'Cody Rhodes', 'Ryback', 'Zack Ryder',
         'Damien Sandow', 'Heath Slater', 'Sheamus', 'Tensai', 'Darren Young', 'Dolph Ziggler']
shuffle(liste)
for i in range(30):
    print(i+1,liste[i])"""

from random import sample

liste[' ']