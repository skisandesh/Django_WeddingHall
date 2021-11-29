import calendar
import time

from django.db import models
from django.contrib.auth.models import User




class HallDetail(models.Model):
    location = models.CharField(max_length=50,default='null')
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    cost = models.CharField(max_length=10)
    area = models.CharField(max_length=50)
    hallimg = models.FileField(upload_to='media/hall_image',default='null')
    def __str__(self):
        return self.name



class UserProfile(models.Model):
    profile = models.CharField(max_length=20)
    list = models.CharField(max_length=20,default='null')
    booked_date = models.DateField()

    def __str__(self):
        return self.profile



class Feedback(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=20)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return self.username