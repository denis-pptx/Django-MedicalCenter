from django.db import models
from patients.models import PatientProfile
from services.models import Service
from doctors.models import DoctorSchedule


class Order(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    doctor_schedule = models.ForeignKey(DoctorSchedule, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=50,
        choices=[
            ('pending', 'Ожидает выполнения'),
            ('completed', 'Выполнен'),
            ('cancelled', 'Отменен'),
        ],
        default='pending'
    )


