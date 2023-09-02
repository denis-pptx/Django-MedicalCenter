from django.db import models


class PhoneNumber(models.Model):
    number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.number


class Email(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class WorkingHours(models.Model):
    DAY_CHOICES = [
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ]
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    hours = models.CharField(max_length=100)

    class Meta:
        unique_together = ['day', 'hours']
        verbose_name = 'Working hour'
        verbose_name_plural = 'Working hours'

    def __str__(self):
        return f"{self.get_day_display()}: {self.hours}"


class MedicalCenter(models.Model):
    address = models.CharField(max_length=200, unique=True)
    phone_numbers = models.ManyToManyField(PhoneNumber)
    emails = models.ManyToManyField(Email)
    working_hours = models.ManyToManyField(WorkingHours)

    def __str__(self):
        return self.address
