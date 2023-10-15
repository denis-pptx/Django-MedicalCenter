from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import RegexValidator
from datetime import date
from django.contrib.auth.models import User
from django.utils import timezone


def validate_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18 or age > 130:
        raise ValidationError('Возраст должен быть от 18 до 130 лет')


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(validators=[validate_age])
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
