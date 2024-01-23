from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post
from django.contrib import admin




# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'content', 'created_at')
    list_filter = ("title",)
    search_fields = ("user",'content')

    ordering = ['-created_at']

admin.site.register(Post, PostAdmin)





