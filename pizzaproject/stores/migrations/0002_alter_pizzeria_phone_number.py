# Generated by Django 3.2.5 on 2021-07-05 16:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzeria',
            name='phone_number',
            field=models.CharField(blank=True, default='+375', max_length=10, validators=[django.core.validators.RegexValidator(regex='\\+375\\d{9}')]),
        ),
    ]