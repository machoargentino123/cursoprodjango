# Generated by Django 3.1.5 on 2021-01-11 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0007_empleados_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='Avatar',
            field=models.ImageField(blank=True, null=True, upload_to='media/empleado', verbose_name='Foto'),
        ),
    ]