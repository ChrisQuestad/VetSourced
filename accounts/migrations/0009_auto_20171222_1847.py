# Generated by Django 2.0 on 2017-12-23 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20171222_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_employer',
            field=models.BooleanField(default=False),
        ),
    ]
