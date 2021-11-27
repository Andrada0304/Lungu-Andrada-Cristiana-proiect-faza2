from django.db import models
from django.contrib.auth.models import User
class List(models.Model):
    name = models.CharField(max_length=50)

class Card(models.Model):
    title = models.CharField(max_length=100)
    description  = models.TextField(blank=True)
    list = models.ForeignKey(List, related_name="cards", on_delete=models.CASCADE)
    story_points = models.IntegerField(null=True, blank=True)
    business_value = models.IntegerField(null=True, blank=True)

class User2(models.Model):
    name = models.TextField(max_length=100)
    birthDate = models.TextField(max_length=50)
    username = models.TextField(max_length=100)
    password = models.TextField(max_length=100)

class Message(models.Model):
    message = models.CharField(max_length=10000)
    timestamp = models.DateTimeField(auto_now = True)
    user =models.CharField(max_length=500)


# Create your models here.
