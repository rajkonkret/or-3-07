import requests

url = 'https://randomuser.me/api/'

response = requests.get(url)
data = response.json()

print(data)
user = data['results'][0]
print(type(user))  # <class 'dict'>
print(user)
print("Imię:", user['name']['first'])
print("Nazwisko:", user['name']['last'])
print("Email", user['email'])
print("Zdjęcie")
photo_url = user['picture']['large']
response_photo = requests.get(photo_url)

with open("user_photo.jpg", 'wb') as f:
    f.write(response_photo.content)

print("Zdjęcie zapisane")
