# funkcje zwraccające wynik

def dodaj(a, b):
    return a + b  # return - zwroc wynik


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(5, 6))
print(dodaj(5, 6) + dodaj(8, 9))
print(oblicz_vat(1000))  # 1230.0
print(oblicz_vat(1000, 7))  # 1070.0
print(oblicz_vat(vat=15, cena=5000))  # 5750.0

zm = oblicz_vat(1000)
print(zm)  # 1230.0
print(type(zm))  # <class 'float'>

if zm == 1230:
    print("Prawidłowo")  # Prawidłowo

x = 3.1485
print(f"{x:.2f}")  # 3.15

x = 3.1485
y = 3.1415
a = x * 100
a = int(a)
print(a)
b = y * 100
b = int(b)
print(b)
print(a == b)  # True
print(x == y)  # False
print(round(x, 2))  # 3.15
print(round(y))  # 3
