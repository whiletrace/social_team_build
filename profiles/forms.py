from django.forms.models import ModelForm, ModelMultipleChoiceField

from .models import Skills, UserProfile


# This is where profile forms will live


class ProfileForm(ModelForm):
    skills = ModelMultipleChoiceField(queryset=Skills.objects.all())


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
