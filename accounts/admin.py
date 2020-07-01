from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from accounts.models import NewUser
from profiles.models import UserProfile
from . import forms


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Users Profile'


class UserAdmin(BaseUserAdmin):

    add_form = forms.UserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'date_of_birth',
                    'is_admin')

    list_filter = ('is_admin',)

    fieldsets = (
        (None, {
            'fields': ('email', 'password')
            }),
        ('permissions', {'fields': ('is_active', 'is_admin')})
        )
    inlines = [UserProfileInline]

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'date_of_birth', 'email',
                       'email2', 'password1', 'password2')}),
        ('permissions', {'fields': ('is_active', 'is_admin')}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Register your models here.
admin.site.register(NewUser, UserAdmin)
admin.site.unregister(Group)
