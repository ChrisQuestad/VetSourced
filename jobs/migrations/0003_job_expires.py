# Generated by Django 2.0 on 2017-12-23 02:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20171219_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 23, 2, 47, 6, 236036, tzinfo=utc)),
        ),
    ]
