# Generated by Django 4.2.1 on 2023-11-07 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_summary_news_text_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='images/news/'),
        ),
    ]
