import datetime
import os
import csv
from google.cloud import storage
import shutil
import tempfile
import pprint
pp = pprint.PrettyPrinter(indent = 4)

def make_files(path):
    temp_dir = tempfile.mkdtemp()
    print(temp_dir)
    all_data = {}

    header = None
    with open(path, 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        row_counter = 0
        for row in csv_reader:
            row_counter += 1
            if row_counter == 1:
                if not header:
                    header = row
                continue
            date = datetime.datetime.strptime(row[0], '%Y-%m-%d')
            if not all_data.get(date):
                all_data[date] = []
            all_data[date].append(row)
    for key in all_data.keys():
        with open(os.path.join(temp_dir, 'file_{f}.csv'.format(
            f = key.strftime("%Y_%d_%y"))), 'w') as write_obj:
            csv_writer = csv.writer(write_obj)
            csv_writer.writerow(header)
            for i in all_data[key]:
                csv_writer.writerow(i)
    return temp_dir

def upload_to_storage(bucket_name):
    path = os.path.join('data', 'file.csv')
    temp_dir =  make_files(path)
    client = storage.Client()
    for filename in os.listdir(temp_dir):
        with open(os.path.join(temp_dir, filename), 'rb') as fh:
            bucket = client.get_bucket(bucket_name)
            blob = bucket.blob(filename)
            blob.upload_from_file(fh)
    shutil.rmtree(temp_dir)

if __name__ == '__main__':
    upload_to_storage(bucket_name = 'xiangfei_india_energy', 
            )
