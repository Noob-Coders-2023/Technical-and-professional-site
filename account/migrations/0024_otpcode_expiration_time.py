# Generated by Django 5.0 on 2024-02-17 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_alter_user_national_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='otpcode',
            name='expiration_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
