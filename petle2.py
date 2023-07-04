dictionary = {'imie': 'Radek', 'nazwisko': 'kowalski'}

print(type(dictionary))  # <class 'dict'>

# wypisze klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

# wypisze wartosci
for v in dictionary.values():
    print(v)

for i in dictionary.items():
    print(i)  # ('nazwisko', 'kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)  # nazwisko => kowalski

dictionary2 = {'name': 'imie', 'company': 'Orange'}
print(dictionary2)  # {'name': 'imie', 'company': 'Orange'}

print({value: key for key, value in dictionary2.items()})
# {'name': 'imie', 'company': 'Orange'}
# {'imie': 'name', 'Orange': 'company'}

d2 = {}
for key, value in dictionary2.items():
    d2[value] = key

print(d2)  # {'imie': 'name', 'Orange': 'company'}

