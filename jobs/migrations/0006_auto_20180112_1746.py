# Generated by Django 2.0 on 2018-01-13 01:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20180102_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 14, 1, 46, 54, 83267, tzinfo=utc)),
        ),
    ]
