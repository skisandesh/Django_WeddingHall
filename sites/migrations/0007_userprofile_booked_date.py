# Generated by Django 3.1.6 on 2021-06-12 06:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0006_remove_userprofile_lists'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='booked_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
