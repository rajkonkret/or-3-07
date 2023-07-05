def odejmij2(a, b):
    return a - b


# lambda - wersja skrócona funkcji
odejmij = lambda a, b: a - b  # załozenia zwraca wynik (ma return)
print(odejmij(6, 7))

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))
# 1230.0
# 1070.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(8))
print(wiek(10))  # nastolatek
print(wiek(11))
print(wiek(18))  # dorosły
print(wiek(25))

lista = [1, 2, 3, 4, 8, 10, 23, 50]
l = []
for i in lista:
    l.append(i * 2)


def zmien(x):
    return x * 2


print(l)  # [2, 4, 6, 8, 16, 20, 46, 100]
print([i * 2 for i in lista])  # [2, 4, 6, 8, 16, 20, 46, 100]

# map() - mapowanie kolekcji, zamianie elementow w kolekcji na podstawie wskazanego działania
print(f"Zastosowanie map: {list(map(zmien, lista))}")  # Zastosowanie map: [2, 4, 6, 8, 16, 20, 46, 100]
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map: [2, 4, 6, 8, 16, 20, 46, 100]

# filter() - sprawdza warunek, gdy spełniony to zwraca ten element
print(f"Zastosowaanie filter: {list(filter(lambda x: x < 3, lista))}")  # Zastosowaanie filter: [1, 2]
print(f"Zastosowaanie filter: {list(filter(lambda x: x > 8, lista))}")
# x > 3 i x < 20
print(f"Zastosowaanie filter: {list(filter(lambda x: 3 < x < 20, lista))}")  # Zastosowaanie filter: [4, 8, 10]
# x > 3 and x < 20 -> 3 < x < 20
