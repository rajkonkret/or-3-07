# krotka (tupla) - niezmienialna lista
# taka zmienna, niezmienna
tupla = ("radek",)  # nawiasy () nieobowiązkowe, przecinek obowiązkowy
print(type(tupla))  # <class 'tuple'>

tupl = "radek"  # str
print(type(tupl))  # <class 'str'>

tupla2 = "Tomek", "Asia", "Zbyszek", "Marcin"
print(tupla2)  # ('Tomek', 'Asia', 'Zbyszek', 'Marcin')
print(type(tupla2))  # <class 'tuple'>

tupla3 = (43, 55, 22.34, 11, 200)
print(type(tupla3))  # <class 'tuple'>
temp = 37, 5
print(type(temp))  # <class 'tuple'>

print(tupla2.count("Tomek"))
print(tupla2.index("Tomek"))

a, b = 1, 2
print(a)
print(b)

a, b = b, a
print(b)

a, *b = 1, 2, 3  # * worek na dane
print(a)  # 1
print(b)  # [2, 3]

# rozpakowania tupli
# ('Tomek', 'Asia', 'Zbyszek', 'Marcin')

imie1, imie2, *imie3 = tupla2
print(imie1)
print(imie2)  # ['Asia', 'Zbyszek']
print(imie3)  # ['Zbyszek', 'Marcin']

print(type(imie3))  # <class 'list'>

lista = list(tupla2)  # zamiana tupli na liste
print(lista)  # ['Tomek', 'Asia', 'Zbyszek', 'Marcin']
