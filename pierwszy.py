print()  # wyswietlanie na ekranie wyswietl/wydrukuj
print("Nazywam się Radek")  # Nazywam się Radek
print('Nazywam się Radek')  # Nazywam się Radek
# PEP8 - dwie spacje po kodzie, znaczek #, i spacja odstepu i dopiero komentarz

# type() - wypisanie typu danych
print(type("RAdek"))  # <class 'str'>  - typ tekstowy
# ctrl alt l

print(39)
print(type(39))  # <class 'int'> - liczby całkowite

print("39" + "14")  # 3914 - konkatenacja, łaczenie tekstow
print(39 + 14)  # 53

print(5 * "4")  # 44444

imie: str = "Radek"  # str - tylko podpowiedź

print(imie)
print(type(imie))  # <class 'str'>

# imie = 48
print(imie)
print(type(imie))  # <class 'int'>

wiek = 48
print(wiek)
print(type(wiek))  # <class 'int'>

# print(imie + wiek)  # TypeError: can only concatenate str (not "int") to str
# ctrl /
# print(5 + "4")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(imie + str(wiek))
# str() - rutowanie na string, zamiana na typ string(tekstowy)

wiek = "Radek"
print(type(wiek))  # <class 'str'>
