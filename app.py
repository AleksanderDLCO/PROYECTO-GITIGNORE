import json
from datetime import datetime
from conexion_datos_PDF import generarReporteDesdeBigQuery
from cloud_storage_client import upload_to_cloud_storage

# Función para leer queries y cabeceras desde un archivo JSON
def leerConsultasDesdeArchivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            data = json.load(archivo)
            return data["queries"]
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {ruta_archivo}")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo {ruta_archivo} tiene un formato incorrecto")
        return []

# Función para generar nombre de archivo con fecha y hora actuales
def generar_nombre_archivo():
    ahora = datetime.now()
    fecha = ahora.strftime("%Y-%m-%d")
    hora = ahora.strftime("%H-%M-%S")
    return f"Reporte_{fecha}_{hora}.pdf"

# Leer queries desde el archivo 'queries.json'
queries = leerConsultasDesdeArchivo('queries.json')

# Generar un reporte único con las múltiples consultas
if queries:
    pdf_content = generarReporteDesdeBigQuery("Reporte de Ventas Múltiple", queries)
    bucket_name = 'poc_gen_kyndryl'
    file_name = generar_nombre_archivo()  # Generar nombre de archivo con fecha y hora
    file_url = upload_to_cloud_storage(pdf_content, bucket_name, file_name)
    print(f"PDF generado y subido con éxito: {file_url}")
else:
    print("No se encontraron queries para procesar.")

