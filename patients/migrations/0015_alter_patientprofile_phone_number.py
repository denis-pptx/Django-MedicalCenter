# Generated by Django 4.2.1 on 2023-09-13 21:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0014_alter_patientprofile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='phone_number',
            field=models.CharField(help_text='Формат: +375-XX-XXX-XX-XX', max_length=17, validators=[django.core.validators.RegexValidator(message='Некорректный номер телефона', regex='\\+375-\\d{2}-\\d{3}-\\d{2}-\\d{2}')]),
        ),
    ]
