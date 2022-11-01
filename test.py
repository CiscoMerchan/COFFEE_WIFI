import csv
# def cafes():
with open('cafe-data.csv', newline='') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    list_of_rows = []
    for row in csv_data:
        print(row)
        list_of_rows.append(row)

    
