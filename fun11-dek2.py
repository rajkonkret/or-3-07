def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper  # bez nawiasów, bo chemy zwrocic funkcje a nie wynik wykonania funkcji


def bold_decorator(func):
    def wrapper():
        result = func()
        return "\033[1m" + result + "\033[0m"

    return wrapper


@bold_decorator
@uppercase_decorator
def greeting():
    return "Hello World"


print(greeting())  # HELLO WORLD  "HELLO WORLD"
