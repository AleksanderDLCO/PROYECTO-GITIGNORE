from google.cloud import storage

def upload_to_cloud_storage(pdf_content, bucket_name, file_name):
    # Crear un cliente de Google Cloud Storage
    storage_client = storage.Client()

    # Obtener el bucket
    bucket = storage_client.bucket(bucket_name)

    # Crear un objeto Blob para el archivo
    blob = bucket.blob(file_name)

    # Subir el contenido del archivo al bucket
    blob.upload_from_file(pdf_content, content_type='application/pdf')

    # La URL pública del archivo (esto es accesible si el bucket permite acceso público)
    return blob.public_url
