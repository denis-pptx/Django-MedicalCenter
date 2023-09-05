from django import forms
from datetime import datetime, timedelta
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
                                           'min': (datetime.now()).date(),
                                           'max': (datetime.now() + timedelta(days=30)).date()}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

