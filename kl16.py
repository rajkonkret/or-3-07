# dataclass - dla klass przechowujacych dane sam generuje techniczne metody
import pickle
from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    id: int

    def greet(self):
        print(f"Witam, jestem {self.first_name} {self.last_name}, Id to {self.id}")


# p0 = Person()  # <__main__.Person object at 0x0000020040BFACD0>
# print(p0)

if __name__ == '__main__':  # main ogranicza wykonanie kodu tylko gdy jest bezposrednio uruchomiony plik
    p1 = Person("Jacek", "Kowalski", 1)
    print(p1)
    # Person(first_name='Jacek', last_name='Kowalski', id=1)  __str__, __repr__

    p2 = Person(1, "Jacek", "kowalski")
    print(p2)
    p1.greet()

    people = [
        Person("Jacek", "Kowalki", 1),
        Person("Mateusz", "Zegar", 2)
    ]

    with open("dataclass.pickle", 'wb') as stream:
        pickle.dump(people, stream)
