from django import forms
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
    email = forms.CharField(label='Email', widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
