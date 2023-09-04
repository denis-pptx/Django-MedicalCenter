from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
from django.contrib.auth.models import User
from services.models import Service


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(
        validators=[MinValueValidator(date(1900, 1, 1)), MaxValueValidator(date.today())]
    )
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"


# class Order(models.Model):
#     patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
#     services = models.ManyToManyField(Service)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"Order #{self.pk}"
