from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.urls import reverse

from orders.models import Order
from .forms import ProfileForm
from django.shortcuts import redirect
from .models import PatientProfile, Feedback
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from datetime import date

import logging
logger = logging.getLogger(__name__)


@login_required
def profile(request):
    user = request.user
    user_profile = get_object_or_404(PatientProfile, user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            form.save()
            logger.info('Patient ProfileForm is valid. Redirect to profile')
            return redirect('patient_profile')
    else:
        logger.info('Patient ProfileForm is not valid')
        form = ProfileForm(instance=user_profile,
                           initial={'first_name': user.first_name,
                                    'last_name': user.last_name})

    logger.info('Displayed patient profile')
    return render(request, 'patients/profile.html', {'form': form})


@login_required
def create_feedback(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        text = request.POST.get('text')

        if rating and 1 <= int(rating) <= 5 and \
                text and 1 <= len(text) <= 500:
            Feedback.objects.create(user=request.user.patientprofile,
                                    rating=rating,
                                    text=text)
            logger.info('Feedback data is correct. Feedback created')
            return render(request, 'patients/feedback-created.html')
        else:
            logger.warning('Feedback data is not correct')
            return HttpResponseBadRequest("Некорректные данные.")

    logger.info('Opened create feedback page')
    return render(request, 'patients/create-feedback.html')


def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            new_profile = profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()

            new_user.first_name = profile_form.cleaned_data['first_name']
            new_user.last_name = profile_form.cleaned_data['last_name']
            new_user.save()

            logger.info('Registration data is valid. User has registered')
            return render(request, 'patients/register_done.html', {'new_user': new_user})

        logger.warning('Registration data is not valid')
    else:
        user_form = UserCreationForm()
        profile_form = ProfileForm()

    return render(request, 'patients/register.html', {'user_form': user_form,
                                                      'profile_form': profile_form})


def order_list(request):
    orders = Order.objects.filter(Q(patient__user=request.user) &
                                  (Q(status='pending') | Q(status='completed'))
                                  ).order_by('doctor_schedule__date')

    context = {
        'orders': orders,
        'today': date.today()
    }

    logger.info('Displayed order list')
    return render(request, 'patients/order_list.html', context=context)


def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if order.doctor_schedule.date >= date.today() \
            and order.status == 'pending':
        order.status = 'cancelled'
        order.save()
        logger.info('Order is cancelled')

    return redirect(reverse('patient_order_list'))



