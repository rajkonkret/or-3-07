# pliki w formacie csv
# pliki w których dane są oddzielone znakiem podziału
# Radek,Maciek,Zenek
import csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['radek', 'coe', '3', '9']

dict2 = dict(zip(fields, row))  # tworzenie słownika na podstwie danych
print(dict2)  # {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '9'}

dict = [
    {'branch': 'COE', 'cgpa': 9.1, 'year': 2, 'name': "Tomek"},
    {'branch': 'COE', 'cgpa': 9, 'year': 2, 'name': "Radek"},
    {'branch': 'COE', 'cgpa': 9.1, 'year': 2, 'name': "Asia"},
    {'branch': 'COT', 'cgpa': 9.1, 'year': 2, 'name': "Radek"},
    {'branch': 'COE', 'cgpa': 9.2, 'year': 3, 'name': "Zenek"},
    {'branch': 'CtI', 'cgpa': 9.1, 'year': 2, 'name': "Radek"},
]

filename = 'records.csv'

with open(filename, 'w', newline='') as csv_f:
    # cswvriter = csv.writer(csv_f)
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=",")
    # csvwriter.writerow(row)
    csvwriter.writeheader()
    csvwriter.writerows(dict)
    csvwriter.writerow(dict2)
