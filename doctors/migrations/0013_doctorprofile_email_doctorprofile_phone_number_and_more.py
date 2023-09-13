# Generated by Django 4.2.1 on 2023-09-12 21:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0012_alter_doctorschedule_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Введите номер телефона в формате +375-XX-XXX-XX-XX', max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='doctorschedule',
            name='date',
            field=models.DateField(default=datetime.date(2023, 9, 14)),
        ),
    ]