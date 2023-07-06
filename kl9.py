# wilodiedziczenie
class A:
    def method(self):
        print("Metoda z kalsy A")


class B:
    def method(self):
        print("Metoda z klasy B")


class C(B, A):  # kolejnośc ważna
    """
    klasa C, dziedziczy po kalsie A i B
    """

    def method(self):
        print(f"Metoda z klasy C")  # Metoda z klasy C
        super().method()  # Metoda z klasy B
        A.method(self)  # Metoda z kalsy A
        # Metoda z klas C
        # Metoda z klasy B
        # Metoda z kalsy A


a = A()
a.method()

b = B()
b.method()

c = C()
c.method()  # Metoda z kalsy A
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>) dla C(B,A)  Metoda z klasy B
