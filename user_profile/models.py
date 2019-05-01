from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model

from django.conf import settings
from django.urls import reverse


# Create your models here.


class ProfileUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, date_of_birth,
                    password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, date_of_birth,
                         password):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth
            )
        user.is_admin = True
        user.save(using=self._db)
        return user


# ! Instead of referring to User directly,
# you should reference the user model
# using django.contrib.auth.get_user_model().
class ProfileUser(AbstractBaseUser):
    """ Custom User model sets email as Unique_Identifier"""

    email = models.EmailField(

        verbose_name='email address',
        max_length=255,
        unique=True
        )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth']

    objects = ProfileUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def get_absolute_url(self):
        return reverse('user_profile:user_detail')


class UserProfile(models.Model):
    """
    UserProfile model holds user data not used in User Auth

    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )

    bio = models.TextField()
    avatar = models.ImageField(blank=True, upload_to='user_profile')


"""
@receiver(post_save, sender=ProfileUser)
def signal(sender, instance, created, **kwargs):
    import pdb; pdb.set_trace()
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()

"""
