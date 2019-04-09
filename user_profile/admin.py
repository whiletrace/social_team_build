from django import forms
from django.contrib import admin
from . import forms
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

    add_form = forms.UserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'is_admin', 'is_active')
    list_filter = ('is_active', 'is_admin',)

    fieldsets = (
        (None, {
            'fields': ('email', 'password')
            }),
        ('profile info', {'fields': ('first_name,', 'last_name')}),
        ('permissions', {'fields':('is_active', 'is_admin', 'is_superuser')})
    )
    inlines = [UserProfileInline]

    search_fields = ('email',)
    ordering = ['email']
    filter_horizontal = ()


# Register your models here.
admin.site.register(ProfileUser, UserAdmin)
admin.site.unregister(Group)



