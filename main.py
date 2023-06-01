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

# exo 5: parcourir une chaine
string = "Python is great"
# Parcoure les caractères de la chaîne
for i in string:
    print(i)

#exo 6: index de caractère au sein d'une chaine
# method 1
text = input("Entrez une phrase,svp : ")
letter_a = len(text)

for i in range(0,letter_a):
    # check si la lettre a est dans le texte
    if(text[i] == 'a'):
        print("La lettre 'a' se trouve à la position:", i , "dans cette chaine")

# method 2
text = input("Entrez une chaine de caractères : ")
has_a = False

for i, c in enumerate(text):
    # Vérifier si 'a' est là
    if c == 'a':
        print(f"La lettre 'a' se trouve à la position : {i}")
        has_a = True

# Afficher un message si 'a' n'a pas été trouvé
if not has_a:
    print("La chaine ne contient pas la lettre 'a'.")

# exo 7: affiche le 1 mot du texte

#method 1
my_text = 'Python est un merveilleux langage de programmation'
# On divise le texte en mots en utilisant l'espace comme séparateur
mots = my_text.split()
premier_mot = mots[0]
print(premier_mot)

# method 2
my_text = 'Python est un merveilleux langage de programmation, mais je préfere PHP'
# initialise une variable pour stocker le premier mot
premier_mot = ''

for caractere in my_text:
    # Si on rencontre un espace, on a fini de lire le premier mot
    if caractere == ' ':
        break
    # Sinon, on ajoute le caractère au premier mot
    premier_mot += caractere

# On affiche le résultat
print(premier_mot)

# exo 8: supprimer les éléments duppliquées de la liste
liste = [2, 7, 5, 2, 17, 13, 2, 7, 13]
# définit une fonction qui supprime les doublons dans la liste
def removeDuplicate(liste):
    # définir et initialiser la liste sans élément dupliqué
    unique = []
    # construction de la liste sans éléments dupliqués
    for x in liste:
        if x not in unique:
            unique.append(x)
    return unique

print(removeDuplicate(liste))

