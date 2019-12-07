import csv

with open("sample.csv", "x", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["1", "2", "3"])
    w.writerow(["4", "5", "6"])
