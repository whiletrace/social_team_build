from django import forms
from django.forms.models import ModelForm, ModelMultipleChoiceField

from .models import Skills, UserProfile


# This is where profile forms will live

class ProfileForm(ModelForm):
    skills = ModelMultipleChoiceField(queryset=Skills.objects.all(), required=False)

    class Meta:
        model = UserProfile
        fields = ['username', 'bio', 'avatar']
        exclude = ['created_by']

# Todo create Profile_form
#   modelform?
#   fields:
#       profile_name
#       bio
#       skills list
#       avatar


class SkillsForm(ModelForm):
    skills_list = forms.CharField(strip=True, required=False)

    class Meta:
        model = Skills

        fields = ('skill',)

    def clean_skills_list(self):
        data = self.cleaned_data['skills_list']

        return data.split(',')
