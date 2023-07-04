while True:
    try:
        z = input("Podaj działanie + - * /")
        a = int(input("Podaj pierwsza liczbe"))
        b = int(input("Podaj druga liczbe"))

        match z:
            case "+":
                print(f"Wynik dodawania {a} + {b} = {a + b}")
            case "-":
                print(f"Wynik odejmowania {a} - {b} = {a - b}")

            case "*":
                print(f"Wynik mnożenia {a} * {b} = {a * b}")
            case "/":
                print(f"Wynik dzielenia {a} / {b} = {a / b}")
            case _:
                break
    except ZeroDivisionError:
        print("Dzielenie przez zero")
    except TypeError:
        print("Bład typu")
    except ValueError:
        print("Błąd wartości")
    except Exception as e:
        print("Bład", e)
    else:
        print("Nie ma błędu")
    finally:
        print("Zawsze")
# 11:25
