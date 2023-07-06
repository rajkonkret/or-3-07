import pickle

lista = [1, 2, 3, 4, 5]

with open('test_lista.txt', 'w') as f:
    f.write(str(lista))

with open('test_lista.txt', 'r') as f:
    lines = f.read()

print(lines)  # [1, 2, 3, 4, 5]
print(type(lines))  # <class 'str'>
print(lines[0])  # [

with open('lista_pickle.log', 'wb') as file:
    pickle.dump(lista, file)

with open('lista_pickle.log', 'rb') as file:
    loaded_list = pickle.load(file)

print(loaded_list)
print(type(loaded_list))  # <class 'list'>
print(loaded_list[0])  # 1

data = {"name": "John", "age": 30, "city": "New York"}
with open('slownik_pickle.log', 'wb') as f:
    pickle.dump(data, f)

with open('slownik_pickle.log', 'rb') as f:
    data_loaded = pickle.load(f)

print(data_loaded)
print(type(data_loaded))  # <class 'dict'>
print(data_loaded['name'])  # John

data_list = [1, 2, 3, 4, 5]
data_dict = {"name": "John", "age": 30, "city": "New York"}

with open("data_pickle.log", 'wb') as f:
    pickle.dump(data_list, f)
    pickle.dump(data_dict, f)

with open('data_pickle.log', 'rb') as f:
    loaded_l = pickle.load(f)
    loaded_d = pickle.load(f)

print(loaded_l)
print(loaded_d)
# [1, 2, 3, 4, 5]
# {'name': 'John', 'age': 30, 'city': 'New York'}
print(type(loaded_d))  # <class 'dict'>

data_dict = {"name": "John", "age": 30, "city": "New York"}

serialized_data = pickle.dumps(data)
print(serialized_data)

deserialized_data = pickle.loads(serialized_data)
print(deserialized_data)  # {'name': 'John', 'age': 30, 'city': 'New York'}
print(type(serialized_data))  # <class 'bytes'>
print(type(deserialized_data))  # <class 'dict'>
