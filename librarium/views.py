from django.shortcuts import render
from django.http import HttpResponse

#---------------------------------------
from reportlab.lib.pagesizes import A4  # <---- Libreria
from reportlab.pdfgen import canvas  # <---- Libreria
# Create your views here.

def index(request):
    return HttpResponse("Librarium index")


def v_generar_pdf(request): #<----- View
    # Crear la respuesta HTTP con el tipo de contenido para PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Crear el objeto canvas de ReportLab para generar el PDF
    p = canvas.Canvas(response, pagesize=A4)
    ancho, alto = A4  # Tamaño de la página

    # Agregar contenido al PDF
    p.setFont("Helvetica", 12)
    p.drawString(100, alto - 100,  "Bienvenido al mundo de los libros digitales...")
    p.drawString(100, alto - 120, "¡Disfruta este PDF!")

    # Finalizar y cerrar el PDF
    p.showPage()
    p.save()

    return response