# Generated by Django 5.0 on 2024-01-23 13:58

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_otprequest_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='request_id',
            field=models.UUIDField(default=uuid.UUID('2f7682ca-c4b3-447e-a088-0d2b3ebac584'), editable=False, primary_key=True, serialize=False),
        ),
    ]