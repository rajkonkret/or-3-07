# wyjątki

# menu z operacjami
# pobrac typ operacji
# pobrac liczby
# wyswietlic wynik
# w petli while

while True:
    print(f"""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
""")

    odp = input("Podaj działąnie jakie chcesz wykonać")
    if odp == '5':
        break
    try:
        a = float(input("Podaj pierwszą liczbę"))
        b = float(input("Podaj drugą liczbę"))

        if odp == '1':
            print(f"Wynik dodawania {a} + {b} = {a + b}")
        elif odp == '2':
            print(f"Wynik odejmowania {a} - {b} = {a - b}")
        elif odp == '3':
            print(f"Wynik mnożenia {a} * {b} = {a * b}")
        elif odp == '4':
            print(f"Wynik dzielenia {a} / {b} = {a / b}")

        # Wynik dodawania 2 + 4 = 6
        else:
            print("Nie znam takiego działania")
    except ZeroDivisionError:
        print("Nie dzielimy przez zero")
    except ValueError:
        print("Bład wartości")
    except TypeError:
        print("Błąd typu")
    except Exception as e:
        print("Wystąpił błąd", e)
    # Wystąpił błąd division by zero
    else:
        print("Gdy nie ma błędu")
    finally:
        print("Zawsze")

try:
    print(2 / 0)  # ZeroDivisionError: division by zero
except ZeroDivisionError:
    print("Dzielenie przez zero")
