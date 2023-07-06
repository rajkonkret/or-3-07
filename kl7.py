class Animal:

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Imie: {self.name}")

    def wydaj_odglos(self):
        pass  # nic nie rób


class Dog(Animal):
    def __init__(self, name, rasa):
        super().__init__(name)
        self.rasa = rasa

    def wydaj_odglos(self):
        print("Hau Hau")

    def info(self):
        super().info()
        print(f"Rasa: {self.rasa}")


class Cat(Animal):
    def __init__(self, name, kolor):
        super().__init__(name)
        self.kolor = kolor

    def wydaj_odglos(self):
        print(f"Miau Miau")

    def info(self):
        super().info()
        print(f"Kolor: {self.kolor}")


class Tiger(Cat):
    def __init__(self, name, kolor, liczba_paskow):
        super().__init__(name, kolor)
        self.liczba_paskow = liczba_paskow

    def wydaj_odglos(self):
        print("Arr Arr")

    def info(self):
        super().info()
        print(f"Liczba pasków: {self.liczba_paskow}")


zwierzaak = Animal("Bezimienny")
zwierzaak.info()
zwierzaak.wydaj_odglos()  # pass

pies = Dog("Burek", "Kundel")
pies.info()
pies.wydaj_odglos()  # Hau Hau

kotek = Cat("Filemon", "Biały")
kotek.info()
kotek.wydaj_odglos()  # Miau Miau

tygrysek = Tiger("Rajah", "Pomorańćzowy", 15)
tygrysek.info()
tygrysek.wydaj_odglos()
# Imie: Rajah
# Kolor: Pomorańćzowy
# Liczba pasków: 15
# Arr Arr