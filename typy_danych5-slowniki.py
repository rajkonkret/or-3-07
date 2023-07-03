# słownik - para klucz wartosc  {"name" : "Radek} {"klucz":"wartość"}

dict = {}  # pusty słownik
print(dict)  # {}
print(type(dict))  # <class 'dict'>

dict['imie'] = "Radek"
print(dict)  # {'imie': 'Radek'}

dict['wiek'] = 39
print(dict)  # {'imie': 'Radek', 'wiek': 39}

print(dict.keys())
print(dict.values())
print(dict.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 39])
# dict_items([('imie', 'Radek'), ('wiek', 39)])

dict.update({'date': '12-12-2023'})
print(dict)  # {'imie': 'Radek', 'wiek': 39, 'date': '12-12-2023'}

dictionary = {'x': 2}
dictionary.update([('y', 3), ('z', 0)])
print(dictionary)  # {'x': 2, 'y': 3, 'z': 0}

dict2 = {'imie': 'name', 'kot': 'cat'}
print(dict2['imie'])  # name
# wypisze słowka jakie ma słowniku
# pobierze od uzytkownika słówko do przetłumaczenia
# wypisze przetłumaczenie

print("Mamy w słowniku", dict2.keys())
key = input("Podaj słówko do przetłumaczenia")
# input() - pobiera dane np.: z klawiatury
# zwraca str()

print(dict2[key.lower().replace(" ", "")])

# input zwraca stringa
a = input("Podaj pierwszą liczbe")
b = input("Podaj druga liczbe")
print(int(a) + int(b))  # int() - rzutowanie, zamiana na int
