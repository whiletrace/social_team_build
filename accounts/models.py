from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.urls import reverse


class ProfileUserManager(BaseUserManager):
    """
    Custom manager that defines how user and superuser is created

    subclasses Djangos BaseUserManager

    methods: create_user
             create_superuser

    """

    def create_user(self, email, first_name, last_name, date_of_birth,
                    password=None):
        """
        method that defines user creation in app and in admin

        :param email:
        :type email: str
        :param first_name:
        :type first_name: str
        :param last_name:
        :type last_name: str
        :param date_of_birth:
        :type date_of_birth: datetime obj
        :param password:
        :type password: str
        :return: User
        :rtype: object
        """
        # if email is not provided exception thrown
        if not email:
            raise ValueError('Users must have an email address')

        # user is defined
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth
            )
        # password for user is set as attr for user
        user.set_password(password)
        # user instantiated and returned
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, date_of_birth,
                         password):
        """
        creates user and sets user as admin role

        :param email:
        :type email: str
        :param first_name:
        :type first_name: str
        :param last_name:
        :type last_name: str
        :param date_of_birth:
        :type date_of_birth: datetime obj
        :param password:
        :type password: str
        :return: SuperUser
        :rtype: object

        """
        # user is defined
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth
            )

        user.set_password(password)
        # user instantiated and returned
        user.save(using=self._db)
        # user set to admin
        user.is_admin = True
        # user instance is saved
        user.save(using=self._db)
        # user is returned
        return user


class NewUser(AbstractBaseUser):
    """
    Model class to define user instances

    Subclasses AbstractBaseUser and is the Auth model
    application uses to define database tables that stores all
    data essential to User authentication contains all
    necessary attr and methods to work with django admin

    :attr
    email : model.CharField :type obj
    first_name model.CharField :type obj
    last_name model.CharField :type obj
    date_of_birth: model.DateField :type obj
    is_active: model.BooleanField :type obj
    is_admin:model.BooleanField :type obj
    objects:  instance ProfileUserManager.:type obj

    :methods
     has_perm
     has_module_perms
     is_staff
     get_absolute_url
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
    REQUIRED_FIELDS = ['date_of_birth', 'first_name', 'last_name']

    objects = ProfileUserManager()

    # does object instance have permissions True
    def has_perm(self, perm, obj=None):
        return True

    # does object instance have app_level permissions True
    def has_module_perms(self, app_label):
        return True

    # does object instance have admin permission
    # reference to admin attr
    def is_staff(self):
        return self.is_admin

    def get_absolute_url(self):
        return reverse('accounts:register_success', kwargs={'pk': self.pk})
