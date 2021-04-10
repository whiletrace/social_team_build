import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

pytest_plugins = ['testing.fixtures.profile_fixtures',
                  'testing.fixtures.project_fixture']


@pytest.fixture
def make_test_superuser():
    def _make_test_superuser():
        super_user = User.objects.create_superuser(
            email='test@Qtest.com',
            first_name='super',
            last_name='user',
            date_of_birth='1975-08-22',
            password='@Password',
            )
        return super_user

    yield _make_test_superuser()


@pytest.fixture()
def make_test_user():
    def _make_test_user():
        user = User.objects.create_user(
            email='test@Qtest.com',
            first_name='test',
            last_name='user',
            date_of_birth='1975-08-22',
            password='@Password',
            )
        return user

    yield _make_test_user()


