from django.db import models
from account.models import User
from extension.utils import jalali_converter, persian_number_converter






# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(verbose_name="تصویر", blank=True, default=None)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = 'پست ها'

    def jcreated_at(self):
        return jalali_converter(self.created_at)

    jcreated_at.short_description = 'تاریخ ساخت'