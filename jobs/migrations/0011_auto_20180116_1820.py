# Generated by Django 2.0 on 2018-01-17 02:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20180112_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 18, 2, 20, 22, 743835, tzinfo=utc)),
        ),
    ]