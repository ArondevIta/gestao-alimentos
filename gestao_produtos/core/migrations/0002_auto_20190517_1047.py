# Generated by Django 2.2.1 on 2019-05-17 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Peso'),
        ),
    ]
