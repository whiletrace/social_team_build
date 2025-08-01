from django import forms
from django.forms.models import ModelForm

from .models import Skills, UserProfile


# This is where profile forms will live

class ProfileForm(ModelForm):
    skills = forms.ModelMultipleChoiceField(queryset=Skills.objects.all(),
                                            required=False,
                                            to_field_name='skill',
                                            help_text='To select multiple items, hold Command (Mac) or Control (Windows)'
                                            )


    class Meta:
        model = UserProfile
        fields = ['username', 'bio', 'avatar']
        exclude = ['created_by']
