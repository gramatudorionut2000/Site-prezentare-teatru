from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='users-contact'),
    path('formular_de_contact/', views.contact_form, name='users-contact_form'),
    path('bilete/', views.tickets, name='users-tickets'),
    path('formular_de_rezervare/', views.reservation_form, name='users-reservation_form'),
    
]