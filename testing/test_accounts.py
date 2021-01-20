import pytest

from pytest_django.asserts import assertTemplateUsed
from django.contrib.auth import get_user_model

from accounts.forms import UserCreationForm

# test models -createsuperuser

User = get_user_model()


@pytest.mark.django_db
def test_superuser_is_admin(make_test_superuser):
    jon = make_test_superuser

    assert jon.is_admin is True


@pytest.mark.django_db
def test_is_instance(make_test_superuser):
    jon = make_test_superuser

    assert isinstance(jon, User)

# create user



@pytest.mark.django_db
def test_user_not_admin(make_test_user):
    jon = make_test_user

    assert jon.is_admin is False


@pytest.mark.django_db
def test_user_instance(make_test_user):
    jon = make_test_user

    assert isinstance(jon, User)


# test User_form

@pytest.mark.django_db
def test_UserCreationForm_valid():
    form = UserCreationForm(data={'email': 'test@test.com',
                                  'email1': 'test@test.com',
                                  'first_name': 'test',
                                  'last_name': 'user',
                                  'date_of_birth': '08/27/1975',
                                  'password1': '@Password',
                                  'password2': "@Password",

                                  })
    assert form.is_valid()


@pytest.mark.django_db
def test_user_creation_form_invalid():
    form = UserCreationForm(data={'email': 'test@test.com',
                                  'email1': 'another@mako.com',
                                  'first_name': 'test',
                                  'last_name': 'user',
                                  'date_of_birth': '08/27/1975',
                                  'password1': '@Password',
                                  'password2':  '@Password'
                                  })

    assert form.is_valid() is False
    assert 'email1' in form.errors


def test_user_create(client):
    response = client.get('/accounts/user_register/')

    assertTemplateUsed(response, template_name='accounts/registration_form.html')
    assert response.status_code is 200


@pytest.mark.django_db
def test_post(client):
    response = client.post('/accounts/user_register/', {
        "email": 'test@test.com',
        "email1": 'test@test.com',
        "first_name": 'test',
        "last_name": 'user',
        "date_of_birth": '08/27/1975',
        "password1": 'Traceh28@52122',
        "password2": 'Traceh28@52122'
        })

    assert User.objects.last().first_name == 'test'
