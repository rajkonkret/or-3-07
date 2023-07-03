wiek = 47
rok = 2023
temp = 36.6
wiek2 = 37.5

print(wiek2)
print(type(wiek2))  # <class 'float'> - zmiennoprzecinkowe

print(5 * "wiek")  # wiekwiekwiekwiekwiek

print(wiek + rok)
print(wiek * rok)
print(wiek - rok)
print(wiek / rok)  # wynik dzielenia zawsze float
print(wiek // rok)  # czesc całkowita z dzielenia
print(wiek ** rok)  # potegowanie
print(wiek % rok)  # modulo, czyli reszta z dzielenia
print(5 % 2)  # reszta 1 bo 2 * 2 = 4 + 1 = 5

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - (5 * 43) + (4 / 2 + 4) / 2)  # -158.0

print(0.2 + 0.8)  # 1.0 float
print(0.2 + 0.7)  # 0.8999999999999999

# typ logiczny
# True, False
czy_znasz_pythona = False
print(czy_znasz_pythona)  # False
print(type(czy_znasz_pythona))  # <class 'bool'> - logiczna
print(int(czy_znasz_pythona))  # int() - zamiana na liczby całkowite, 0 - False, 1 - True
czy_znasz_pythona = True
print(int(czy_znasz_pythona))  # 1 True

x = 1
print(bool(x))  # bool()  - zamiana (rzutowanie) na typ logiczny, True

x = 100
print(bool(x))  # True

x = -10
print(bool(x))  # True

x = 0
print(bool(x))  # False

x = 'radek'
print(bool(x))  # True

x = True  # None - nic
print(bool(x))  # False

x = ''
print(bool(x))  # False
x = []  # pusta lista
print(bool(x))  # False

print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

print(True or False)  # True
print(False or False)  # False
print(False or True)  # True
print(True or True)  # True

print(not False)  # True
print(not True)  # False
