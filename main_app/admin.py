from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Chef, Client, Request, Comment


# Register your models here.

admin.site.register(Chef)
admin.site.register(Client)
admin.site.register(Request)
admin.site.register(Comment)