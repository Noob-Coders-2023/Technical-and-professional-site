# Generated by Django 5.0 on 2024-01-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_alter_choes_cours_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='gender',
            field=models.CharField(choices=[('w', 'مونث'), ('m', 'مذکر'), ('wm', 'مونث ومذکر')], max_length=2, verbose_name='جنسیت'),
        ),
    ]