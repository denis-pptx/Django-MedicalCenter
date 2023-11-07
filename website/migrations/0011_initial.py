# Generated by Django 4.2.1 on 2023-11-07 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '0010_delete_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/banners/')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='RotationInterval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval', models.PositiveIntegerField(default=5000)),
            ],
        ),
    ]