from google.cloud import bigquery

def upload_to_bq():
    client = bigquery.Client()
    table_name = 'gen_energy_non_part'
    #the * means to load all files that match that pattern
    gs_path = 'gs://xiangfei_india_energy/file*'
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    # truncate any data already there
    job_config.write_disposition = 'WRITE_TRUNCATE'
    # skip the first row, because it contains header info
    job_config.skip_leading_rows = 1
    dataset_ref = client.dataset('india_energy')
    dataset = bigquery.Dataset(dataset_ref)
    load_job = client.load_table_from_uri(
           gs_path, dataset_ref.table(table_name),
          job_config=job_config)
    try:
        load_job.result()
    except google.api_core.exceptions.BadRequest:
        raise ValueError(load_job.errors)

if __name__ == '__main__':
    upload_to_bq()
