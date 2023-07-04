import csv

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as csv_f:
    # sprawdzenie jaki delimiter ma ustawiony plik csv
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)  # delimiter= ;
    csv_f.seek(0)  # zerowanie pozycji, ustawienie indeksu do odczytu na 0

    # csvreader = csv.reader(csv_f, delimiter=";")
    csvreader = csv.reader(csv_f, dialect)
    print(type(csvreader))  # <class '_csv.reader'>

    # next() odczytuje biezacy element
    # przestawia wskaźnik na następny element
    fields = next(csvreader)  # pobrał wiersz 0 i ustawił wskaźnik na wiersz 1
    for row in csvreader:  # pętla wystartowałą od indeksu 1 a  nie 0
        rows.append(row)
    print("Suma wierszy", csvreader.line_num)  # Suma wierszy 8

print(fields)  # ['name', 'branch', 'year', 'cgpa']
print(rows)
# [['Tomek', 'COE', '2', '9.1'], ['Radek', 'COE', '2', '9'], ['Asia', 'COE', '2', '9.1'], ['Radek', 'COT', '2', '9.1'],
#  ['Zenek', 'COE', '3', '9.2'], ['Radek', 'CtI', '2', '9.1'], ['radek', 'coe', '3', '9']]
print(rows[0])  # ['Tomek', 'COE', '2', '9.1']
print(rows[0][0])  # Tomek
