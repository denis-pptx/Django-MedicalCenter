from django import forms
from django.core.exceptions import ValidationError

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
        fields = ['day_of_week', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

