import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True, default="user")

class CustomUser(models.Model):
    # Add your custom fields here, e.g., roles
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    roles = models.ManyToManyField(Role, blank=True)
    
    def __str__(self):
        return self.email

class Washroom(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    condition = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Ticket(models.Model):
    washroom = models.ForeignKey(Washroom, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    ticket_text = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default="Open")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published", default=timezone.now)

    def __str__(self):
        return self.ticket_text