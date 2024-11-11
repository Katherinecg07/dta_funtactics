from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("download_png", views.v_reporte_png, name="download_png")
  
]