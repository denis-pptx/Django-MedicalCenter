from statistics import median

from django.db.models import Q, Count, Sum
from django.shortcuts import render

from doctors.models import DoctorProfile
from orders.models import Order, PatientProfile
from datetime import date
from django.contrib.auth.decorators import user_passes_test

from services.models import Service


@user_passes_test(lambda user: user.is_superuser)
def planned_visits(request):

    status = request.GET.get('status', 'all')
    if status == 'completed':
        status_filter = Q(status='completed')
    elif status == 'pending':
        status_filter = Q(status='pending')
    elif status == 'cancelled':
        status_filter = Q(status='cancelled')
    else:
        status_filter = Q()

    days = request.GET.get('days', 'all')
    today = date.today()
    if days == 'past':
        days_filter = Q(doctor_schedule__date__lt=today)
    elif days == 'today':
        days_filter = Q(doctor_schedule__date=today)
    elif days == 'future':
        days_filter = Q(doctor_schedule__date__gt=today)
    else:
        days_filter = Q()

    order = request.GET.get('order', 'asc')
    if order == 'asc':
        order_by = 'doctor_schedule__date'
    else:
        order_by = '-doctor_schedule__date'

    orders = Order.objects.filter(status_filter & days_filter).order_by(order_by)

    patient_id = request.GET.get('patient_id', None)
    if patient_id:
        orders = orders.filter(patient__id=patient_id)

    patients = PatientProfile.objects.all()

    context = {'status': status,
               'days': days,
               'order': order,
               'orders': orders,
               'patient_id': int(patient_id) if patient_id else None,
               'patients': patients}

    return render(request, 'stats/planned_visits.html', context)


@user_passes_test(lambda user: user.is_superuser)
def cost_summary(request):
    patients = PatientProfile.objects.all()

    patient_id = request.GET.get('patient_id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    summary = []
    if patient_id and start_date and end_date:
        selected_patient = PatientProfile.objects.get(id=patient_id)
        orders = Order.objects.filter(
            patient=selected_patient,
            doctor_schedule__date__range=(start_date, end_date)
        ).exclude(status='cancelled')

        doctor_costs = {}
        for order in orders:
            doctor = order.doctor_schedule.doctor
            cost = doctor_costs.get(doctor, 0) + order.service.price
            doctor_costs[doctor] = cost

        summary = [(doctor, cost) for doctor, cost in doctor_costs.items()]

    return render(request, 'stats/cost_summary.html', {
        'patients': patients,
        'patient_id': int(patient_id) if patient_id else None,
        'start_date': start_date,
        'end_date': end_date,
        'summary': summary
    })


@user_passes_test(lambda user: user.is_superuser)
def doctor_appointments(request):
    doctors = DoctorProfile.objects.all()
    doctor_id = request.GET.get('doctor_id')
    selected_date = request.GET.get('date')

    patients = []
    if doctor_id:
        orders = Order.objects.filter(doctor_schedule__doctor_id=doctor_id).exclude(status='cancelled')
        if selected_date:
            orders = orders.filter(doctor_schedule__doctor_id=doctor_id)

        patients = list(set(map(lambda order: order.patient, orders)))

    context = {
        'doctors': doctors,
        'doctor_id': int(doctor_id) if doctor_id else None,
        'selected_date': selected_date,
        'patients': patients,
    }

    return render(request, 'stats/doctor_appointments.html', context=context)


@user_passes_test(lambda user: user.is_superuser)
def patients(request):
    return render(request, 'stats/patients.html', context={
        'patients': PatientProfile.objects.order_by('user__first_name', 'user__last_name')
    })


@user_passes_test(lambda user: user.is_superuser)
def services_and_sales(request):
    services = Service.objects.order_by('name')

    sales = 0.0
    for order in Order.objects.filter(status='completed'):
        sales += order.service.price

    context = {
        'services': services,
        'sales': sales,
    }

    return render(request, 'stats/services_and_sales.html', context)


@user_passes_test(lambda user: user.is_superuser)
def statistics(request):

    ages = [(date.today() - patient.date_of_birth).days // 365
            for patient in PatientProfile.objects.all()]
    avg_age = round(sum(ages) / len(ages), 2) if ages else 0
    median_age = round(median(ages), 2) if ages else 0

    popular_services = Service.objects.annotate(order_count=Count('order')).order_by('-order_count')
    most_popular_service = popular_services.first()

    profitable_services = Service.objects.annotate(total_profit=Sum('order__service__price')).order_by('-total_profit')
    most_profitable_service = profitable_services.first()

    context = {
        'avg_age': avg_age,
        'median_age': median_age,
        'most_popular_service': most_popular_service,
        'most_profitable_service': most_profitable_service
    }

    return render(request, 'stats/statistics.html', context)
