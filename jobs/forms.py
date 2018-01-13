from django import forms
from django.forms.models import ModelForm
from .models import Job


class CreateJobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'employment_type', 'compensation',
                'location',
                'experience_required',
                'education',
                'description',
                'job_link',
                ]
