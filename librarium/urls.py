from django.urls import path
from . import views

urlpatterns = [
    # lo que se escribe en ruta de chrome
    path("", views.index, name="index"),
    path("download_pdf", views.v_generar_pdf, name="download_pdf"),
    path("data-analitica", views.v_data_analitica, name="data-analitica"),
    path("data-frames", views.v_data_frames, name="data-frames"),
    path("servicios", views.v_servicios, name="servicios"),
]


