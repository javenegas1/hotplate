# Generated by Django 4.1.2 on 2022-10-17 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_user_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='profile_pic',
            new_name='profile_picture',
        ),
    ]
