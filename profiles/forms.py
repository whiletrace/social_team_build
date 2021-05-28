from django import forms
from django.forms.models import ModelForm

from .models import Skills, UserProfile


# This is where profile forms will live

class ProfileForm(ModelForm):
    skills_list = forms.ModelMultipleChoiceField(queryset=Skills.objects.all(),
                                                 required=False,
                                                 to_field_name='skill',
                                                 help_text=
                                                 'to select multiple hold'
                                                 ' command for mac or control '
                                                 'for windows '
                                                 )

    skills = forms.CharField(strip=True, required=False,
                             help_text='multiple skills should '
                                       'be separated by comma')


    class Meta:
        model = UserProfile
        fields = ['username', 'bio', 'avatar']
        exclude = ['created_by']

    def __str__(self):
        return str.split(',')
