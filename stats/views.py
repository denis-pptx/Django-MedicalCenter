from django.db.models import Q
from django.shortcuts import render
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
