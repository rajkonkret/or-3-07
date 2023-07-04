import csv

lista = []
with open('dane.csv', "r") as file:
    reader = csv.reader(file)
    for i in reader:
        lista.append(i)

print(lista)  # [['SN', ' Name', ' City'], ['1', ' Michael', ' New Jersey'], ['2', ' Jack', ' California']]

lista[1][1] = "Radek"

with open('dane2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(lista)
# 13:30