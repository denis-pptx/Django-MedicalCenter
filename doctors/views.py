from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm
from .models import Profile


@permission_required('doctors.can_edit_profile')
def profile(request):
    user = request.user
    user_profile = get_object_or_404(Profile, user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile,
                           initial={'first_name': user.first_name,
                                    'last_name': user.last_name})

    return render(request, 'doctors/profile.html', {'form': form})


def doctors(request):
    return render(request, 'doctors/doctors_list.html')
