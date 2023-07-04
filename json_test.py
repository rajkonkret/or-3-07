# json - {"name":"Radek"}
# json - obiekt typu klucz-wartosc
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_aapli': None}
print(person_dict)  # {'name': 'Radek', 'age': 40, 'czy_aapli': None}
print(type(person_dict))  # <class 'dict'>

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {"name": "Radek", "age": 40, "czy_aapli": null}
# z indent=4
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_aapli": null
# }
# z sort_keys=True - zostały posortowane
# {
#     "age": 40,
#     "czy_aapli": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', 'r') as fh:
    data = json.load(fh)

print(data)  # {'age': 40, 'czy_aapli': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>
print(data['name'])  # Radek

print(data.keys())
print(data.values())
print(data.items())
# dict_keys(['age', 'czy_aapli', 'name'])
# dict_values([40, None, 'Radek'])
# dict_items([('age', 40), ('czy_aapli', None), ('name', 'Radek')])
