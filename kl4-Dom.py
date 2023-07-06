class Dom:
    """
    klasa opisująca Dom
    """

    def __init__(self, metraz, kolor, liczba_okien):  # __init__ konstruktor
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def podaj_kolor(self):
        print(f"Mamy kolor {self.__kolor}")

    def zmien_kolor(self):
        wybor = input("Podaj nowy kolor")
        self.__kolor = wybor
        self.podaj_kolor()
        self.__farba()

    def podaj_metraz(self):
        print(f"Mamy metraż {self.__metraz}")

    def zmien_metraz(self):
        wybor = int(input("Podaj nowy metraż"))
        self.__metraz = wybor
        self.podaj_metraz()

    def podaj_okna(self):
        print(f"Mamy metraż {self.__liczba_okien}")

    def zmien_okna(self):
        wybor = int(input("Podaj liczbę okien"))
        self.__liczba_okien = wybor
        self.podaj_okna()

    def __farba(self):
        print("Skończyłą się farba", self.__kolor)


dom1 = Dom(500, "biały", 8)
dom1.podaj_metraz()
dom1.podaj_okna()
dom1.podaj_kolor()
# Mamy metraż 500
# Mamy metraż 8
# Mamy kolor biały
dom1.zmien_metraz()
# Podaj nowy metraż456
# Mamy metraż 456
dom1.zmien_kolor()
# Podaj nowy kolorzółty
# Mamy kolor zółty
# Skończyłą się farba zółty
