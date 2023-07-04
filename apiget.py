import requests as re

url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'
response = re.get(url)
print(response)
# <Response [200]> - ok
# 3XX - posrednie błedy
# 4xx - grube błedy, 404 -brak zasobu, 400 bad request
# 5xxx - błedy wewnetrzne serwera np.: json nieprawidłowy

table = response.json()
print(table)
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
#  'rates': [{'no': '127/A/NBP/2023', 'effectiveDate': '2023-07-04', 'mid': 4.4273}]}
print(table['table'])
print(table['currency'])
print(table['code'])
print(table['rates'])  # [{'no': '127/A/NBP/2023', 'effectiveDate': '2023-07-04', 'mid': 4.4273}]
print(type(table['rates']))  # <class 'list'>
print(table['rates'][0])  # {'no': '127/A/NBP/2023', 'effectiveDate': '2023-07-04', 'mid': 4.4273}
print(table['rates'][0]['no'])
print(table['rates'][0]['effectiveDate'])
print(table['rates'][0]['mid'])
# 127/A/NBP/2023
# 2023-07-04
# 4.4273

