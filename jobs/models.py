import datetime
from django.db import models
from django.utils import timezone

class Job(models.Model):
    # Job Title
    title = models.CharField(max_length=64)
    # Company
    company = models.CharField(max_length=32)
    # Full Time, Part Time, Intern, Contract, Temporary
    employment_type = models.CharField(max_length=32)
    # Salary
    compensation = models.CharField(max_length=32)
    # Job Location(s)
    location = models.CharField(max_length=32)
    # Required Experience
    experience_required = models.CharField(max_length=32)
    # Education Required
    education = models.CharField(max_length=32)
    # Date Job Was Created
    posted_at = models.DateTimeField(auto_now_add=True)
    # Job Description(Company Info, Responsibilities, Requirements)
    description = models.TextField()
    # Link to Company site
    job_link = models.URLField()
    # Job Posting Expiration
    expires = models.DateTimeField(default=timezone.now() + datetime.timedelta(weeks=+26))
    # Belongs to an employer
    employer = models.ForeignKey('accounts.User',
                                    related_name='jobs',
                                    on_delete=models.CASCADE)
    def __str__(self):
        return self.title + ' ' + self.company
