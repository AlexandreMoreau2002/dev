poids = input("ton poids mon gros (en kg) ?")
taille = input("ta taille mgl (en m) ?")

poids = float(poids)
taille = float(taille)

taille_au_carré = taille * taille
imc = poids / taille_au_carré

print("votre imc est de : " + str(imc))

