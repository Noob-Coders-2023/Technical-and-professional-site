# Generated by Django 5.0 on 2024-02-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_choes_cours_selection_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Free_school',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='نام آموزشگاه')),
                ('founder', models.CharField(max_length=60, verbose_name='نام موسس')),
                ('phone_number', models.CharField(max_length=11, verbose_name='شماره تماس')),
                ('field', models.CharField(max_length=100, verbose_name='رشته آموزشی')),
                ('gender', models.CharField(choices=[('w', 'مونث'), ('m', 'مذکر'), ('wm', 'مونث ومذکر')], max_length=2, verbose_name='جنسیت')),
                ('address', models.CharField(max_length=150, verbose_name='آدرس')),
            ],
        ),
        migrations.DeleteModel(
            name='YourModel',
        ),
    ]
