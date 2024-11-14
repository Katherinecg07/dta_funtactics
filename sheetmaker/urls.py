from django.urls import path
from . import views

urlpatterns = [ # como excribir url en navegador---> sheetmaker/macros
    path("", views.index, name="index"),
    path("download_xls", views.v_reporte_xls, name="download_xls"),
    path("macros", views.v_macros, name="macros"),
    path("powerbi", views.v_powerbi, name="powerbi"),
    path("analitica", views.v_analitica, name="analitica"),
    
]