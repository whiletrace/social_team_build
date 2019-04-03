from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from django.utils import timezone
from .models import UserProfile
import os
from python_proj7 import settings
# Create your tests here.

# Todo: Test for model:
#   make sure user is created
#   user has correct attr
#   user is saved to database


class ModelTests(TestCase):

    def test_model(self):
        now = timezone.now()
        test_img = SimpleUploadedFile(name='test_photo.jpg',
                                      content=open(os.path.join(
                                          settings.BASE_DIR,
                                          'user_profile/static/user_profile'
                                          '/img/test_imag.jpg'),
                                          'rb').read()).close()

        user = UserProfile.objects.create(

            email='esm36@gmail.com',
            password='password',

            )
        import pdb; pdb.set_trace()
        self.assertLess(user.created_at, now)
# Todo: Test django forms
#   registration form
#   login form
#   edit profile form
#   edit password form
#   create setup: User
#   make sure fields are validating

# Todo: test django views:
#   create user
#   user profile
#   login
#   edit profile
#   edit password
