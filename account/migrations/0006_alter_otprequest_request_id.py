# Generated by Django 5.0 on 2024-01-19 06:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_otprequest_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='request_id',
            field=models.UUIDField(default=uuid.UUID('d540c8a0-63d1-44ba-97ad-82e55f956edc'), editable=False, primary_key=True, serialize=False),
        ),
    ]