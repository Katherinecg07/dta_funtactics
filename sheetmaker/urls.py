from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("download_xls", views.v_reporte_xls, name="download_xls"),
  
]