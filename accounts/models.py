from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Users Bio
    bio = models.TextField(blank=True, null=True)
    # Users Current Industry
    industry = models.CharField(max_length=24, blank=True, null=True)
    # Users Current Job Title
    current_job = models.CharField(max_length=24, blank=True, null=True)
    # Users Desired industry
    desired_industry = models.CharField(max_length=64, blank=True, null=True)
    # Users Desired Job Title
    desired_job = models.CharField(max_length=64, blank=True, null=True)
    # Verification of Employee/Employer
    is_employer = models.BooleanField(default=False)
    # User Name
    first_name = models.CharField(max_length=24, blank=True, null=True)
    last_name = models.CharField(max_length=24, blank=True, null=True)


    employer = models.OneToOneField('accounts.EmployerProfile',
                                    blank=True,
                                    null=True,
                                    on_delete=models.SET_NULL)

class EmployerProfile(models.Model):
    # Company Name
    company = models.CharField(max_length=64)
    # Company Description
    about = models.TextField()
    # Company industry
    industry = models.CharField(max_length=64)
    # Company Location(s)
    location = models.CharField(max_length=64)
