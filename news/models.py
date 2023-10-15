from django.db import models
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from news.common import get_path_to_html, html_template


def upload_to_news_image(instance, filename):
    now = instance.publish_date
    print(now)
    return os.path.join('images',
                        'news',
                        str(now.year),
                        str(now.month).zfill(2),
                        str(now.day).zfill(2),
                        filename)


class News(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_to_news_image, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'


@receiver(post_save, sender=News)
def create_html_file(sender, instance, created, **kwargs):
    if created:  # Ели только что создано
        html_path = os.path.join('news', 'templates',
                                 get_path_to_html(instance))
        os.makedirs(os.path.dirname(html_path), exist_ok=True)  # Создать директории, если их нет
        with open(html_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_template)
