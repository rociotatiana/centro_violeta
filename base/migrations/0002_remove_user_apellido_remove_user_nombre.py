# Generated by Django 5.0.3 on 2024-04-26 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nombre',
        ),
    ]
