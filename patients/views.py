from django.shortcuts import render
from .forms import ProfileForm
from django.shortcuts import render, redirect


def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('patient_profile')
    else:
        form = ProfileForm(instance=user)

    return render(request, 'patients/profile.html', {'form': form})

