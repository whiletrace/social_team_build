import pytest


# test models


@pytest.mark.django_db
def test_project_model(make_test_project):
    project = make_test_project

    assert project.title == "BIGTITLE"


@pytest.mark.django_db
def test_create_project(client):
    response = client.get('/projects/create_project/')

    assert response.status_code == 200
