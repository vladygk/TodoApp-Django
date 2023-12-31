# Generated by Django 4.2.4 on 2023-08-17 21:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_todotask_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotask',
            name='Title',
            field=models.CharField(max_length=30, validators=[django.core.validators.MaxLengthValidator(30), django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator('^[A-Za-z ]+$', message='Todo task name should contain only letters!')]),
        ),
    ]
