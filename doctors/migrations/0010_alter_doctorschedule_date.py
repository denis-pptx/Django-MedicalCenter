# Generated by Django 4.2.1 on 2023-09-10 13:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0009_alter_doctorschedule_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorschedule',
            name='date',
            field=models.DateField(default=datetime.date(2023, 9, 11)),
        ),
    ]
