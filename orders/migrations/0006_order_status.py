# Generated by Django 4.2.1 on 2023-09-05 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_doctor_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Ожидает выплнения'), ('completed', 'Выполнен'), ('cancelled', 'Отменен')], default='pending', max_length=50),
        ),
    ]
