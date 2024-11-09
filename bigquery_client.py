from google.cloud import bigquery

def obtenerDatosDeBigQuery(sql_query):
    client = bigquery.Client()

    try:
        query_job = client.query(sql_query)
        results = query_job.result()

        datos = [dict(row) for row in results]
        return datos
    except Exception as e:
        print(f"Error al obtener datos de BigQuery: {e}")
        return []
