from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("download_png", views.v_reporte_png, name="download_png"),
    path("lista_reportes", views.v_lista_reportes, name="lista_reportes"),
     #/graphify/lista_reportes
    path("lista_imagenes", views.v_lista_imagenes, name="lista_imagenes")
    
]