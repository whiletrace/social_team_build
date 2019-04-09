from django import forms

import gettext
from . import models

_ = gettext.gettext


# utility function for field clean and validation
# used in validations of email and password
# because the comparison operations are identical
def validate_equal(arg1, arg2):
    if arg1 != arg2:
        raise forms.ValidationError('{} and {} needs to match'
                                    .format(arg1, arg2))


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='verify password',
                                widget=forms.PasswordInput)

    email1 = forms.CharField(label='email',
                             widget=forms.EmailInput)
    email2 = forms.CharField(label='verify email',
                             widget=forms.EmailInput)

    def clean_password2(self):
        cleaned_data = super().clean()
        password1 = cleaned_data('password1')
        password2 = cleaned_data('password2')
        validate_equal(password1, password2)
        return password2

    def clean_email2(self):
        cleaned_data = super().clean()
        email1 = cleaned_data('email1')
        email2 = cleaned_data('email2')
        validate_equal(email1, email2)
        return email2

    # a cleaning method for making sure the fields
    # match there verification partners etc
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class Meta:
        model = models.ProfileUser
        fields = (
            'email',
            'first_name',
            'last_name',)


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


