from django.conf import settings
from django.db import models
from django.urls import reverse


# So this is going to be a model for profile
# non auth related user information

class Skills(models.Model):
    skill = models.CharField(blank=True, default='', max_length=25)


class UserProfile(models.Model):
    """
    UserProfile model defines database table
    that store user data not used in User Auth

    attr:
    user : modelOneToOneField :type obj
    bio : model.TextField :type obj
    avatar : model.ImageField :type obj

    """
    created_by = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        default="", unique=True,
        on_delete=models.CASCADE
        )
    username = models.CharField(blank=True, default='', max_length=50)
    bio = models.TextField(blank=True, default='')
    avatar = models.ImageField(blank=True, upload_to='media')

    skills = models.ManyToManyField('Skills', blank=True,
                                    related_name='profile_skills')

    def get_absolute_url(self):
        return reverse('profiles:detail', kwargs={'pk': self.pk})



