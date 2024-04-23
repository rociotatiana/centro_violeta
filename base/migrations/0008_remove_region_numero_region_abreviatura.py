# Generated by Django 5.0.3 on 2024-04-22 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_comuna_abreviacion_region_numero_provincia_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='numero',
        ),
        migrations.AddField(
            model_name='region',
            name='abreviatura',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
