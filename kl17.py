from kl16 import Person
import pickle

with open('dataclass.pickle', 'rb') as file:
    p = pickle.load(file)

print(p)  # [Person(first_name='Jacek', last_name='Kowalki', id=1), Person(first_name='Mateusz',
# last_name='Zegar', id=2)]
print(type(p))  # <class 'list'>

for person in p:
    person.greet()

# Witam, jestem Jacek Kowalki, Id to 1
# Witam, jestem Mateusz Zegar, Id to 2
# 13:15