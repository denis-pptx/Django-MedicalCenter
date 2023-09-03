from django import forms
from .models import DoctorProfile


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    experience = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = DoctorProfile
        fields = ['first_name', 'last_name', 'specializations', 'experience',
                  'category', 'academic_degree', 'types', 'photo']
