# Generated by Django 5.0 on 2024-01-23 11:11

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_otprequest_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='request_id',
            field=models.UUIDField(default=uuid.UUID('eb798064-eeae-4783-90e6-ad17a892fa7a'), editable=False, primary_key=True, serialize=False),
        ),
    ]
