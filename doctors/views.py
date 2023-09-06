from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from datetime import date

from django.views.decorators.http import require_POST

from orders.models import Order
from .forms import ProfileForm, DoctorScheduleForm
from .models import DoctorProfile, DoctorSchedule


@permission_required('doctors.can_edit_profile')
def profile(request):
    user = request.user
    user_profile = get_object_or_404(DoctorProfile, user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            form.save()
            return redirect('doctor_profile')
    else:
        form = ProfileForm(instance=user_profile,
                           initial={'first_name': user.first_name,
                                    'last_name': user.last_name})

    return render(request, 'doctors/profile.html', {'form': form})


def doctors(request):
    return render(request, 'doctors/doctors_list.html')


@permission_required('doctors.view_doctorschedule')
def doctor_schedule(request):
    doctor = request.user.doctorprofile
    schedule = DoctorSchedule.objects.filter(doctor=doctor,
                                             date__gte=date.today()
                                             ).order_by('date')

    return render(request, 'doctors/schedule.html', {'doctor_schedule': schedule,
                                                     'doctor': doctor})


@permission_required('doctors.add_doctorschedule')
def create_schedule(request):
    if request.method == 'POST':
        form = DoctorScheduleForm(request.POST)
        form.instance.doctor = request.user.doctorprofile
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.doctor = request.user.doctorprofile
            schedule.save()
            return redirect(reverse('doctor_schedule'))
    else:
        form = DoctorScheduleForm()

    return render(request, 'doctors/create_schedule.html', {'form': form})


@permission_required('doctors.change_doctorschedule')
def update_schedule(request, pk):
    schedule = DoctorSchedule.objects.get(pk=pk)

    orders_on_schedule = Order.objects.filter(doctor_schedule=schedule)
    if orders_on_schedule.exists():
        return render(request, 'doctors/cannot_modify_schedule.html',
                      {'schedule': schedule, 'orders': orders_on_schedule})

    if request.user.doctorprofile != schedule.doctor:
        return redirect(reverse('doctor_schedule'))

    if request.method == 'POST':
        form = DoctorScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('doctor_schedule')
    else:
        form = DoctorScheduleForm(instance=schedule)

    return render(request, 'doctors/update_schedule.html', {'form': form, 'schedule': schedule})


@permission_required('doctors.delete_doctorschedule')
def delete_schedule(request, pk):
    schedule = get_object_or_404(DoctorSchedule, pk=pk)

    orders_on_schedule = Order.objects.filter(doctor_schedule=schedule)
    if orders_on_schedule.exists():
        return render(request, 'doctors/cannot_modify_schedule.html',
                      {'schedule': schedule, 'orders': orders_on_schedule})

    if request.user.doctorprofile != schedule.doctor:
        return redirect('doctor_schedule')

    if request.method == 'POST':
        schedule.delete()
        return redirect('doctor_schedule')

    return render(request, 'doctors/delete_schedule.html', {'schedule': schedule})


def order_list(request):
    doctor = request.user.doctorprofile
    status = request.GET.get('status', 'all')
    days = request.GET.get('days', 'all')

    if status == 'completed':
        status_filter = Q(status='completed')
    elif status == 'pending':
        status_filter = Q(status='pending')
    else:
        status_filter = Q()

    today = date.today()
    if days == 'past':
        days_filter = Q(doctor_schedule__date__lt=today)
    elif days == 'today':
        days_filter = Q(doctor_schedule__date=today)
    elif days == 'future':
        days_filter = Q(doctor_schedule__date__gt=today)
    else:
        days_filter = Q()

    not_cancelled_filter = ~Q(status='cancelled')

    orders = Order.objects.filter(
        (status_filter & days_filter & not_cancelled_filter) &
        Q(doctor_schedule__doctor=doctor)
    ).order_by('doctor_schedule__date')

    context = {
        'doctor': doctor,
        'orders': orders,
        'status': status,
        'days': days,
    }
    return render(request, 'doctors/order_list.html', context=context)



@require_POST
def complete_order(request, order_id):
    doctor = request.user.doctorprofile
    order = get_object_or_404(Order, id=order_id, doctor_schedule__doctor=doctor)

    if order.status == 'pending':
        order.status = 'completed'
        order.save()

    return redirect('doctor_order_list')
