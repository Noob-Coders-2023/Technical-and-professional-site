# Generated by Django 5.0 on 2024-01-19 06:19

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_otprequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='request_id',
            field=models.UUIDField(default=uuid.UUID('f340df66-de2a-41da-bd70-f75dfb6f08c1'), editable=False, primary_key=True, serialize=False),
        ),
    ]