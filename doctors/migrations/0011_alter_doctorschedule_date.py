# Generated by Django 4.2.1 on 2023-09-11 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0010_alter_doctorschedule_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorschedule',
            name='date',
            field=models.DateField(default=datetime.date(2023, 9, 12)),
        ),
    ]
