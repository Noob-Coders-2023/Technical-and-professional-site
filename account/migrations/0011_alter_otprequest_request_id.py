# Generated by Django 5.0 on 2024-01-23 13:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_otprequest_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='request_id',
            field=models.UUIDField(default=uuid.UUID('3ad94e52-83b9-4cc6-b6f1-3954045f170a'), editable=False, primary_key=True, serialize=False),
        ),
    ]
