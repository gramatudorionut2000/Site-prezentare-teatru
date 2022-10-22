from django.shortcuts import render

def tickets(request):
    return render(request, 'users/bilete.html')

def contact(request):
    return render(request, 'users/contact.html')

def contact_form(request):
    return render(request, 'users/Formular_de_contact.html')

def reservation_form(request):
    return render(request, 'users/Formular_de_rezervare.html')