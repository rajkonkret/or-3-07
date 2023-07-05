# funkcje
a = 6
b = 7


# te funkcje nie zwracają wyniku, tylko wyswietlają
# definicja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # funkcja z argumentami, obowiązkowe
    print(a + b)


def odejmij(a, b, c=0):  # c może byc przekazaywane, ale jak nie ma to jest domyślnie równe 0
    print(a - b - c)


def odejmij2(liczba1, liczba2):
    print(liczba1 - liczba2)


# wywołanie funkcji
dodaj()
dodaj2(4, 5)
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
odejmij(1, 2, 3)  # argumenty pozycyjne
odejmij(1, 2)
odejmij(b=5, a=8, c=9)  # -6, argumenty nazwane
odejmij2(liczba2=4, liczba1=5)
print(dodaj())  # None
# print(dodaj() + dodaj2(6, 7))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
