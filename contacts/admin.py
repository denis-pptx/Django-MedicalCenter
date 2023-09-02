from django.contrib import admin
from .models import PhoneNumber, Email, WorkingHours, MedicalCenter

admin.site.register(MedicalCenter)
admin.site.register(PhoneNumber)
admin.site.register(Email)
admin.site.register(WorkingHours)
