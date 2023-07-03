import random

# random - generowanie liczb pseudolosowych

print(random.randint(1, 6))  # int 1..6
print(random.random())  # float 0..0.999999
print(random.random() * 6)  # float 0..5.999999
print(random.randrange(6))  # int 0..5
print(random.randrange(1, 6))  # 1..5 int

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))

lista2 = list(range(1, 50))  # 1..49
print(lista2)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
# 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))

wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)

print(random.choices(lista2, k=6))
# [38, 8, 24, 43, 36, 46]