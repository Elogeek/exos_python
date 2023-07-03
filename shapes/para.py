from rectangle import Rectangle


class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height

    # méthode qui calcul le volume
    def Volume(self):
        return self.length * self.width * self.height


my_rectangle = Rectangle(7, 5)
my_para = Parallelepipede(7, 5, 2)
print("Le périmètre de mon rectangle est : ", my_rectangle.Calculate_perimeter())
print("La surface de mon rectangle est : ", my_rectangle.Calculate_area())
print("Le volume de mon parallélépipède est : ", my_para.Volume())
