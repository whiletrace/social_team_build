from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone
# Create your models here.
# Todo:create_model
#   fields:
#   first name
#   last name
#   date of birth
#   email
#   password
#   avatar image
#   bio



# ! Instead of referring to User directly,
# you should reference the user model
# using django.contrib.auth.get_user_model().


class ProfileUser(AbstractUser):
    """ Custom User model sets email as Unique_Identifier"""

    email = models.EmailField(

        verbose_name='email address',
        max_length=255,
        unique=True
        )

    REQUIRED_FIELDS = ('first_name', 'last_name')
    USERNAME_FIELD = 'email'


class UserProfile(models.Model):
    """
    UserProfile model holds user data not used in User Auth

    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )


    date_of_birth = models.DateField()
    bio = models.TextField()
    avatar = models.ImageField(blank=True)
