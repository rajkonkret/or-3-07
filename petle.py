# for - petla iterujaca
import random

for i in range(10):  # 0..9
    print(i)

for i in range(10):
    pass  # nie rób nic

for _ in range(10):  # _ niema zmienna
    pass

for i in range(10):
    print(i * 2)

lista2 = list(range(1, 50))

for i in range(6):
    wyn = random.choice(lista2)
    lista2.remove(wyn)
    print(wyn)

for i in range(10):
    if i % 2 == 0:
        print(i, "jest parzysta")

# 0 jest parzysta
# 2 jest parzysta
# 4 jest parzysta
# 6 jest parzysta
# 8 jest parzysta

lista3 = [j for j in range(10) if j % 2 == 0]
lista4 = []
for j in range(10):
    if j % 2 == 0:
        lista4.append(j)

print(lista3)  # [0, 2, 4, 6, 8]
print(lista4)  # [0, 2, 4, 6, 8]

for c in lista4:
    if c == 2:
        c += 1  # c = c + 1
    print(c)  # 3

a = 1
a += 1  # a = a + 1
print(a)  # 2
a -= 1  # a = a - 1
print(a)  # 1
a *= 3  # a = a * 3
print(a)  # 3
a %= 2  # a = a % 2
print(a)  # 1
a /= 2  # a = a /2
print(a)  # 0.5 float

imiona = ['Radek', 'Asia', 'Zbyszek', 'Marcin']
for p in imiona:
    print(p)

# wypisac imiona z listy i odpowiadający im indeks
# 0 Radek
# 1 Asia

for i in range(len(imiona)):  # range(4) -> 0..3
    print(i, imiona[i])
# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Marcin

# enumerate - zwraca ponumerowana kolekcje
for p in enumerate(imiona):
    print(p)  # (0, 'Radek')

# a,b = (0, 'Radek')

for p, w in enumerate(imiona):
    print(p, w)  # 0 Radek

for p, w in enumerate(imiona):
    print(p, w, sep=";", end=" ")  # 0;Radek 1;Asia 2;Zbyszek 3;Marcin
# sep= - znak oddzielajacy elemnty po przecinku(domyslnie spacja)
# end= - znak konca lini (domyslnie enter (\n))

print()
ludzie = ['Radek', 'Zenek', 'Asia', 'Marcin', "Franek"]
wiek = [47, 67, 34, 32]

# for p, o in enumerate(ludzie):
#     print(p, o, wiek[p])  # IndexError: list index out of range
#
# łączy kolekcje i zwraca tuple
for k in zip(ludzie, wiek):
    print(k)  # ('Radek', 47)

for o, w in zip(ludzie, wiek):
    print(o, w)  # Radek 47

for p in enumerate(zip(ludzie, wiek)):
    print(p)  # (3, ('Marcin', 32))
# (3, ('Marcin', 32)) int, krotka)
for i, o in enumerate(zip(ludzie, wiek)):
    print(i, o)  # 3 ('Marcin', 32)
for i, (o, w) in enumerate(zip(ludzie, wiek)):
    print(i, o, w)  # 3 Marcin 32

jezyk = ['java', 'python']

for i, (o, w, j) in enumerate(zip(ludzie, wiek, jezyk)):
    print(i, o, w, j)  # 3 Marcin 32
# 0 Radek 47 java
# 1 Zenek 67 python