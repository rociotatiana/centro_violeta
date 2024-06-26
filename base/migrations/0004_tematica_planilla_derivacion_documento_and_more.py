# Generated by Django 5.0.3 on 2024-05-03 00:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_comunidad_options_alter_mensaje_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tematica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='planilla_derivacion',
            name='documento',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='planilla_derivacion',
            name='estado',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='planilla_derivacion',
            name='respuesta_derivacion',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='registro_intervencion',
            name='documento',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='registro_intervencion',
            name='resumen',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='beneficiaria',
            name='casos_judicializados',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='beneficiaria',
            name='nivel_educativo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='planilla_derivacion',
            name='casos_judicializados',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='comunidad',
            name='tematicas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.tematica'),
        ),
    ]
