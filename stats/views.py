from django.db.models import Q
from django.shortcuts import render

from doctors.models import DoctorProfile
from orders.models import Order, PatientProfile
from datetime import date
from django.contrib.auth.decorators import user_passes_test


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
        )

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

    orders = []
    if doctor_id and selected_date:
        orders = Order.objects.filter(
            doctor_schedule__doctor_id=doctor_id,
            doctor_schedule__date=selected_date
        )

    context = {
        'doctors': doctors,
        'doctor_id': int(doctor_id) if doctor_id else None,
        'selected_date': selected_date,
        'orders': orders,
    }

    return render(request, 'stats/doctor_appointments.html', context=context)
