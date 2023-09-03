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

        if self.experience and self.experience > datetime.now(timezone.utc).date():
            raise ValidationError({'experience': "Experience date should not be in the future."})


class DoctorSchedule(models.Model):
    DAYS_OF_WEEK = (
        ('Mon', 'Понедельник'),
        ('Tue', 'Вторник'),
        ('Wed', 'Среда'),
        ('Thu', 'Четверг'),
        ('Fri', 'Пятница'),
        ('Sat', 'Суббота'),
        ('Sun', 'Воскресенье'),
    )

    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor} - {self.day_of_week}"

    class Meta:
        unique_together = ('doctor', 'day_of_week')

    def clean(self):
        super().clean()

        if self.end_time <= self.start_time:
            raise ValidationError({'end_time': "Время окончания должно быть больше времени начала."})

        existing_schedule = DoctorSchedule.objects.filter(
            doctor=self.doctor,
            day_of_week=self.day_of_week
        ).exclude(pk=self.pk)  # Исключаем текущий объект из поиска

        if existing_schedule.exists():
            raise ValidationError({'day_of_week': "Расписание для этого дня уже существует."})