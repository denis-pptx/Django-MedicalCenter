from datetime import datetime, timedelta

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Service, Order
from doctors.models import DoctorProfile, DoctorSchedule


# def select_doctor_date(request, service_id):
#     service = get_object_or_404(Service, id=service_id)
#     doctors = DoctorProfile.objects.filter(specializations__service_category=service.subcategory.category)
#     context = {
#         'service': service,
#         'doctors': doctors,
#     }
#     return render(request, 'orders/select_doctor_date.html', context)


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

        # Определяем текущую дату и конечную дату (через неделю)
        today = datetime.now().date()
        end_date = today + timedelta(days=7)

        # Создаем список слотов для недели вперед
        slots = []
        current_date = today
        while current_date < end_date:
            day_of_week = current_date.strftime('%a')
            # Получаем расписание врача для текущего дня недели
            schedule = DoctorSchedule.objects.filter(
                doctor=doctor,
                day_of_week=day_of_week,
            ).first()
            if schedule:
                slots.append({
                    'date': current_date,
                    'schedule': schedule
                })
            current_date += timedelta(days=1)

        context = {
            'service': service,
            'doctor': doctor,
            'slots': slots,
        }
        return render(request, 'orders/select_doctor_date.html', context)


def create_order(request):
    if request.method == 'POST':
        service_id = request.POST.get('service_id')
        doctor_id = request.POST.get('doctor_id')
        schedule_id = request.POST.get('schedule_id')

        Order.objects.create(
            patient=request.user.patientprofile,
            service=Service.objects.get(id=service_id),
            doctor=DoctorProfile.objects.get(id=doctor_id),
            appointment_date=request.POST.get('appointment_date'),
        )

        return redirect(reverse('order_success'))

