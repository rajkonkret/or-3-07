user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # float zmiennoprzecinkowe
liczba = 134567456234  # int

print("Witaj %s masz teraz %d lat" % (user, wiek))
# print("Witaj %s masz teraz %d lat" % (wiek, user))  # TypeError: %d format: a real number is required, not str
# ctrl d - powieanie linijki w której stoi kursor
# %s str
# %d digit

print('Witaj %(user)s, masz teraz %(age)d lat' % {'user': user, "age": wiek})
# Witaj Tomek, masz teraz 39 lat

print("Witaj {} masz teraz {} lat".format(user, wiek))  # Witaj Tomek masz teraz 39 lat
print("Witaj {} masz teraz {} lat".format(wiek, user))  # Witaj 39 masz teraz Tomek lat

print(f"Witaj {user}, masz teraz {wiek} lat")  # f - fstring, sformatowany tekst

print("Używamy wersji Pythona %i" % 3)  # Używamy wersji Pythona 3
print("Używamy wersji Pythona %f" % 3.9)  # Używamy wersji Pythona 3.900000
print("Używamy wersji Pythona %.1f" % 3.9)  # Używamy wersji Pythona 3.9
print("Używamy wersji Pythona %.2f" % 3.9)  # Używamy wersji Pythona 3.90
print("Używamy wersji Pythona %.0f" % 3.9)  # Używamy wersji Pythona 4
print("Używamy wersji Pythona %.f" % 3.9)  # Używamy wersji Pythona 4
# zero miejsc po przecinku, zaokrągla
x = 3.14
print("Zero miejsc po przecinku %.f" % x)
print("Orginalny x=", x)

print(f"Uzywamy wersji Pythona {wersja}")  # Uzywamy wersji Pythona 3.900001
print(f"Uzywamy wersji Pythona {wersja:.1f}")  # Uzywamy wersji Pythona 3.9
print(f"Uzywamy wersji Pythona {wersja:.0f}")  # Uzywamy wersji Pythona 4

print(f"{user:>10}")  # "     Tomek"
print(f"{user:>20}")  # "               Tomek"
print(f"{user:<30}")  # "Tomek                         "

print(liczba)  # 134567456234
print("Nasza duża liczba {:,}".format(liczba))  # Nasza duża liczba 134,567,456,234
print("Nasza duża liczba {:,}".format(liczba).replace(",", "."))  # Nasza duża liczba 134.567.456.234
print("Nasza duża liczba {:,}".format(liczba).replace(",", " "))  # Nasza duża liczba 134 567 456 234
print(f"Nasza duza liczba {liczba:,}")  # Nasza duza liczba 134,567,456,234


