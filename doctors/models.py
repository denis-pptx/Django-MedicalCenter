from datetime import timezone, datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from services.models import Category as ServiceCategory


class Specialization(models.Model):
    name = models.CharField(max_length=100)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class AcademicDegree(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specializations = models.ManyToManyField(Specialization)
    experience = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    academic_degree = models.ForeignKey(AcademicDegree, on_delete=models.SET_NULL, null=True, blank=True)
    types = models.ManyToManyField(Type)
    photo = models.ImageField(upload_to='images/doctors/profile_photos', null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

    def clean(self):
        super().clean()

        if self.experience and self.experience.year < 1950:
            raise ValidationError({'experience': "The beginning of the work experience should not be less than 1950."})

        if self.experience and self.experience > datetime.now(timezone.utc).date():
            raise ValidationError({'experience': "Experience date should not be in the future."})
