import pytest


# test models


@pytest.mark.django_db
def test_Project_model(make_test_project):
    project = make_test_project

    assert project.title == "BIGTITLE"
