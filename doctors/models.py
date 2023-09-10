from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from services.models import Category as ServiceCategory
from datetime import date, timedelta


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


class DoctorProfile(models.Model):
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

        if self.experience and self.experience > datetime.now().date():
            raise ValidationError({'experience': "Experience date should not be in the future."})


class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    date = models.DateField(default=date.today() + timedelta(days=1))
    start_time = models.TimeField(default='09:00')
    end_time = models.TimeField(default='17:00')

    def __str__(self):
        return f"{self.doctor}"

    class Meta:
        unique_together = ('doctor', 'date')

    def clean(self):
        super().clean()

        if self.end_time <= self.start_time:
            raise ValidationError({'end_time': "Время окончания должно быть больше времени начала."})

        if self.date < datetime.now().date():
            raise ValidationError({'date': "Вы не можете добавить расписание в прошлом."})

        max_allowed_date = datetime.now().date() + timedelta(days=30)
        if self.date > max_allowed_date:
            raise ValidationError({'date': "Вы не можете добавить расписание более чем на 30 дней вперед."})

        existing_schedule = DoctorSchedule.objects.filter(
            doctor=self.doctor,
            date=self.date
        ).exclude(pk=self.pk)

        if existing_schedule.exists():
            raise ValidationError({'date': "Расписание для этой даты уже существует."})