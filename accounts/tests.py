from django.test import Client, TestCase

from django.contrib.auth import authenticate, get_user_model, login

from .forms import *

User = get_user_model()



class TestSuperUser(TestCase):

    def setUp(self):
        superuser = User.objects.create_superuser(
            email='superuser@user.com',
            first_name='test',
            last_name='user',
            date_of_birth='1975-08-27',
            password='ThisisatestPassword@1234'
            )


    def test_superuser(self):
        john = User.objects.get(first_name='test')
        self.assertEqual(john.is_admin, True)


class TestUser(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            email='user@user.com',
            first_name='test',
            last_name='user',
            date_of_birth='1975-08-27',
            password='ThisisatestPassword@1234'
            )

    def test_user(self):
        john = User.objects.get(first_name='test')
        self.assertEqual(john.is_admin, False)


class TestUserLogin(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            email='user@user.com',
            first_name='test',
            last_name='user',
            date_of_birth='1975-08-27',
            password='ThisisatestPassword@1234'
            )

    def test_login(self):
        user = authenticate(username='user@user.com', password='ThisisatestPassword@1234')
        self.assertEqual(user.is_authenticated, True)


class TestUserCreationForm(TestCase):

    def test_form(self):
        form = UserCreationForm(data={
            "email": 'test@test.com',
            "email1": 'test@test.com',
            "first_name": 'test',
            "last_name": 'user',
            "date_of_birth": '08/27/1975',
            "password1": 'Traceh28@52122',
            "password2": 'Traceh28@52122'
            })
        self.assertTrue(form.is_valid())


class TestView(TestCase):

    def test_user_create(self):
        c = Client()
        response = c.get('/accounts/user_register/')
        self.assertTemplateUsed(response, template_name='accounts/layout.html')
        self.assertTemplateUsed(response, template_name='accounts/registration_form.html')
        self.assertEqual(response.status_code, 200)

    def test_post(self):

        c = Client()
        response = c.post('/accounts/user_register/', {
            "email": 'test@test.com',
            "email1": 'test@test.com',
            "first_name": 'test',
            "last_name": 'user',
            "date_of_birth": '08/27/1975',
            "password1": 'Traceh28@52122',
            "password2": 'Traceh28@52122'
            })
        self.assertRedirects(response, '/profiles/detail/')
