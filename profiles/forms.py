from django.forms.models import ModelForm, ModelMultipleChoiceField

from .models import UserProfile, Skills
# This is where profile forms will live


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'bio', 'avatar', 'skills']

        exclude = ['created_by']

# Todo create Profileform
#   modelform?
#   fields:
#       profilename
#       bio
#       skills list
#       avatar
