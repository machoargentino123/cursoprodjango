# Generated by Django 3.0.2 on 2020-11-26 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0005_auto_20200820_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleados',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombre completo'),
        ),
    ]
