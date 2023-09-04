from django.db import models
from patients.models import PatientProfile
from services.models import Service
from doctors.models import DoctorProfile


class Order(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    appointment_date = models.DateField()

