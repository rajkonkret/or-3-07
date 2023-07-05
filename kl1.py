# klasa - szablon opisujacy jakie cechy ma miec obiekt
# kalsa moze posiadac pola, funkcje
# obiekt

class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def podaj_wiek(self):
        print("Mam", self.wiek, "lat")


print(print.__doc__)  # dokumentacja
print(Human.__doc__)  # Klasa Human opisująca człowieka w pythonie

cz1 = Human()  # obiekt klasy Human
print(cz1)  # <__main__.Human object at 0x000001BAA29FCED0>
print(cz1.plec)  # . pr tabulator - automatycznie doda print
print(cz1.wiek)
print(cz1.imie)
cz1.imie = "Ania"
cz1.wiek = 26
print(cz1.plec)  # . pr tabulator - automatycznie doda print
print(cz1.wiek)
print(cz1.imie)
# k
# 26
# Ania
cz1.powitanie()  # Nazywam się Ania
cz1.podaj_wiek()  # Mam 26 lat

cz2 = Human()
cz2.imie = "Radek"
cz2.plec = "m"
print(cz2.imie)
print(cz2.plec)
cz2.powitanie()  # Nazywam się Radek
