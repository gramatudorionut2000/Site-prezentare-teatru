from django.shortcuts import render
from .models import Employee,Show, Announcement, Actor, Stage, Play

def home(request):
    context_home ={
        'shows': Show.objects.all()
    }
    return render(request, 'teatru/index.html', context_home)

def informatii_generale(request):
    context_announcements ={
        'announcements': Announcement.objects.all()
    }
    return render(request, 'teatru/informatii_generale.html', context_announcements)

def istoric(request):
    return render(request, 'teatru/Istoric.html')

def program(request):
    context_plays ={
        'plays': Play.objects.all()
    }
    return render(request, 'teatru/program.html', context_plays)

def sali_de_spectacol(request):
    context_stages ={
        'stages': Stage.objects.all()
    }
    return render(request, 'teatru/sali_de_spectacol.html', context_stages)

def trupe_de_actori(request):
    context_actors ={
        'actors': Actor.objects.all()
    }
    return render(request, 'teatru/trupe_de_actori.html', context_actors)    

def angajatii_teatrului(request):
    context_employees ={
        'employees': Employee.objects.all()
    }
    return render(request, 'teatru/angajatii_teatrului.html', context_employees)    