from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, EmployerProfile

class EmployerForm(ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ['company', 'about', 'industry', 'location',]


class UpdateProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['bio', 'industry', 'current_job', 'desired_industry', 'desired_job']
