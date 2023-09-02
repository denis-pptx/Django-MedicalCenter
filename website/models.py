from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Page(models.Model):
    PAGE_TYPES = (
        ('home', 'Главная'),
        ('about', 'О нас'),
        ('requisites', 'Реквизиты'),
        ('faq', 'FAQ'),
    )

    title = models.CharField(max_length=200)
    page_type = models.CharField(max_length=20, choices=PAGE_TYPES, default='home')
    active = models.BooleanField(default=True)
    content = MarkdownxField()

    @property
    def formatted_markdown(self):
        return markdownify(self.content)
