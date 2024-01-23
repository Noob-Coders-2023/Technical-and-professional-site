from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from extension.utils import jalali_converter, persian_number_converter


# Create your models here.
class Course(models.Model):
    STATUS_CHOICES = (
        ('n', 'شروع نشده است'),
        ('f', 'مهلت به پایان رسید')
    )
    GENDER_CHOICES = (
        ('w', 'مونث'),
        ('m', 'مذکر'),
        ('z', 'مونث ومذکر')
    )
    title = models.CharField(max_length=70, verbose_name='نام دوره')
    teacher = models.CharField(max_length=100, null=True, verbose_name='مدرس')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='آدرس دوره', blank=True, default=None)
    thumbnail = models.ImageField(verbose_name="تصویر", blank=True, default=None)
    description = models.TextField(verbose_name="محتوا")

    time = models.IntegerField(verbose_name="مدت زمان دوره")
    start = models.DateField(verbose_name="تاریخ شروع")
    end = models.DateField(verbose_name="تاریخ پایان")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    govermentcenter = models.CharField(max_length=150, verbose_name='نام مرکز دولتی')
    workshop = models.CharField(max_length=150, verbose_name='کارگاه/آموزشگاه')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='جنسیت')

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
    title = models.CharField(max_length=100, verbose_name='موضوع', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True)
    text = models.CharField(max_length=700, verbose_name='متن پیام', null=True, blank=True)

    class Meta:
        verbose_name = "پیام "
        verbose_name_plural = 'پیام ها'


class Choes_cours(models.Model):
    cours = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True)


class YourModel(models.Model):
    image = models.ImageField(upload_to='images/')
