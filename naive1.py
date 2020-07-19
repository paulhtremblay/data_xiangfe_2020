import os
import csv
import datetime

import pprint
pp = pprint.PrettyPrinter(indent = 4)

from bokeh.io import show
from bokeh.plotting import figure
from bokeh.layouts import gridplot

def parse_file(path, verbose = False):
    """
    path: path to the CSV file

    Reads CSV file and returns a Python dictionary.
    """
    regions  = {'Northern':[], 'Eastern': [], 'NorthEastern':[], 'Southern': [], 
            'Western': []
            }
    with open(path, 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        row_counter = 0
        for row in csv_reader:
            row_counter += 1
            if row_counter == 1:
                continue
            date = datetime.datetime.strptime(row[0], '%Y-%m-%d')
            thermal_est = float(row[3].replace(',',''))
            nuclear_est = float(row[5].replace(',',''))
            hydro_est = float(row[7].replace(',',''))
            region = row[1]
            regions[region].append((date, thermal_est, nuclear_est, hydro_est))
    if verbose:
        pp.pprint(regions["NorthEastern"])
    return regions

def main():
    """
    Gets data and creates a Bokeh Plot for the Northern Region of India
    """
    d = parse_file(os.path.join('data', 'file.csv'))
    p = figure(x_axis_type = 'datetime', title = 'Estimated Thermal Generation',
                 plot_width = 650 , plot_height = 650, y_range = None)
    p.line(x = [x[0] for x in d['Northern']], 
            y = [x[1] for x in d['Northern']], legend_label = 'ther', color = 'blue')
    p.line(x = [x[0] for x in d['Northern']], 
            y = [x[2] for x in d['Northern']], legend_label = 'nuc', color='red')
    p.line(x = [x[0] for x in d['Northern']], 
            y = [x[3] for x in d['Northern']], legend_label = 'hyd', color='green')
    p.yaxis.axis_label = 'MU'
    show(p)


if __name__ == '__main__': 
    main()
