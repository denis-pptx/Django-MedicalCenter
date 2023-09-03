from django.shortcuts import get_object_or_404
from .forms import ProfileForm
from django.shortcuts import redirect
from .models import PatientProfile
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


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
            return redirect('patient_profile')
    else:
        form = ProfileForm(instance=user_profile,
                           initial={'first_name': user.first_name,
                                    'last_name': user.last_name})

    return render(request, 'patients/profile.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            new_profile = profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return render(request, 'patients/register_done.html', {'new_user': new_user})
    else:
        user_form = UserCreationForm()
        profile_form = ProfileForm()

    return render(request, 'patients/register.html', {'user_form': user_form,
                                                      'profile_form': profile_form})
