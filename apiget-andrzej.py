import requests
import requests.utils

url = 'http://localhost:5000/users'

response = requests.get(url)
print(response)
data = response.json()
print(data)
print(type(data))
print(data['name'])
print(data['email'])
# <class 'dict'>
# radek@wp.pl
# radek@wp.pl
