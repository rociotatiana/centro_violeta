# Generated by Django 5.0.3 on 2024-04-25 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_beneficiaria_rut'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comuna',
            name='region',
        ),
    ]