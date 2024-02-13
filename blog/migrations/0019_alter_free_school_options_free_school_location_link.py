# Generated by Django 5.0 on 2024-02-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_free_school_delete_yourmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='free_school',
            options={'verbose_name': 'آموزشگاه آزاد', 'verbose_name_plural': 'آموزشگاهای آزاد'},
        ),
        migrations.AddField(
            model_name='free_school',
            name='location_link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='لینک گوگل مپ'),
        ),
    ]
