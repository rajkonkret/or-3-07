# lista - kolekcja, przechowuje dowolną ilośc danych, moga byc przechowywane w jedej kolekcji rózne typy
# zachowuje kolejnosc dodawania

lista = []  # pusta lista
print(lista)  # []

lista.append("Radek")  # append() - dodawanie elementu do listy (na końcu)
lista.append("Maciek")
lista.append("JAśko")
lista.append('Zenek')

print(lista)  # ['Radek', 'Maciek', 'JAśko', 'Zenek']
# indeksy są numerowne od 0
print(lista[0])  # Radek
print(lista[2])  # JAśko
# print(lista[10])  # IndexError: list index out of range
print(len(lista))  # długosc 4 co oznacza, ze ostatni indeks = 3
print(lista[-1])  # Zenek
print(lista[-2])  # JAśko
print(lista[0:3])  # ['Radek', 'Maciek', 'JAśko'] indeksy 0,1,2 co oznacza, że 3 nie jest brany pod uwagę
print(lista[2:])  # ['JAśko', 'Zenek']
print(lista[:3])  # ['Radek', 'Maciek', 'JAśko']

# nadpisanie elementu o indeksie
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Zenek']

# wstawic element na indeks i rozszerzyc liste
lista.insert(1, "Marcin")
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Mikołaj', 'Zenek']

# usuniecie elemntu
lista.remove("Maciek")
print(lista)  # ['Radek', 'Marcin', 'Mikołaj', 'Zenek']

# usuniecie po indeksie

indeks = lista.index('Zenek')
print(indeks)
print(lista.pop(indeks))  # Zenek - zwraca usuniety elemnt i go usuwa
print(lista)  # ['Radek', 'Marcin', 'Mikołaj']

a = 1
b = 3
a = b
print(b)
a = 7
print(b)  # 3

lista3 = lista.copy()  # kopiowanie danych z jedej listy do drugiej
lista2 = lista  # kopiuje referencje czyli odnosnik do listy
print(lista)
print(lista2)
lista.clear()  # kasowanie danych z listy
print(lista)  # []
print(lista2)  # []
print(lista3)

liczby = [54, 999, 34, 22, 12.34, 687]
print(liczby)
print(type(liczby))  # <class 'list'>
liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 687, 999]

lista_osoby = ['radek', 'ola']
lista_osoby.sort()
print(lista_osoby)  # ['ola', 'radek']

liczby.reverse()
print(liczby)

liczby[3] = 6666
print(liczby)
print(liczby[0:3])  # [999, 687, 54]
print(liczby[-2])
print(liczby[0:-2])
print(liczby[-3:])  # [6666, 22, 12.34]

liczby.remove(54)
print(liczby)

print(liczby.pop(3))

print(len(liczby))  # 4
print(liczby)  # [999, 687, 6666, 12.34]

krotka = tuple(liczby)
print(krotka)  # (999, 687, 6666, 12.34)

# 13:30
