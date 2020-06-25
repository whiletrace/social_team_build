from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.password_validation import (
    password_validators_help_texts, validate_password,

    )

from . import models

User = get_user_model()


def validate_equal(arg1, arg2):
    if arg1 != arg2:
        raise forms.ValidationError('passwords needs to match')


class UserCreationForm(forms.ModelForm):
    """
    model form that is tasked with gathering user_data

    If valid Data gathered is cleaned passed to models.ProfileUser
    and a authenticated User object in instantiated if user data is not valid
    form will display help text to user so user can correct errors in input
    defines UserCreation form fields which are django objects, field,
    labels, field widgets as well as methods for data validation for
    fields as well as a save method that is unique for a user instance.

    :var:
    email: forms.field :type: obj
    email1: forms.field :type: obj
    password: forms.field :type: obj
    password: forms.field :type: obj
    date_of_birth: forms.field :type: obj

    methods:
    clean_password2
    clean_email1
    save
    """

    # form field definitions
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

        """
        passes user input to password validators

        logic for validation of two conditions in this
        method 1. validates that password does not contain
        users first_name or last_name if condition met
        raise Validation error and message is conveyed to user
        if condition is not met
        password input auth django auth validators
        input compared to determine That password1 and password 2 are equal
        if condition is not met validation error
        is raised and message is conveyed to user

        :var:
        first_name: form.field.data Type: Obj
        last_name: form.field.data. Type: Obj
        password1: form.field.data.Type: Obj
        password2 :form.field.data. Type: Obj

        :return: password2: form.field.data
        :rtype: Obj
        """

        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        # conditional statement to test whether uses first_name
        # or last_name is contained within password input
        if first_name in password2 or last_name in password2:
            # if yes validation error raised
            raise forms.ValidationError(
                # message passed to user
                'password cannot contain first or last name ')
        # if condition is not met
        else:
            # password is passed to django auth password validators
            # defined in social_team_build/settings
            validate_password(password1, user=User)
            # util function see top of module
            validate_equal(password1, password2)
        return password2

    def clean_email1(self):
        """
        method for comparison of data from field email and email1

        input compared to determine That password1 and password 2 are equal
        if condition is not met validation error
        is raised and message is conveyed to user

        :var
        email: form.field.data type: obj
        email1 form.field.data type obj

        :return: email1: form.field.data
        :rtype: Obj
        """
        email = self.cleaned_data.get('email')
        email1 = self.cleaned_data.get('email1')
        validate_equal(email, email1)
        return email1

    def save(self, commit=True):
        """
        Save User.instance object if commit=True

        :var: user :type obj

        :param commit: :type function
        :type commit:  :type function
        :return: User instance
        :rtype: obj
        """

        user = super().save(commit=False)
        # relates password instance to user instance generated
        # after form validation and user is instantiated
        user.set_password(self.cleaned_data["password1"])
        # if database commit for formal def
        # see SQL commit
        # If commit user instance is saved
        if commit:
            user.save()
        # user object is returned
        return user


    # Meta class Declares fields included in form
    # defines relationship with associated model class
    class Meta:
        model = models.NewUser
        fields = (
            'email',
            'email1',
            'first_name',
            'last_name',
            'date_of_birth')


class UserChangeForm(forms.ModelForm):
    """
    A form for updating users, implemented primarily in Admin

    Includes all the fields on the user,
    but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()


    # Meta class Declares fields included in form
    # defines relationship with associated model class
    class Meta:
        model = models.NewUser
        fields = (
            'email',
            'password',
            'date_of_birth',
            'is_active',
            'is_admin'
            )


    def clean_password(self):
        """

        :return:
        :rtype:
        """
        return self.initial["password"]


class UserProfileForm(forms.ModelForm):
    """
    model form for the user profile

    this collects user data not related to auth
    which is bio info which is a textfield
    and avatar which is a image field
    class defines form fields, and
    methods for form field validation

    :var
      bio: forms.field :type Obj
      avatar forms.field :type Obj

    methods:
    clean_bio
    """

    # defines form bio form field
    bio = forms.CharField(help_text="This needs to be at least 10 char long",
                          widget=forms.Textarea)

    def clean_bio(self):
        """
        method gets user inputted data and makes sure 10 char long

        if user input is less than 10 chars long
        validation error is raised and message
        conveyed to user

         :var
         bio: form.field.data

        :return: form.field. data
        :rtype: obj
        """

        # user inputted data
        bio = self.cleaned_data.get('bio')
        # if bio data length less than 10
        if len(bio) < 10:
            # form validation error is raised and message
            # is conveyed to user
            raise forms.ValidationError('bio needs to be at '
                                        'least 10 char long',
                                        code='bio_not_min_length')
        # form field data is returned
        return bio


    # Meta class Declares fields included in form
    # defines relationship with associated model clas
    class Meta:
        model = models.UserProfile
        fields = [
            'bio',
            'avatar'
            ]


class EditUserForm(UserCreationForm):
    """
    model form to gather data for user edit profile

    If valid Data gathered is cleaned passed to models.ProfileUser
    and a authenticated User object in updated if user data is not valid
    form will display help text to user so user can correct errors in input
    subclasses UserCreation form fields which are django objects, field,
    labels,  excludes passwords as well as verification email
    field widgets. The methods for data validation for
    fields  is inherited from UserCreation field
    as well as a save method that is unique for a user instance.

    :var:
    email: forms.field :type: obj
    email1: forms.field :type: obj
    password: forms.field :type: obj
    password: forms.field :type: obj
    date_of_birth: forms.field :type: obj

    methods:

    save
    """

    # field exclusions
    password1 = None
    password2 = None

    email1 = None
    email2 = None
    # field for dob input formats and help text
    date_of_birth = forms.DateField(label='birthday',
                                    input_formats=['%Y-%m-%d',
                                                   '%m/%d/%Y',
                                                   '%m/%d/%y'
                                                   ],
                                    help_text="has to be in format YYYY-MM-DD,"
                                              " MM/DD/YYY, MM/DD/YY"
                                    )


    # Meta class Declares fields excluded
    # subclasses UserCreationForm.meta
    class Meta(UserCreationForm.Meta):
        exclude = ('password1',
                   'password2',
                   'email1')


    def save(self, commit=True):
        """
        overrides save method from
        UserCreation form because not processing password
        so now on commit  user object is updated
        and returned

        :param commit:
        :type commit:
        :return: User
        :rtype: object
        """
        user = self.instance
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    """
    model form handles user data gathering
    for  User login

    """

    def confirm_login_allowed(self, user):
        """
        handles verification of user input
        are not valid raises validation error

        :param user:
        :type user: Object

        """
        # comparison of input data to known credentials
        # if credentials do not match message is outputted
        # and user remains anonymous
        # if credentials match user is authenticated
        if not user.is_active:
            raise forms.ValidationError(
                'You must create a profile to login', code='Not-registered'
                )
