# Generated by Django 5.0 on 2024-01-23 14:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_otprequest_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='request_id',
            field=models.UUIDField(default=uuid.UUID('93a9d29b-9ad0-4343-aaee-f469b55f83ea'), editable=False, primary_key=True, serialize=False),
        ),
    ]