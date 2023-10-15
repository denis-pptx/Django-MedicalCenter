from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/news/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'

