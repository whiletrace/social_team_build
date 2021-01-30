from django import forms
from django.forms.models import ModelForm

from .models import UserProfile


# This is where profile forms will live

class ProfileForm(ModelForm):
    skills = forms.CharField(strip=True, required=False)

    class Meta:
        model = UserProfile
        fields = ['username', 'bio', 'avatar']
        exclude = ['created_by']

    def __str__(self):
        return str.split(',')