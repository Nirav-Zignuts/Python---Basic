import csv
with open('data.csv',mode='r') as file:
    read = csv.reader(file)
    for line in read:
        print(line)