# set, zbiór - przechowuje niezduplikowane elemnty
# tracimy kolejnosc przy dodawaniu elementow do seta

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

zb2 = set()
print(zb2)  # set()
zbior.add(33)  # add() - dodawanie lemntu do seta
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22}

# usuniecie ze zbioru pierwszego elementu
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22}
zbior.pop()
print(zbior)  # {777, 11, 44, 18, 22}

lista2 = list(zbior)  # zamiana zbioru na liste
print(lista2)  # [777, 11, 44, 18, 22]
print(type(lista2))  # <class 'list'>

zbior2 = {66, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)  # {66, 18, 52, 999, 11, 44, 62}

print(zbior | zbior2)  # suma zbiorow  {66, 999, 777, 11, 44, 18, 52, 22, 62} (or)
print(zbior & zbior2)  # częśc wspolna {18, 11, 44}  (and)
print(zbior - zbior2)  # różnica {777, 22}

print(zbior.difference(zbior2))  # {777, 22}
print(zbior2.difference(zbior))  # {66, 52, 62, 999}
