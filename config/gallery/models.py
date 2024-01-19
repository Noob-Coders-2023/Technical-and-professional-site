from django.db import models


# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title
