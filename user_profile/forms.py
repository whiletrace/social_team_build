from django import forms

import gettext
from . import models

_ = gettext.gettext

#custom validator for the password


class Registration(forms.ModelForm):
    email = forms.EmailField(label='Enter your email', max_length=100)
    email_validation = forms.CharField(max_length=100)

    class Meta:
        model = models.UserProfile

        fields = [
            'first_name',
            'last_name',
            'email',
            'DOB',
            'avatar',
            'password'
            ]

# a cleaning method for making sure the fields match
# match there verification partners etc
    def pattern_clean(self, match1, match2):
        cleaned_data = super().clean()
        match1 = cleaned_data.get('{}'.format(match1))
        match2 = cleaned_data.get('{}'.format(match2))
        if match1 != match2:
            raise forms.ValidationError(_('{}'.format(match1) + 'needs to match'
                                          + '{}'.format(match2)))
# Todo: create forms
#   registration form:
#       fields:
#           first name
#           last name
#           email: validate emails match
#           date of birth validate: (YYYY-MM-DD, MM/DD/YYYY, or MM/DD/YY)
#           password: passwords must match
#               minimum password length of 14 characters.
#               must use of both uppercase and lowercase letters
#               must include one or more numerical digits
#               must include one or more of special characters, such as @, #, $
#               cannot contain the user name or parts of the user’s full name,
#               such as their first name
#           avatar image

#   Todo: change of password form:
#           password: passwords must match
#               minimum password length of 14 characters.
#               must use of both uppercase and lowercase letters
#               must include one or more numerical digits
#               must include one or more of special characters, such as @, #, $
#               cannot contain the user name or parts of the user’s full name,
#               such as their first name

#   Todo: Login_Form:
#       email
#       password

