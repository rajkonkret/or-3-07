class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print("Jadę pojazdem")


class Car(Vehicle):
    def drive(self):
        print("Jadę samochodem")


class Bike(Vehicle):
    def drive(self):
        print("Jadę rowerem")


class HybridCar(Car, Bike):
    def drive(self):
        print("Jadę samochodem hybrydowym")
        super().drive()
        Bike.drive(self)


car1 = Car("polonez")
car1.drive()  # Jadę samochodem

rower = Bike("Romet")
rower.drive()  # Jadę rowerem

hyb = HybridCar("Toyota")
hyb.drive()  # Jadę samochodem hybrydowym
print(HybridCar.__mro__)
# (<class '__main__.HybridCar'>, <class '__main__.Car'>, <class '__main__.Bike'>,
# <class '__main__.Vehicle'>, <class 'object'>)
