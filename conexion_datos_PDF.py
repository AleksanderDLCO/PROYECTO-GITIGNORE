import bigquery_client as DatosBQ
from pdf_generator import reportePDF

def generarReporteDesdeBigQuery(titulo, queries):
    contenido_pdf = []

    for query_info in queries:
        sql_query = query_info["sql"]
        cabecera = query_info["cabecera"]

        datos = DatosBQ.obtenerDatosDeBigQuery(sql_query)
        contenido_pdf.append({
            "titulo_seccion": f"Datos de ventas sobre: {cabecera[0][1]}",
            "cabecera": cabecera,
            "datos": datos
        })

    # Generar el PDF en memoria
    reporte = reportePDF(titulo, contenido_pdf)
    return reporte.exportar_pdf_en_memoria()
