from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
from services.models import Service


class Patient(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    date_of_birth = models.DateField(
        validators=[MinValueValidator(date(1900, 1, 1)), MaxValueValidator(date.today())]
    )
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        unique_together = ['last_name', 'first_name', 'patronymic', 'date_of_birth']



class Order(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.pk}"
