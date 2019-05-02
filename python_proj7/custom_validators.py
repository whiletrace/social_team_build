from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

#custom validator for the password
class SpecialCharacterValidator:

    def validate(self, password, user=None):
        if password.isalnum():
            raise ValidationError(
                _('Password needs to contain at least one special character'),
                code='no_special_characters'

                )

    def get_help_text(self):
        return _("Password needs to contain at"
                 "least one special character such as _@#$&")


class UpperLowerCaseValidator:

    def validate(self, password, user=None):
        if password.islower() or password.isupper():
            raise ValidationError(
                _('Password needs at least one upper and one lower case letter'),
                code='password_all_upper_or_lower_cased'

                )

    def get_help_text(self):
        return _("Password needs at least one upper and one lower case letter")


class ContainsNumberValidator:

    def validate(self, password, user=None):
        if password.isalpha():
            raise ValidationError(
                _('password needs to contain at least one number'),
                code='password_entirely_alphabetic'
                )

    def get_help_text(self):
        return _("password needs to contain at least one number")
