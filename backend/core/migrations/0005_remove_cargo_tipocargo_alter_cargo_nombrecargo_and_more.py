# Generated by Django 5.0.4 on 2024-06-19 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tipocargo_cargo_tipocargo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargo',
            name='tipoCargo',
        ),
        migrations.AlterField(
            model_name='cargo',
            name='nombreCargo',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='TipoCargo',
        ),
    ]