from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Service, Order
from services.models import PromoCode
from doctors.models import DoctorProfile, DoctorSchedule

import logging
logger = logging.getLogger(__name__)


def select_doctor(request, service_id):
    service = Service.objects.get(id=service_id)
    doctors = DoctorProfile.objects.filter(specializations__service_category=service.subcategory.category)
    context = {
        'service': service,
        'doctors': doctors,
    }
    logging.info('Displayed doctor selection page')
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

        logging.info('Displayed doctor date selection page')
        return render(request, 'orders/select_doctor_date.html', context)


def create_order(request):
    if request.method == 'POST':
        service = Service.objects.get(id=request.POST.get('service_id'))
        schedule = DoctorSchedule.objects.get(id=request.POST.get('schedule_id'))

        promo_code = PromoCode.objects.filter(code=request.POST.get('promo_code'), isAvailable=True).first()
        print(promo_code)
        Order.objects.create(
            patient=request.user.patientprofile,
            service=service,
            doctor_schedule=schedule,
            promo_code=promo_code
        )

        context = {
            'service': service,
            'schedule': schedule
        }

        return render(request, 'orders/order_success.html', context=context)

