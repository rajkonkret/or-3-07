# warunki - instrukcje sterowania przepływem programu
# if

odp = True

if odp:
    print("Brawo")  # wcięcie obowiązkowe, warunek spełniony
else:
    print("Musisz sie dalej uczyć")  # w przeciwnym przypadku

print("Dalsza częśc programu")

# podatek = 0.0
# zarobki = int(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:  # kolejny warunek
#     podatek = 0.2
# elif zarobki < 100000:  # kolejny warunek
#     podatek = 0.4
# else:
#     podatek = 0.6
# # kolejnośc warunków jest ważna
# print(f"Zapłacisz {podatek * zarobki} zł")

suma_zam = 150
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0
print(f"Rabat wynosi {rabacik}")

rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabat}")
# Rabat wynosi 25
# Rabat wynosi 25
# 14:50

lista_bledow = []
alert_system = 'dysk'
error = 'dowolny'

error_message = "Stało się coś strasznego"

if alert_system == 'console':  # == porównanie
    print(error_message)
elif alert_system == "email":
    lista_bledow.append('email')
    if error == 'medium':
        lista_bledow.append("ostrzezenie")
    elif error == 'critical':
        lista_bledow.append("krytyczny")
    else:
        lista_bledow.append("inny")
else:
    print("System nieznany")

print(lista_bledow)  # ['email', 'inny']

a = 14
b = 3

print(f"Wynik porównania {a} > {b}: {a > b}")
print(f"Wynik porównania {a} < {b}: {a < b}")
print(f"Wynik porównania {a} == {b}: {a == b}")  # czy równe
print(f"Wynik porównania {a} != {b}: {a != b}")  # czy różne
# Wynik porównania 14 > 3: True
# Wynik porównania 14 < 3: False
# Wynik porównania 14 == 3: False
# Wynik porównania 14 != 3: True

# napisac test z historii
# wyswietlic pytanie
# pobrac odpowiedz
# wyswietlic wynik(czy odpowiedz prawwidłowa)

odp = input("podaj datę Chrztu Polski")
if odp == '966':
    print("Prawidłowa odpowiedź")
else:
    print("Masz w ksiazce na stronie 23")
