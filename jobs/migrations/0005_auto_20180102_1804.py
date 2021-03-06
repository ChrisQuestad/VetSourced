# Generated by Django 2.0 on 2018-01-03 02:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20171222_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_link',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 4, 2, 4, 14, 893016, tzinfo=utc)),
        ),
    ]
