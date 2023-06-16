import csv
reader = csv.DictReader(open('test.csv'))

result = {}
for row in reader:
    for column, value in row.items():  # consider .iteritems() for Python 2
        result.setdefault(column, []).append(value)
print(result)

reader = csv.DictReader(open('test.csv'))

result = {}

for row in reader:
    for column, value in row.items():
        result.setdefault(column, []).append(value)
