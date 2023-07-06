# dziedziczenie

class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


class Samochod(Pojazd):  # Dziedziczymy po klasie Pojazd
    """
    Samochód
    """

    def __init__(self, kolor, marka):
        super().__init__(kolor)
        self.marka = marka

    def info(self):
        super().info()
        print(f"Marka: {self.marka}")


poj = Pojazd("Czerowny")
poj.info()
poj2 = Samochod("Biały", "Volvo")
poj2.info()
# Kolor: Czerowny
# Kolor: Biały
# Marka: Volvo
