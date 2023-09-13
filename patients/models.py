from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from datetime import date
from django.contrib.auth.models import User
from django.utils import timezone


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(
        validators=[MinValueValidator(date(1900, 1, 1)), MaxValueValidator(date.today())]
    )
    address = models.CharField(max_length=100)

    phone_number = models.CharField(
        max_length=17,
        validators=[
            RegexValidator(
                regex=r"\+375-\d{2}-\d{3}-\d{2}-\d{2}",
                message='Некорректный номер телефона',
            ),
        ],
        help_text="Формат: +375-XX-XXX-XX-XX"
    )

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"


class Feedback(models.Model):
    user = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
