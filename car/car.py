class Car:
    def __init__(self, brand, model, speed, engine):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.engine = engine

    def accelerate(self):
        self.speed += 20

    def show_speed(self):
        print(f"La vitesse de la voiture est de {self.speed} km/h.")


# Test
my_car = Car("Tesla", "Model S", 0, "électrique")
my_car.accelerate()
my_car.show_speed()

# Test 2
my_car.accelerate()
my_car.show_speed()
