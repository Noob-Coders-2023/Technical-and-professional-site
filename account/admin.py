from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import SignupForm, CustomUserChangeForm
from .models import User
from django.contrib.auth.models import Group


# Register your models here.


class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = SignupForm
    list_display = ('email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('main', {"fields": ('email', 'phone_number', 'password')}),
        ('permission', {'fields': ('is_active', 'is_admin')})
    )
    search_fields = ('email','username')
    ordering = ('username',)
    filter_horizontal = ()

admin.site.unregister(Group)
admin.site.register(User,UserAdmin)