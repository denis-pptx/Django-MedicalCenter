# Generated by Django 4.2.1 on 2023-09-13 21:15

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0013_alter_patientprofile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='date_of_birth',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(1900, 1, 1)), django.core.validators.MaxValueValidator(datetime.date(2023, 9, 14))]),
        ),
    ]
