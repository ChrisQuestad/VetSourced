# Generated by Django 2.0 on 2017-12-22 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_employerprofile_employer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employerprofile',
            name='employer',
        ),
    ]