# Generated by Django 5.0.3 on 2024-04-22 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_region_nombre'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comunidades',
            new_name='Comunidad',
        ),
    ]
