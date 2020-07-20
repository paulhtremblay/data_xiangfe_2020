from google.cloud import bigquery
#import pprint
import google
#import pprint
#pp = pprint.PrettyPrinter(indent = 4)

def create_table():
    client = bigquery.Client()
    dataset_id = 'india_energy'
    table_id = 'gen_energy'
    schema = [
        bigquery.SchemaField('date', 'DATE', mode='REQUIRED'),
        bigquery.SchemaField('region', 'STRING', mode='REQUIRED'),
        bigquery.SchemaField('therm_actual', 'FLOAT', mode='REQUIRED'),
        bigquery.SchemaField('therm_est', 'FLOAT', mode='REQUIRED'),
        bigquery.SchemaField('nuc_actual', 'FLOAT', mode='REQUIRED'),
        bigquery.SchemaField('nuc_est', 'FLOAT', mode='REQUIRED'),
        bigquery.SchemaField('hyd_actual', 'FLOAT', mode='REQUIRED'),
        bigquery.SchemaField('hyd_est', 'FLOAT', mode='REQUIRED'),
            ]
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)
    if table_id in (x.table_id for x in client.list_tables(client.dataset(dataset_id))):
        client.delete_table(table_ref)
    table = bigquery.Table(table_ref, schema=schema)
    table.time_partitioning = bigquery.TimePartitioning(type_=bigquery.TimePartitioningType.DAY, 
            field = 'date', 
            require_partition_filter = False)
    table = client.create_table(table)  

if __name__ == '__main__':
    create_table()
