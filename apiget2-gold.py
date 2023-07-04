from pprint import pprint

import requests as re

url = 'http://api.nbp.pl/api/cenyzlota'
response = re.get(url)
print(response)
# <Response [200]> - ok
# 3XX - posrednie błedy
# 4xx - grube błedy, 404 -brak zasobu, 400 bad request
# 5xxx - błedy wewnetrzne serwera np.: json nieprawidłowy

table = response.json()
print(table)
# <Response [200]>
# [{'data': '2023-07-04', 'cena': 252.47}]
print(f"Data {table[0]['data']}, cena {table[0]['cena']}")  # Data 2023-07-04, cena 252.47

url2 = 'http://api.nbp.pl/api/cenyzlota/last/5'
response = re.get(url2)
print(response)
gold_last = response.json()
print(gold_last)
# [{'data': '2023-06-28', 'cena': 249.73}, {'data': '2023-06-29', 'cena': 249.85},
# {'data': '2023-06-30', 'cena': 249.36},
#  {'data': '2023-07-03', 'cena': 252.47}, {'data': '2023-07-04', 'cena': 252.47}]
for item in gold_last:
    print(item)
# {'data': '2023-06-28', 'cena': 249.73}
# {'data': '2023-06-29', 'cena': 249.85}
# {'data': '2023-06-30', 'cena': 249.36}
# {'data': '2023-07-03', 'cena': 252.47}
# {'data': '2023-07-04', 'cena': 252.47}

pprint(gold_last)  # ładniej wyswietla dane
# [{'cena': 249.73, 'data': '2023-06-28'},
#  {'cena': 249.85, 'data': '2023-06-29'},
#  {'cena': 249.36, 'data': '2023-06-30'},
#  {'cena': 252.47, 'data': '2023-07-03'},
#  {'cena': 252.47, 'data': '2023-07-04'}]
