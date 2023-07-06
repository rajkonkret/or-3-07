def kwadrat(n):
    for x in range(n):
        print(x ** 2)


def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # wykonaj operacje i zwroc wynik (return), zapamietuje miejsce gdzie skończył


kwadrat(5)
kwa = kwadrat2(5)  # tworzenie generatora(inicjacja)
print(type(kwa))  # <class 'generator'>

print(next(kwa))  # 0
print(next(kwa))  # 1
print(next(kwa))  # 4

print("wypisz cokolwiek")
print("zrób cokolwiek")
lista = []
lista.append("1234567800")
print(lista)

print(next(kwa))  # 9
print(next(kwa))  # 16


# print(next(kwa))  # StopIteration
def counter(start=0):
    n = start
    while True:
        yield n
        n += 1


def counter2(min=0):
    n = min
    while True:
        yield n
        n -= 1


c = counter()
print(next(c))
print(next(c))
print(next(c))
print(next(c))

c2 = counter2(10)
print(next(c2))
print(next(c2))
print(next(c2))
print(next(c2))


def counter3(start=0):
    n = start
    while True:
        result = yield n
        print(result)
        if result == 'q':
            break
        n += 1


c3 = counter3(10)
print(next(c3))
print(next(c3))
print(next(c3))

print(c3.send('OK'))  # OK
print(c3.send('q'))  # q
# print(next(c3))  # StopIteration
