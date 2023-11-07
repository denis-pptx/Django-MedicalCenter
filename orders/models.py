from django.db import models
from patients.models import PatientProfile
from services.models import Service, PromoCode
from doctors.models import DoctorSchedule


class Order(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    doctor_schedule = models.ForeignKey(DoctorSchedule, on_delete=models.CASCADE)
    promo_code = models.ForeignKey(PromoCode, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ('pending', 'Ожидает выполнения'),
            ('completed', 'Выполнен'),
            ('cancelled', 'Отменен'),
        ],
        default='pending'
    )


