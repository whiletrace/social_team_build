from django.conf import settings
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver



# So this is going to be a model for profile
# non auth related user information

class Skills(models.Model):
    skill = models.CharField(blank=True, default='', max_length=50)

    def __str__(self):
        return self.skill


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
        default="createdby", unique=True,
        on_delete=models.CASCADE
        )
    username = models.CharField(blank=True, default='', max_length=50)
    bio = models.TextField(blank=True, default='')
    avatar = models.ImageField(blank=True, upload_to='media')

    skills = models.ManyToManyField('Skills', blank=True,
                                    related_name='profile_skills')

    def get_absolute_url(self):
        return reverse('profiles:detail', kwargs={'pk': self.pk})



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def my_handlers(sender, created, instance, **kwargs):
    if created and not kwargs.get('raw', False):
        UserProfile.objects.get_or_create(created_by=instance)


