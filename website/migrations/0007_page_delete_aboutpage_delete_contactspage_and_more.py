# Generated by Django 4.2.1 on 2023-06-04 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_requisitespage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('page_type', models.CharField(choices=[('home', 'Главная'), ('about', 'О нас'), ('requisites', 'Реквизиты'), ('faq', 'FAQ')], default='home', max_length=20)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AboutPage',
        ),
        migrations.DeleteModel(
            name='ContactsPage',
        ),
        migrations.DeleteModel(
            name='FAQPage',
        ),
        migrations.DeleteModel(
            name='RequisitesPage',
        ),
    ]
