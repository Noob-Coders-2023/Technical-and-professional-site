# Generated by Django 5.0 on 2024-02-19 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0025_otpcode_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otpcode',
            name='first_name',
        ),
    ]
