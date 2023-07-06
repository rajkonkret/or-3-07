import pickle


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


person = Person("John", 30)

with open('person.pickle', 'wb') as f:
    pickle.dump(person, f)

with open('person.pickle', 'rb') as f:
    loaded_person = pickle.load(f)

print(loaded_person.greet())  # Hello, my name is John and I am 30 years old.
