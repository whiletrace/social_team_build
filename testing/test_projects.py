import pytest

from projects.models import UserProject


# test models


@pytest.mark.django_db
def test_project_model(make_test_project):
    project = make_test_project

    assert project.title == "BIGTITLE"


@pytest.mark.django_db
def test_create_project(client):
    response = client.get('/projects/create_project/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_post(client, make_test_user):
    user = make_test_user
    client.force_login(user)
    response = client.post('/projects/create_project/', {
        'created_by':make_test_user,
        'title':'bigguy',
        'description':'this is bio and what of it',
        'timeline':'whenever',
        'requirements':'so many requirements'
        })

    assert UserProject.objects.last().title == 'bigguy'
