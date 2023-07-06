import requests
import xml.etree.ElementTree as ET

url = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=xml'

response = requests.get(url)
print(response)

xml_data = response.content
print(xml_data)

root = ET.fromstring(xml_data)
print(root)  # <Element 'ArrayOfExchangeRatesTable' at 0x000001EEBC1CD210>

table_name = root.find(".//Table").text
print(f"Tabela: {table_name}")  # Tabela: A

date = root.find(".//EffectiveDate").text
print(f"Data tabeli: {date}")  # Data tabeli: 2023-07-06

no = root.find('.//No').text
print(f"Numer tabeli {no}")  # Numer tabeli 129/A/NBP/2023

rates = root.findall('.//Rate')
print(rates)

for rate in rates:
    currency = rate.find('Currency').text
    code = rate.find('Code').text
    mid = rate.find('Mid').text
    print(f"{code}: {currency} - {mid}")
# 14:25
