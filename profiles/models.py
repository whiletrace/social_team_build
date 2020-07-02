from django.conf import settings
from django.db import models
from django.urls import reverse

from accounts.views import ProfileView


# So this is going to be a model for profile
# non auth related user information

# Todo create model for User profile
#   fields:
#       Profile name : Charfield
#       email: EmailField(value already grabbed by User model)
#       skills: ManytoMany Field?
#

#Todo create funct Skills:
#  getorcreate for skills list
#  if user has skill get skill
#  if skill DoesNotExist createNewSkill
#  default list of skills to chose from


class UserProfile(models.Model):
    """
    UserProfile model defines database table
    that store user data not used in User Auth

    attr:
    user : modelOneToOneField :type obj
    bio : model.TextField :type obj
    avatar : model.ImageField :type obj

    """
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default="",
        on_delete=models.CASCADE
        )

    bio = models.TextField()
    avatar = models.ImageField(blank=True, upload_to='user_profile')

    def get_absolute_url(self):
        return reverse(ProfileView, kwargs={'pk':self.pk})
