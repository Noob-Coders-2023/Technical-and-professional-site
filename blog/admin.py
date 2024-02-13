
from .models import Course, Free_school,Conect
from django.contrib import admin


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'ptime', 'jstart', 'jend', 'status', 'teacher', 'gender')
    list_filter = ("status",)
    search_fields = ("title", 'description')
    # prepopulated_fields = {'slug':('title',)}
    ordering = ['-status', 'start']


admin.site.register(Course, CourseAdmin)


class ConectAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')

admin.site.register(Conect, ConectAdmin)


class AcademiAdmin(admin.ModelAdmin):
    list_display = ('name', 'founder', 'phone_number', 'field', 'gender', 'address')
    list_filter =('name',)
    search_fields = ("founder", 'name')


admin.site.register(Free_school, AcademiAdmin)

