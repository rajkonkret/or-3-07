names = ['Charles', 'Susan', 'Patrick', 'George']
new_list = [n for n in names]
print(new_list)  # ['Charles', 'Susan', 'Patrick', 'George']

n = [(a, b) for a in range(1, 3) for b in range(1, 3)]
print(n)  # [(1, 1), (1, 2), (2, 1), (2, 2)]

new_list_with_c = [n for n in names if n.startswith('C')]
print(new_list_with_c)  # ['Charles']

nums = [1, 2, 3, 4, 5, 6]
new_list_numbers = [num * 2 if num % 2 == 0 else num for num in nums]
print(new_list_numbers)

b = {"abc", "def"}
new_set = {s.upper() for s in b}  # {'DEF', 'ABC'}
print(new_set)

c = {"name": "Pooka", "age": 5}
new_dict = ["{}:{}".format(k.upper(), v) for k, v in c.items()]
print(new_dict)  # ['NAME:Pooka', 'AGE:5']

numbers = [1, 2, 3, 4, 5]
squred = [num ** 2 for num in numbers]
print(squred)

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # [2, 4]

even_odd = ['parzysta' if x % 2 == 0 else 'nieparzysta' for x in numbers]
print(even_odd)  # ['nieparzysta', 'parzysta', 'nieparzysta', 'parzysta', 'nieparzysta']

numbers2 = [-1, -2, 3, -4, -5]
absolute = [abs(x) for x in numbers2]
print(f"Wartości absolutne: {absolute}")  # Wartości absolutne: [1, 2, 3, 4, 5]

word = "Python"
letters = [letter for letter in word]
print(f"Literki: {letters}")
# Literki: ['P', 'y', 't', 'h', 'o', 'n']

lista1 = [word]
print(lista1)  # ['Python']

lista3 = []
lista3.append(word)
print(lista3)  # ['Python']

lista2 = list(word)
print(lista2)  # ['P', 'y', 't', 'h', 'o', 'n']
