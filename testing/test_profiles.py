import pytest
from pytest_django.asserts import assertTemplateUsed
# test models
from profiles.models import Skills, UserProfile


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

    assertTemplateUsed(response, template_name='./profiles/profile_form.html')
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
