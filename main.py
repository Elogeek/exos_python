# Exercice 1: find divisor of an integer in python
n = int(input("Tapez la valeur de l'entier n "))
# Iterate through all integers less than or equal to n
for i in range(1, n+1):
    # Test if i is a divisor of n
    if (n % i == 0):
        print("Le nombre",i," est un diviseur de ",n)

# Exercice 2: multiplication tables

# Multiplication table of an integer entered on the keyboard
n = int(input("Tapez la valeur de n "))
print("La table de multiplication de", n, "est")
for i in range(1,10):
    print(i, "x", n, "=", i*n)

# Multiplication table of 1 -> 10
for n in range(1,11):
    # Separator insert
    print("*********")
    print("la table de multiplication de", n, "est")
    for i in range(1, 11):
        print(i, "x", n, "=", i*n)

# Exercice 3: the quotient and the remainder of the Euclidean division of a by b
a = int(input("Entrez le premier nombre entier:"))
b = int(input("Entrez le deuxième nombre entier:"))

# Calculate the quotient and remainder of Euclidean division
quotient = a // b
reste = a % b

# Show result
print("Le quotient de la division euclidienne de", a, "par", b, "est:", quotient)
print("Le reste de la division euclidienne de", a, "par", b, "est:", reste)

# Exercice 4: test if a number is prime
n = int(input("Tapez la valeur de n :  "))
# Trick: use a counter that counts the number of divisors of n
compteur = 0
for i in range(1, n + 1):
    if (n % i == 0):
        compteur = compteur + 1

# Tests if the number of divisors of n is = 2 to conclude that n is prime
if (compteur == 2):
    print("Le nombre ", n, "est premier")
else:
    print("Le nombre", n, "n'est pas premier")

# Exercice 5: browse a string
string = "Python is great"
for i in string:
    print(i)

# Exercice 6: character index within a string
# method 1
text = input("Entrez une phrase,svp : ")
letter_a = len(text)

for i in range(0,letter_a):
    # Check if the letter a is in the text
    if(text[i] == 'a'):
        print("La lettre 'a' se trouve à la position:", i , "dans cette chaine")

# method 2
text = input("Entrez une chaine de caractères : ")
has_a = False

for i, c in enumerate(text):
    # Check if the letter a is in the text
    if c == 'a':
        print(f"La lettre 'a' se trouve à la position : {i}")
        has_a = True

# Exercice 7 : displays words beginning with "a"
text = input("Entrez votre texte : ")
# Splits text into a list of words
words = text.split()
# Go through each word and check if it starts with "a"
words_start_a = []
for mot in words:
    if mot.startswith("a") or mot.startswith("A"):
       words_start_a.append(mot)

# Displays words starting with "a"
if len(words_start_a) > 0:
    print("Les mots commençant par 'a' sont :", words_start_a)
else:
    print("Il n'y a pas de mots commençant par 'a' dans votre texte.")
# Display a message if 'a' was not found
if not has_a:
    print("La chaine ne contient pas la lettre 'a'.")

# Exercise 8: Displays the first word of the text
#method 1
my_text = 'Python est un merveilleux langage de programmation'
# split text into words using space as a separator
mots = my_text.split()
premier_mot = mots[0]
print(premier_mot)

# method 2
my_text = 'Python est un merveilleux langage de programmation, mais je préfere PHP'
# Initialize a variable to store the first word
premier_mot = ''

for caractere in my_text:
    # If we encounter a space, we have finished reading the first word
    if caractere == ' ':
        break
    # Otherwise, we add the character to the first word
    premier_mot += caractere

# show the result
print(premier_mot)

# Exercice 9: remove duplicate items from the list
liste = [2, 7, 5, 2, 17, 13, 2, 7, 13]

# a function that removes duplicates from the list
def removeDuplicate(liste):
    # define and initialize list without duplicate element
    unique = []
    # construction of the list without duplicate elements
    for x in liste:
        if x not in unique:
            unique.append(x)
    return unique

print(removeDuplicate(liste))




