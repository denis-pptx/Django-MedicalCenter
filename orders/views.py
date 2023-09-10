from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Service, Order
from doctors.models import DoctorProfile, DoctorSchedule


def select_doctor(request, service_id):
    service = Service.objects.get(id=service_id)
    doctors = DoctorProfile.objects.filter(specializations__service_category=service.subcategory.category)
    context = {
        'service': service,
        'doctors': doctors,
    }
    return render(request, 'orders/select_doctor.html', context)


def select_doctor_date(request):
    if request.method == 'POST':
        service = get_object_or_404(Service, id=request.POST.get('service_id'))
        doctor = get_object_or_404(DoctorProfile, id=request.POST.get('doctor_id'))
        schedules = doctor.doctorschedule_set.filter(date__gte=datetime.now().date())

        context = {
            'service': service,
            'doctor': doctor,
            'schedules': schedules
        }

        return render(request, 'orders/select_doctor_date.html', context)


def create_order(request):
    if request.method == 'POST':
        service = Service.objects.get(id=request.POST.get('service_id'))
        schedule = DoctorSchedule.objects.get(id=request.POST.get('schedule_id'))

        Order.objects.create(
            patient=request.user.patientprofile,
            service=service,
            doctor_schedule=schedule
        )

        context = {
            'service': service,
            'schedule': schedule
        }

        return render(request, 'orders/order_success.html', context=context)

