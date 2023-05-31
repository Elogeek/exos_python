# exo 1 : déterminer les diviseur d'un entier en python
n = int(input("Tapez la valeur de l'entier n "))
# parcourir tous les entiers inféreir ou égale à n
for i in range(1, n+1):
    # tester si i est un diviseur de n
    if (n % i == 0):
        print("Le nombre",i," est un diviseur de ",n)

# exo 2 : les tables de multiplication

# Table de multiplication d'un entier saisi au clavier
# Lire la valeur de l'entier n
n = int(input("Tapez la valeur de n "))
print("La table de multiplication de", n, "est")
for i in range(1,10):
    print(i, "x", n, "=", i*n)

#Table de multiplication de 1 -> 10
for n in range(1,11):
    #insert separator
    print("*********")
    print("la table de multiplication de", n, "est")
    for i in range(1, 11):
        print(i, "x", n, "=", i*n)

# exo 3 :  le quotient et le reste de la division euclidienne de a par b
# Demander à l'utilisateur de saisir les deux nombres entiers
a = int(input("Entrez le premier nombre entier:"))
b = int(input("Entrez le deuxième nombre entier:"))

# Calculer le quotient et le reste de la division euclidienne
quotient = a // b
reste = a % b

# Afficher le résultat
print("Le quotient de la division euclidienne de", a, "par", b, "est:", quotient)
print("Le reste de la division euclidienne de", a, "par", b, "est:", reste)

# exo 4 : tester si un nombre est premier
# Lire la valeur de l'entier n
n = int(input("Tapez la valeur de n :  "))
# on utilise un compteur qui compte le nombre de diviseurs de n
compteur = 0
for i in range(1, n + 1):
    if (n % i == 0):
        compteur = compteur + 1

# On teste si le nombre de diviseurs de n est = 2 pour conclure que n est premier
if (compteur == 2):
    print("Le nombre ", n, "est premier")
else:
    print("Le nombre", n, "n'est pas premier")
