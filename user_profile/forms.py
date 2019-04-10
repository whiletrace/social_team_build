from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.forms import modelformset_factory
from datetime import datetime
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
    """This form gathers and validates data used for user_creation

    form gathers:
    email
    password
    first_name
    last_name

    this form validates that both email and password
    match the corresponding verification fields

    if form validates data is saved to models.ProfileUser
    and a user is created
    """
    password1 = forms.CharField(label='password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='verify password',
                                widget=forms.PasswordInput)

    email1 = forms.CharField(label='email',
                             widget=forms.EmailInput)
    email2 = forms.CharField(label='verify email',
                             widget=forms.EmailInput)

    def clean_password2(self):
        """method verifies password1 and password2 fields match """
        cleaned_data = super().clean()
        password1 = cleaned_data('password1')
        password2 = cleaned_data('password2')
        validate_equal(password1, password2)
        return password2

    def clean_email2(self):
        """method verifies email1 and email2 fields match """
        cleaned_data = super().clean()
        email1 = cleaned_data('email1')
        email2 = cleaned_data('email2')
        validate_equal(email1, email2)
        return email2

    def save(self, commit=True):
        """Save the provided password in hashed format"""
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


class UserProfileForm(forms.ModelForm):
    """ model form for the user profile"""

    def clean_date_of_birth(self):
        cleaned_data = super().clean()
        date_of_birth = cleaned_data('date_of_birth')
        date_fmt = ('%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y')
        for fmt in date_fmt:
            try:
                datetime.strptime(date_of_birth, fmt)
            except ValueError:
                raise forms.ValidationError(
                    ' dates must be idn the format YYYY-MM-DD,'
                    'MM/DD/YYYY, or MM/DD/YY.', code='date_wrong_format'
                    )
        return date_of_birth

    def clean_bio(self):
        cleaned_data = super().clean()
        bio = cleaned_data('bio')
        if len(bio) < 10:
            raise forms.ValidationError('bio needs to be at '
                                        'least 10 char long',
                                        code='bio_not_min_length')
        return bio


    class Meta:
        model = models.UserProfile
        fields = [
            'date_of_birth',
            'bio',
            'avatar'
            ]


UserProfileFormSet = forms.modelformset_factory(
    model=models.UserProfile,
    form=UserProfileForm,

    )

UserProfileInlineFormSet = forms.inlineformset_factory(
    models.ProfileUser,
    models.UserProfile,
    extra=0,
    fields=('date_of_birth',
            'bio',
            'avatar'),
    formset=UserProfileFormSet,
    min_num=1,
    max_num=1,
    )


class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                'You must create a profile to login', code='Not-registered'
                )

class ChangePasswordForm(PasswordChangeForm):
    

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


