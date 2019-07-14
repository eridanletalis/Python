import csv

with open('Crimes.csv') as file:
    csv_data = [raw for raw in csv.reader(file)]
    id_primary_crime = 0
    d = {}
    for i in range(len(csv_data[0])):
        if csv_data[0][i] == 'Primary Type':
            id_primary_crime = i
            break

    for raw in csv_data:
        if raw[id_primary_crime] == 'Primary Type':
            continue
        if not d.get(raw[id_primary_crime]):
            d[raw[id_primary_crime]] = 1
        else:
            d[raw[id_primary_crime]] += 1
    print(d)