from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
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
    schedule = DoctorSchedule.objects.filter(doctor=request.user.doctorprofile)

    def custom_sort(schedule_item):
        days_order = {
            'Mon': 1,
            'Tue': 2,
            'Wed': 3,
            'Thu': 4,
            'Fri': 5,
            'Sat': 6,
            'Sun': 7,
        }
        return days_order[schedule_item.day_of_week]

    sorted_schedule = sorted(schedule, key=custom_sort)
    return render(request, 'doctors/schedule.html', {'doctor_schedule': sorted_schedule,
                                                     'doctor': request.user})


@permission_required('doctors.add_doctorschedule')
def create_schedule(request):
    if request.method == 'POST':
        form = DoctorScheduleForm(request.POST)
        form.instance.doctor = request.user.doctorprofile
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.doctor = request.user.doctorprofile
            schedule.save()
            return redirect('doctor_schedule')
    else:
        form = DoctorScheduleForm()

    return render(request, 'doctors/create_schedule.html', {'form': form})


@permission_required('doctors.change_doctorschedule')
def update_schedule(request, pk):
    schedule = DoctorSchedule.objects.get(pk=pk)

    if request.user.doctorprofile != schedule.doctor:
        return redirect('schedule_list')

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

    if request.user.doctorprofile != schedule.doctor:
        return redirect('schedule_list')

    if request.method == 'POST':
        schedule.delete()
        return redirect('doctor_schedule')

    return render(request, 'doctors/delete_schedule.html', {'schedule': schedule})
