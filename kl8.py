# klasa abstrakcyjna - taka klasa z ktorej nie mozna stworzyc obiektu
# dopiero z klasy dziedziczącej po klasie abstrakcyjnej tworzymy obiekt
from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "lecę z szybkością", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print(f"Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("kokokokokokoko")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


class Orzel(Ptak):
    def wydaj_odglos(self):
        print("piiiiiiiiii")

    def poluj(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")


# po dodaniu @abstractmethod
# TypeError: Can't instantiate abstract class Ptak with abstract method wydaj_odglos
# orz1 = Ptak("Orzeł", 20)
# orz1.latam()  # Tu Orzeł lecę z szybkością 20
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()

kur2 = Kura("Kura")
kur2.latam()  # Tu Kura Ja nie latam
kur2.wydaj_odglos()  # kokokokokokoko
kur2.dziobanie()  # Tu Kura Idę sobie podziobać


orz2 = Orzel("Orzel", 25)
orz2.wydaj_odglos()  # piiiiiiiiii
orz2.latam()
orz2.poluj()  # Tu Orzel Rozpoczynam polowanie
