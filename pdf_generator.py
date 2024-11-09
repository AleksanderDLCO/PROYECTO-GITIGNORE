from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm, inch  # Asegúrate de que esto esté importado

class numeracionPaginas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """Agregar numeración a cada página"""
        numeroPaginas = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(numeroPaginas)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, conteoPaginas):
        self.drawRightString(200 * mm, 15 * mm + (0.2 * inch), "Página {} de {}".format(self._pageNumber, conteoPaginas))

class reportePDF:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido
        self.estilos = getSampleStyleSheet()

    @staticmethod
    def _encabezadoPiePagina(canvas, archivoPDF):
        """Encabezado y pie de página para el PDF"""
        canvas.saveState()
        estilos = getSampleStyleSheet()

        # Encabezado
        encabezadoNombre = Paragraph("Reporte Generado", estilos["Normal"])
        encabezadoNombre.wrapOn(canvas, archivoPDF.width, archivoPDF.topMargin)
        encabezadoNombre.drawOn(canvas, archivoPDF.leftMargin, archivoPDF.height + archivoPDF.topMargin)

        # Pie de página
        piePagina = Paragraph("Reporte generado por Kyndryl", estilos["Normal"])
        piePagina.wrapOn(canvas, archivoPDF.width, archivoPDF.bottomMargin)
        piePagina.drawOn(canvas, archivoPDF.leftMargin, 15 * mm)  # Aquí usas mm, asegúrate de que esté importado correctamente

        canvas.restoreState()

    def convertirDatos(self, cabecera, datos):
        estiloEncabezado = ParagraphStyle(name="estiloEncabezado", alignment=TA_LEFT, fontSize=10, textColor=colors.white)
        claves, nombres = zip(*cabecera)
        encabezado = [Paragraph(nombre, estiloEncabezado) for nombre in nombres]
        nuevosDatos = [tuple(encabezado)]

        for dato in datos:
            nuevosDatos.append([Paragraph(str(dato.get(clave, "N/A")), self.estilos["Normal"]) for clave in claves])

        return nuevosDatos

    def exportar_pdf_en_memoria(self):
        """Exportar el contenido a un único archivo PDF en memoria (para enviar a Cloud Storage)."""
        from io import BytesIO
        buffer = BytesIO()

        alineacionTitulo = ParagraphStyle(name="centrar", alignment=TA_CENTER, fontSize=13, textColor=colors.red)
        alineacionSubTitulo = ParagraphStyle(name="ladear", alignment=TA_LEFT, fontSize=11, textColor=colors.red)
        historia = [Paragraph(self.titulo, alineacionTitulo), Spacer(1, 12)]

        for seccion in self.contenido:
            historia.append(Paragraph(seccion["titulo_seccion"], alineacionSubTitulo))
            historia.append(Spacer(1, 15))
            convertirDatos = self.convertirDatos(seccion["cabecera"], seccion["datos"])
            tabla = Table(convertirDatos, colWidths=(540 / len(seccion["cabecera"])), hAlign="CENTER")
            tabla.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.red),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.black),
            ]))
            historia.append(tabla)
            historia.append(Spacer(1, 15))

        archivoPDF = SimpleDocTemplate(buffer, pagesize=letter)
        archivoPDF.build(historia, onFirstPage=self._encabezadoPiePagina, onLaterPages=self._encabezadoPiePagina, canvasmaker=numeracionPaginas)

        buffer.seek(0)
        return buffer
