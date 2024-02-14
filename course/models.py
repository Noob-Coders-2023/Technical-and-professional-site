from django.contrib.auth.models import AbstractUser
from django.db import models
from account.models import User
from django.conf import settings
from extension.utils import jalali_converter, persian_number_converter
from django.core.exceptions import ValidationError


# Create your models here.
class Course(models.Model):
    STATUS_CHOICES = (
        ('n', 'شروع نشده است'),
        ('f', 'مهلت به پایان رسید')
    )
    GENDER_CHOICES = (
        ('w', 'زن'),
        ('m', 'مرد'),
        ('wm', 'زن و مرد')
    )
    title = models.CharField(max_length=70, verbose_name='نام دوره')
    teacher = models.CharField(max_length=100, null=True, verbose_name='مدرس')
    thumbnail = models.ImageField(upload_to='images/', verbose_name="تصویر", blank=True, null=True)
    description = models.TextField(verbose_name="محتوا")
    course_code = models.CharField(max_length=5, blank=True, null=True, verbose_name='کد درس')
    time = models.IntegerField(verbose_name="مدت زمان دوره")
    start = models.DateField(verbose_name="تاریخ شروع")
    end = models.DateField(verbose_name="تاریخ پایان")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت", default='n')
    govermentcenter = models.CharField(max_length=150, verbose_name='نام مرکز دولتی')
    workshop = models.CharField(max_length=150, verbose_name='کارگاه/آموزشگاه')
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, verbose_name='جنسیت')

    class Meta:
        verbose_name = "دوره"
        verbose_name_plural = 'دوره ها'

    def __str__(self):
        return self.title

    def jstart(self):
        return jalali_converter(self.start)

    jstart.short_description = 'تاریخ شروع'

    def jend(self):
        return jalali_converter(self.end)

    jend.short_description = 'تاریخ پایان'

    def ptime(self):
        return persian_number_converter(str(self.time))

    ptime.short_description = 'مدت زمان دوره'


class Conect(models.Model):
    SUBJECT_CHOICES = (
        ('sh', 'شکایت'),
        ('da', 'درخواست'),
        ('en', 'انتقاد'),

    )
    MEHVAR_CHOICES = (
        ('ma', 'مالی'),
        ('ed', 'اداری'),
        ('am', 'آموزش'),
        ('sa', 'سنجش و گواهینامه'),
        ('ta', 'تکریم ارباب رجوع'),

    )
    RELATIONSHIP_CHOICES = (
        ('rm', 'رییس مرکز'),
        ('ka', 'کارشناس آموزش'),
        ('ki', 'کارشناس it'),
        ('ma', 'معاون آموزش'),
        ('em', 'ارتباط با مربیان'),
    )
    first_lastname = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی', null=True, blank=True)
    national_code = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True, unique=True)
    title = models.CharField(max_length=100, verbose_name='موضوع', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True)
    text = models.CharField(max_length=700, verbose_name='متن پیام', null=True, blank=True)
    subject = models.CharField(max_length=2, choices=SUBJECT_CHOICES, verbose_name='موضوع', null=True, blank=True)
    mehvar = models.CharField(max_length=2, choices=MEHVAR_CHOICES, verbose_name='محور شکایت', null=True, blank=True)
    relationship=models.CharField(max_length=2,choices=RELATIONSHIP_CHOICES ,verbose_name='ارتباط با', null=True, blank=True)
    class Meta:
        verbose_name = "پیام "
        verbose_name_plural = 'پیام ها'


class Choes_cours(models.Model):
    cours = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    selection_time = models.DateField(auto_now_add=True, verbose_name='زمان انتخاب شده درس', null=True, blank=True)

    def jselection_time(self):
        return jalali_converter(self.selection_time)


# class YourModel(models.Model):
#     image = models.ImageField(upload_to='images/')

class Free_school(models.Model):
    GENDER_CHOICES = (
        ('w', 'مونث'),
        ('m', 'مذکر'),
        ('wm', 'مونث ومذکر')
    )
    name = models.CharField(max_length=40, verbose_name='نام آموزشگاه')
    founder = models.CharField(max_length=60, verbose_name='نام موسس')
    phone_number = models.CharField(max_length=11, verbose_name='شماره تماس')
    field = models.CharField(max_length=100, verbose_name='رشته آموزشی')
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, verbose_name='جنسیت')
    address = models.CharField(max_length=150, verbose_name='آدرس')
    location_link = models.CharField(max_length=255, blank=True, null=True, verbose_name='لینک گوگل مپ')

    class Meta:
        verbose_name = "آموزشگاه آزاد"
        verbose_name_plural = 'آموزشگاهای آزاد'
