# Classe rectangle
class Rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width

    # Méthode qui calcule le périmètre du rectangle
    def Calculate_perimeter(self):
        return 2*(self.length + self.width)

    # Méthode qui calcule la surface du rectangle
    def Calculate_area(self):
        return self.length * self.width


