from django.contrib import admin
from .models import Course,Conect,Choes_cours
from django.contrib import admin




# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'ptime', 'jstart', 'jend', 'status','teacher','gender')
    list_filter = ("status",)
    search_fields = ("title",'description')
    # prepopulated_fields = {'slug':('title',)}
    ordering = ['-status','start']

admin.site.register(Course, CourseAdmin)


class ConectAdmin (admin.ModelAdmin):
    list_display = ('title','text')



admin.site.register(Conect, ConectAdmin)




