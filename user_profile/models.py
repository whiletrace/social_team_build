from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.urls import reverse


class ProfileUserManager(BaseUserManager):
    """Custom Profile manager logic used for user and superuser creation

    please see:
    https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#writing-a
    -manager-for-a-custom-user-model

    for further documentation

    """

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


class ProfileUser(AbstractBaseUser):
    """ Custom User model sets email as Unique_Identifier

    please see:
    https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#specifying
    -a-custom-user-model


    """
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
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = ProfileUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

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
