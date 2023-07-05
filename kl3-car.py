class Car:
    """
    Klasa samochod
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        # oznaczenie pola jako prywante - element enkapsulacji, hermetyzacji
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def licznik(self):
        print(f"Prędkość wynosi", self.__predkosc, "km/h")

    def hamuj(self):
        self.__predkosc -= 10
        self.licznik()

    def __zmien_bieg(self):
        print("Zmiana biegu")


car1 = Car("Fiat", 2023)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# print(car1.__predkosc)  # 50  AttributeError: 'Car' object has no attribute '__predkosc'.
# Did you mean: '_Car__predkosc'?
car1.licznik()  # Prędkość wynosi 50 km/h
# enkapsulacja - wystawienie metody do odczytu pola
car1.__predkosc = 100
car1.licznik()  # 50
print(car1.__predkosc)  # 100 bo tak naprawde odczytuje nowostworzone pole __predkośc niezalezne od pola obiektu
car1.licznik()  # Prędkość wynosi 50 km/h
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()  # Prędkość wynosi 0 km/h
print(car1.__predkosc)  # 100
