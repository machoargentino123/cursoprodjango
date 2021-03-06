# Generated by Django 3.0.2 on 2020-08-19 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0002_auto_20200817_0007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['name'], 'verbose_name': 'Departamento', 'verbose_name_plural': 'Areas departamentales'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'short_name')},
        ),
    ]
