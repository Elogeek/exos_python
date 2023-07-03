from math import *


class Circle:
    def __init__(self, a, b, rayon):
        self.a = a
        self.b = b
        self.rayon = rayon

    # Méthode qui calcule le périmètre du cercle
    def Calculate_perimeter(self):
        return 2 * pi * self.rayon

    # Méthode qui calcule la surface du cercle
    def Calculate_area(self):
        return pi * self.rayon ** 2

    def formEquation(self, x, y):
        return (x - self.a) ** 2 + (y - self.b) ** 2 - self.rayon ** 2

    # méthode qui permet de tester si un pointA(x,y) appartient ou non au cercle C
    def test_appartenance(self, x, y):
        if self.formEquation(x, y) == 0:
            print("le point : (", x, y, ") appartient au cercle C")
        else:
            print("le point : (", x, y, ") n'appartient pas au cercle C")


# Instanciation
C = Circle(1, 2, 1)

print("le périmètre du cercle C est  : ", C.Calculate_perimeter())
print("le surface du cercle C est  : ", C.Calculate_area())
C.test_appartenance(1, 1)
