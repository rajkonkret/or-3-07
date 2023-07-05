# dekoratory

def dekor(funk):
    def wew():
        print("Dekorujemy")
        print("Coś")
        return funk()  # wykonaj funkcje ktora pryzszła jako argument, return - odeslij wynik wykonania tej funkcji

    return wew


@dekor
def hej():
    print("Hej")


@dekor
def hej1():
    print("Ja nie jestem Hej :)")


hej()
hej1()
# Dekorujemy
# Coś
# Hej
# Dekorujemy
# Coś
# Ja nie jestem Hej :)
