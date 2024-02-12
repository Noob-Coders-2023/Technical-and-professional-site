# Generated by Django 5.0 on 2024-02-12 14:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_choes_cours_selection_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choes_cours',
            name='selection_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='زمان انتخاب شده درس'),
        ),
    ]
