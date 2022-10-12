from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse 

class User(AbstractUser):

    class Role(models.TextChoices):
        CHEF = 'CHEF', 'Chef'
        CLIENT = 'CLIENT', 'Client'
    
    class Location(models.TextChoices):
        ATLANTA = 'ATLANTA', 'Atlanta'
        DENVER = 'DENVER', 'Denver'

    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    first_name = models.CharField(verbose_name='first_name', max_length=100)
    last_name = models.CharField(verbose_name='last_name', max_length=100)
    role = models.CharField(verbose_name='role', max_length=50, choices=Role.choices, default=Role.CLIENT)
    location = models.CharField(verbose_name='location', max_length=50, choices=Location.choices, default=Location.ATLANTA)


    def get_absolute_url(self):
        return '{}'.format(self.username)

class ChefManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Role.CHEF)

class Chef(User):

    # objects = ChefManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = User.Role.CHEF
        return super().save(*args, **kwargs)

class ClientManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Role.CLIENT)

class Client(User):

    # objects = ClientManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = User.Role.CLIENT
        return super().save(*args, **kwargs)

class Request(models.Model):

    title = models.CharField(max_length=50)
    summary = models.TextField(max_length=300)
    people = models.IntegerField(default=1)

    user = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

##one to one calendar to chef model
