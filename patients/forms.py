from django import forms
from .models import PatientProfile


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientProfile
        fields = ['first_name', 'last_name', 'date_of_birth',
                  'phone_number', 'address']
