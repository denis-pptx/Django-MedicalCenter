from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MinLengthValidator


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")
    image = models.ImageField(upload_to='images/services/categories', null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'subcategories'
        verbose_name = 'subcategory'


class Service(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    price = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(999999999)])

    def __str__(self):
        return self.name


class PromoCode(models.Model):
    code = models.CharField(
        max_length=4,
        unique=True,
        validators=[MinLengthValidator(limit_value=4)]
    )

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    discount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], help_text='скидка в процентах')
    isAvailable = models.BooleanField(default=True)

    def __str__(self):
        return self.code