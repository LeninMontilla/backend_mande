# Generated by Django 5.0.2 on 2024-02-10 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicios',
            name='image_servicio',
        ),
    ]