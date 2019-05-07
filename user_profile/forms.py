import gettext

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.password_validation import\
    (
    password_validators_help_texts, validate_password
    )

from . import models

user = get_user_model()
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
    email = forms.CharField(label='email',
                            widget=forms.EmailInput)
    email1 = forms.CharField(label='verify email',
                             widget=forms.EmailInput)

    password1 = forms.CharField(label='password',
                                widget=forms.PasswordInput,
                                help_text=password_validators_help_texts())
    password2 = forms.CharField(label='verify password',
                                widget=forms.PasswordInput)

    date_of_birth = forms.DateField(label='birthday',
                                    input_formats=['%Y-%m-%d',
                                                   '%m/%d/%Y',
                                                   '%m/%d/%y'
                                                   ],
                                    help_text='has to be in format YYYY-MM-DD, '
                                              'MM/DD/YYYY, MM/DD/YY'
                                    )

    def clean_password2(self):
        """method verifies password1 and password2 fields match """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        validate_password(password1, user=user)
        validate_equal(password1, password2)
        return password2

    def clean_email1(self):
        """method verifies email1 and email2 fields match """
        email = self.cleaned_data.get('email')
        email1 = self.cleaned_data.get('email1')
        validate_equal(email, email1)
        return email1

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
            'email1',
            'first_name',
            'last_name',
            'date_of_birth')


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = models.ProfileUser
        fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserProfileForm(forms.ModelForm):
    """ model form for the user profile"""
    bio = forms.CharField(help_text="This needs to be at least 10 char long",
                          widget=forms.Textarea)

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if len(bio) < 10:
            raise forms.ValidationError('bio needs to be at '
                                        'least 10 char long',
                                        code='bio_not_min_length')
        return bio

    class Meta:
        model = models.UserProfile
        fields = [
            'bio',
            'avatar'
            ]


class EditUserForm(UserCreationForm):
    """This form gathers and validates data used for editing

    form gathers:
    email
    first_name
    last_name


    if form validates data is saved to models.ProfileUser
    and a user is updated subclasses UserCreationForm
    """

    password1 = None
    password2 = None

    email1 = None
    email2 = None

    date_of_birth = forms.DateField(label='birthday',
                                    input_formats=['%Y-%m-%d',
                                                   '%m/%d/%Y',
                                                   '%m/%d/%y'
                                                   ],
                                    help_text="has to be in format YYYY-MM-DD,"
                                              " MM/DD/YYY, MM/DD/YY"
                                    )


    class Meta(UserCreationForm.Meta):
        exclude = ('password1', 'password2', 'email1')

    def save(self, commit=True):
        user = self.instance
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                'You must create a profile to login', code='Not-registered'
                )
