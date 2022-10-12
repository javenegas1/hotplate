from django.contrib import admin
from .models import Chef, Client, Request


# Register your models here.

admin.site.register(Chef)
admin.site.register(Client)
admin.site.register(Request)