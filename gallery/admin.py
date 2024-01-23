from django.contrib import admin
from django.contrib import admin
from .models import Image
# Register your models here.


class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_preview')
    search_fields = ('title', 'description')

    def image_preview(self, obj):
        return obj.image.url if obj.image else ''

    image_preview.short_description = 'تصویر پیش‌ نمایش'

admin.site.register(Image, GalleryItemAdmin)