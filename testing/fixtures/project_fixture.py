import pytest

from projects.models import UserProject


@pytest.fixture
def make_test_project(make_test_user):
    def _make_test_project():
        test_project = UserProject(
            created_by=make_test_user,
            title='BIGTITLE',
            description='this is a bio and its going to be outrageous',
            timeline='a picture here',
            requirements='this is going to be a requirement'

            )
        test_project.save()

        return test_project

    yield _make_test_project()
