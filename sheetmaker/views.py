from django.shortcuts import render
from django.http import HttpResponse
from openpyxl import Workbook
import datetime
# Create your views here.
def index(request):
    return HttpResponse("sheetmaker index")

def v_macros(request): # carpeta en donde se encuentra el html
    return render(request, "sheetmaker/macros.html")

def v_powerbi(request):
    return render(request, "sheetmaker/powerbi.html")

def v_analitica(request):
    return render(request, "sheetmaker/analitica.html")

def v_reporte_xls(request):
    # Crear un libro de Excel
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Reporte de Ejemplo"

    # Agregar encabezados
    encabezados = ["ID", "Nombre", "Fecha"]
    worksheet.append(encabezados)

    # Agregar algunos datos de ejemplo
    datos = [
        [1, "Alice", datetime.date(2023, 11, 5)],
        [2, "Bob", datetime.date(2023, 11, 6)],
        [3, "Charlie", datetime.date(2023, 11, 7)],
    ]

    for fila in datos:
        worksheet.append(fila)

    # Preparar la respuesta HTTP con el archivo Excel
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=reporte.xlsx"

    # Guardar el libro en la respuesta
    workbook.save(response)

    return response