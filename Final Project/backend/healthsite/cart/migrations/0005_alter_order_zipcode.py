# Generated by Django 4.0.1 on 2022-04-24 18:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_order_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='zipcode',
            field=models.CharField(max_length=5, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Zipcode'),
        ),
    ]
