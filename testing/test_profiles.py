import pytest
from pytest_django.asserts import assertTemplateUsed
# test models
from profiles.models import Skills, UserProfile
from django.contrib.auth import get_user_model
from django.http import request
User = get_user_model()
@pytest.mark.django_db
def test_userprofile_model(make_test_profile):
    user = make_test_profile

    assert user.bio == 'this is a bio and its going to be outrageous'


@pytest.mark.django_db
def test_skills_model(make_skill):
    skill = make_skill

    assert isinstance(skill, Skills)


@pytest.mark.django_db
def test_many(make_test_profile):
    user = make_test_profile

    assert user.skills.all()[0].skill == 'Django'


# test views
@pytest.mark.django_db
def test_create_profile(client):
    response = client.get('/profiles/create_profile/')

    assertTemplateUsed(response, template_name='profiles/profile_form.html')
    assert response.status_code is 200


@pytest.mark.django_db
def test_post(client, make_test_user):
    user = make_test_user
    client.force_login(user)
    response = client.post('/profiles/create_profile/', {
        'created_by': make_test_user,
        'username': 'bigguy',
        'bio': 'this is bio and what of it',
        'avatar': 'a picture here'
        })

    assert UserProfile.objects.last().username == 'bigguy'


#test profile_update
@pytest.mark.django_db
def test_profile_update(client, make_test_profile):

    client.force_login(make_test_profile.created_by)
    data = {
        'created_by': make_test_profile.created_by,
        'username': 'unguy',
        'avatar':   'somepicture',
        'bio': 'I made a change to the bio and I am proud',
        'skills': 'skill1, skill2, skill3'
        }
    response = client.post('/profiles/edit_profile/', data=data)
    print(response.client)
    assert make_test_profile.username == 'unguy'