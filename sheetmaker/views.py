from django.shortcuts import render
from django.http import HttpResponse
from openpyxl import Workbook
import datetime
# Create your views here.

# Declarar una variable
static_values =  {
    "direccion": "Las flores amarillas 343434 | Concepción",
    "telefono": "+56 912345678",
    "email": " me@gmail.com",
    "whatsapp": "+56 985717759",
    "instagram": ""
}

def index(request):
    return HttpResponse("sheetmaker index")

def v_macros(request): # carpeta en donde se encuentra el html
    context =  {
        "static_values": static_values,
        "features": ["Soporta xls, xlsx, formatos libres.",
            "Permite importar, modificar y exportar.",
            "Cantidad de ejecuciones ilimitadas.",
            "Envia tus reportes por email.",
            "Edita documentos en línea."]
    }
    return render(request, "sheetmaker/macros.html", context)

def v_powerbi(request):
    context =  {
        "static_values": static_values,
        "features": ["Caract1",
            "Permite elaborar dashboards muy interesantes",
            "Caract2 ",
            "Caract3",
            "Caract4."]
    }
    return render(request, "sheetmaker/powerbi.html", context)

def v_analitica(request):
    context =  {
        "static_values": static_values,
        "promos": [ # diccionario dentro de un array
            {
                "title": "10% Off", 
                "color": "bg-primary", 
                "rules": ["Regla1", "Regla2"] # array dentro de un diccionario
            },
            {"title": "30% Off", "color": "bg-success",
             "rules": ["Regla1", "Regla2"]
             },
            {"title": "50% Off", "color": "bg-danger",
             "rules": ["Regla1", "Regla2"]
             }
        ]
    }
    return render(request, "sheetmaker/analitica.html", context)

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