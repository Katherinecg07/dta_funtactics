from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("download_pdf", views.v_generar_pdf, name="download_pdf")
  
]


