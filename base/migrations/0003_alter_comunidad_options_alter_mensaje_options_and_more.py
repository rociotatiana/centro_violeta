# Generated by Django 5.0.3 on 2024-05-02 17:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_user_apellido_remove_user_nombre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comunidad',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AlterModelOptions(
            name='mensaje',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.RenameField(
            model_name='mensaje',
            old_name='comunidades',
            new_name='comunidad',
        ),
        migrations.AddField(
            model_name='comunidad',
            name='participantes',
            field=models.ManyToManyField(blank=True, related_name='participantes', to=settings.AUTH_USER_MODEL),
        ),
    ]