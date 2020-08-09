import csv

with open('energy.csv', 'r') as read_obj, open('temp.csv', 'w') as write_obj:
    csv_reader = csv.reader(read_obj)
    csv_writer = csv.writer(write_obj)
    #['Date', 'Region', 'thermal_actual', 'thermal_est', 'nuclear_actual', 'nuclear_est', 'hydro_actual', 'hydro_est']

    for counter, row in enumerate(csv_reader):
        if counter == 0:
            csv_writer.writerow(row)
            print(row)
        else:
            r = []
            for counter, i in enumerate(row):
                if counter <= 1:
                    r.append(i)
                else:
                    r.append(float(i.replace(',','')))
            csv_writer.writerow(r)
