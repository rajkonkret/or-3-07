import json

with open('dane_json.json', 'r') as f:
    data = json.load(f)

print(data)
# {'squadName': 'Super hero squad', 'homeTown': 'Metro City', 'formed': 2016, 'secretBase': 'Super tower', 'active': True,
#  'members': [{'name': 'Molecule Man', 'age': 29, 'secretIdentity': 'Dan Jukes',
#               'powers': ['Radiation resistance', 'Turning tiny', 'Radiation blast']},
#              {'name': 'Madame Uppercut', 'age': 39, 'secretIdentity': 'Jane Wilson',
#               'powers': ['Million tonne punch', 'Damage resistance', 'Superhuman reflexes']},
#              {'name': 'Eternal Flame', 'age': 1000000, 'secretIdentity': 'Unknown',
#               'powers': ['Immortality', 'Heat Immunity', 'Inferno', 'Teleportation', 'Interdimensional travel']}]}

print(data['squadName'])
print(data['homeTown'])
print(data['formed'])
print(data['secretBase'])
print(data['active'])
print(data['members'])
# [{'name': 'Molecule Man', 'age': 29, 'secretIdentity': 'Dan Jukes',
#   'powers': ['Radiation resistance', 'Turning tiny', 'Radiation blast']},
#  {'name': 'Madame Uppercut', 'age': 39, 'secretIdentity': 'Jane Wilson',
#   'powers': ['Million tonne punch', 'Damage resistance', 'Superhuman reflexes']},
#  {'name': 'Eternal Flame', 'age': 1000000, 'secretIdentity': 'Unknown',
#   'powers': ['Immortality', 'Heat Immunity', 'Inferno', 'Teleportation', 'Interdimensional travel']}]
members = data['members']
print(type(members))  # <class 'list'>
print(members[0])
# {'name': 'Molecule Man', 'age': 29, 'secretIdentity': 'Dan Jukes',
#  'powers': ['Radiation resistance', 'Turning tiny', 'Radiation blast']}
memb0 = members[0]
print(type(memb0))  # <class 'dict'>
print(memb0['name'])
print(memb0['age'])
print(memb0['secretIdentity'])
print(memb0['powers'])  # ['Radiation resistance', 'Turning tiny', 'Radiation blast']
print(data['members'][0]['powers'][0])  # Radiation resistance
powers_memb0 = memb0['powers']
print(powers_memb0[0])  # Radiation resistance

