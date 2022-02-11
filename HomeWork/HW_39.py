import csv

with open('data2.csv') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(row)
