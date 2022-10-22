from django.contrib import admin
from .models import Employee, Actor, Announcement, Stage, Show, Play

admin.site.register(Employee)
admin.site.register(Actor)
admin.site.register(Stage)
admin.site.register(Play)
admin.site.register(Show)
admin.site.register(Announcement)
