# Generated by Django 4.1.2 on 2022-10-16 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_chatroom_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChatRoom',
        ),
    ]
