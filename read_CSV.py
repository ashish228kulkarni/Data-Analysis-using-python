import csv
f = open('some.csv', 'rb')
reader = csv.reader(f)
for row in reader:
    print row
f.close()
