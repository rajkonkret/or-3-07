a = 10
b = 10


def dodaj():
    a = 6 # a i b sa lokalne, nie wpływja na globalne zmienne o tej samej nazwie
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)  # tu bierze zmienne globalne do obliczen


def dodaj3():
    global a  # zostaje uzyte a globalne(nie ma a lokalnego), nastepuje zmiana danych w globalnym a
    a = 6
    b = 7
    print(a + b)


print("Zmienna a z góry", a)  # Zmienna a z góry 10
dodaj()
print("Zmienna a z góry", a)  # Zmienna a z góry 10
dodaj2()
print("Zmienna a z góry", a)  # Zmienna a z góry 10

dodaj3()  # 13
print("Zmienna a z góry", a)  # Zmienna a z góry 6

