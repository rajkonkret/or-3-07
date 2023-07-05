# funkcja, ktora oblicza średnią

# a = 1, 2, 3
# i, *cyfry = a


def liczby(i=0, *cyfry):
    print(cyfry)
    print(type(cyfry))  # <class 'tuple'>, (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    suma = 0
    try:
        for c in cyfry:
            suma += c

        print(suma)
        count = len(cyfry)
        print(count)  # 0
        srednia = suma / count
    except Exception as e:
        print("Bład", e)
    else:  # gdy nie ma błedu
        print(f"Srednia dla ucznia {i} wynosi {srednia}")


liczby()
liczby(1, 2, 3)
liczby(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
liczby("1", 2, 3)  # Bład unsupported operand type(s) for +=: 'int' and 'str'
liczby("a", 2)  # Bład unsupported operand type(s) for +=: 'int' and 'str'
# 11:30