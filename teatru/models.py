from datetime import datetime
from distutils.command.upload import upload
from email.policy import default
from django.db import models


class Employee(models.Model):
    title = models.CharField(max_length=30)
    department =models.CharField(default='placeholder' ,max_length=30)
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='employee_pics')

class Show(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='show_pics')

class Announcement(models.Model):
    title = models.TextField()
    description = models.TextField()
    type = models.CharField(default='placeholder', max_length=30)
    image = models.ImageField(upload_to='announcement_pics')

class Stage(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='stage_pics')

class Actor(models.Model):
    title = models.CharField(max_length=30)
    band =models.CharField(default='placeholder' ,max_length=30)
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='actor_pics')

class Play(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    date= models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to='show_pics')                    