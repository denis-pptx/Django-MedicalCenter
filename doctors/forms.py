from django import forms
from datetime import timedelta
from django.utils import timezone
from .models import DoctorProfile, DoctorSchedule


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    experience = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = DoctorProfile
        fields = ['first_name', 'last_name', 'specializations', 'experience',
                  'category', 'academic_degree', 'types', 'photo']


class DoctorScheduleForm(forms.ModelForm):
    class Meta:
        model = DoctorSchedule
        fields = ['date', 'start_time', 'end_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date',
                                           'min': (timezone.now()).date(),
                                           'max': (timezone.now().date() + timedelta(days=30))}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

