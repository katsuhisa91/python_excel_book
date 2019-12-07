import csv

with open('sample.csv', 'r', newline='') as f:
    r = csv.reader(f)
    for row in r:
        print(row)
