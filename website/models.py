from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/banners/')
    link = models.URLField()


class RotationInterval(models.Model):
    interval = models.PositiveIntegerField(default=5000)
