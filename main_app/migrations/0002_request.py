# Generated by Django 4.1.2 on 2022-10-12 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('summary', models.TextField(max_length=300)),
                ('people', models.IntegerField(default=1)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.client')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
