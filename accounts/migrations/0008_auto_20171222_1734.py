# Generated by Django 2.0 on 2017-12-23 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20171221_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_employer',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
