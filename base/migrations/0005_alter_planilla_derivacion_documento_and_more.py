# Generated by Django 5.0.3 on 2024-05-03 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_tematica_planilla_derivacion_documento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planilla_derivacion',
            name='documento',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='registro_intervencion',
            name='documento',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
