from django.shortcuts import render
from .models import MedicalCenter


def medical_centers(request):
    centers = MedicalCenter.objects.all()
    return render(request, 'contacts/medical_centers.html', {'centers': centers})
