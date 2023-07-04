# petla while
# petla sterowana warunkiem

licznik = 0

while True:  # pętla nieskończona
    licznik += 1
    print("Komunikat!")
    if licznik > 10:
        break  # przerwij tą pętle

print(licznik)
licznik = 0
while licznik < 10:
    print("komunika!")
    licznik += 1

lista = []  # pusta lista
lista2 = []
while True:
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))

print(lista)  # ['5', '6', '23', '45', '12', '11']
print(lista2)  # [5, 6, 7, 8, 23, 43, 12]
