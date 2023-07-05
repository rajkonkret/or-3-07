class Human:
    """
    Klasa Human opisująca człowiek a w Pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec='k'):  # tzw konstruktor
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def podaj_wiek(self):
        print("Mam", self.wiek, "lat")

    def moj_wzrost(self):
        print("Mam", self.wzrost, "cm wzrostu")

    def ruszaj(self):
        if self.plec == 'm':
            print("Ruszyłem w drogę")
        else:
            print("Ruszyłąm w drogę")


# cz1 = Human()  # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Radek", 80, 180, "m")  # konstruktor z argumentami
print(cz1.imie)
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.plec)
cz1.powitanie()
cz1.podaj_wiek()  # Mam 80 lat
cz1.moj_wzrost()
cz1.ruszaj()  # Ruszyłem w drogę

cz2 = Human("Ania", 34, 168)
print(cz2.plec)
cz2.ruszaj()
cz2.moj_wzrost()
cz2.podaj_wiek()