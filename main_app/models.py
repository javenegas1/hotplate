from datetime import date
from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.urls import reverse 

class User(AbstractUser):

    class Role(models.TextChoices):
        CHEF = 'CHEF', 'Chef'
        CLIENT = 'CLIENT', 'Client'

    role = models.CharField(verbose_name='role', max_length=50, choices=Role.choices, default=Role.CLIENT)
    location = models.CharField(verbose_name='location', max_length=50)

    def get_absolute_url(self):
        return '{}'.format(self.username)

class ChefManager(UserManager):

    def create_user(self, *args, **kwargs):
        if not email:
            raise ValueError('User must have email')
        email = self.normalize_email(email)
        user = self.model(*args, **kwargs)
        user.save(using=self._db)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs).filter(role=User.Role.CHEF)
        print(qs)
        return qs

class Chef(User):

    objects = ChefManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = User.Role.CHEF
        return super().save(*args, **kwargs)

class ClientManager(UserManager):

    def create_user(self, *args, **kwargs):
        if not email:
            raise ValueError('User must have email')
        email = self.normalize_email(email)
        user = self.model(*args, **kwargs)
        user.save(using=self._db)
    
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.CLIENT)

class Client(User):

    objects = ClientManager()

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
    date_of_event = models.DateField(default=date.today)

    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, default=1, related_name="requests")
    user = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date_of_event']

##rating system??
##add profile pictures - stretch

class Comment(models.Model):

    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, default=1, related_name="comments")
    name = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)
    body = models.TextField(default='comment')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} commented on {}'.format(self.name.username, self.created)
    
    class Meta:
        ordering = ['-created']