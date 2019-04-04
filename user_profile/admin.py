from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import ProfileUser, UserProfile


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Users Profile'


class UserAdmin(BaseUserAdmin):
    inlines = [UserProfileInline]

    ordering = ['email']

# Register your models here.
admin.site.register(ProfileUser, UserAdmin)
admin.site.unregister(Group)



