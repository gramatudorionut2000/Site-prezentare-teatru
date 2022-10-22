from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='teatru-home'),
    path('istoric/', views.istoric, name='teatru-istoric'),
    path('angajatii_teatrului/', views.angajatii_teatrului, name='teatru-angajatii_teatrului'), 
    path('trupe_de_actori/', views.trupe_de_actori, name='teatru-trupe_de_actori'), 
    path('informatii_generale/', views.informatii_generale, name='teatru-informatii_generale'), 
    path('sali_de_spectacol/', views.sali_de_spectacol, name='teatru-sali_de_spectacol'),
    path('program/', views.program, name='teatru-program'),  
]