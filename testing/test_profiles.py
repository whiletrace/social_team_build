import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

# test models
from profiles.models import Skills, UserProfile

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
        'created_by':make_test_user,
        'username':'bigguy',
        'bio':'this is bio and what of it',
        'avatar':'a picture here'
        })

    assert UserProfile.objects.last().username == 'bigguy'


#test profile_update
@pytest.mark.django_db
def test_update_URL(client, make_test_profile):
    client.force_login(make_test_profile.created_by)

    response = client.get('/profiles/edit_profile/')
    print(response.client)
    assert response.status_code == 200


#test profile_update
@pytest.mark.django_db
def test_update_profile(client, make_test_user, make_test_profile):

    client.force_login(make_test_user)
    new_profile = make_test_profile

    data = {
        'username': 'unguy',
        'bio': 'this is a bio and its going to be good',
        }

    response = client.post(reverse('profiles:edit_profile'), data)
    new_profile.refresh_from_db()
    assert new_profile.username == 'unguy'
