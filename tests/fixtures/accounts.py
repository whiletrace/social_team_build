from django.contrib.auth import get_user_model
import pytest

User = get_user_model()


@pytest.fixture
def make_test_superuser():
    def _make_test_superuser():
        super_user = User.create_superuser(
            email='test@Qtest.com',
            first_name='super',
            last_name='user',
            date_of_birth='08/27/1975',
            password='@Password',
            )
        return super_user

    yield _make_test_superuser()
    User.close()


@pytest.fixture()
def make_test_user():
    def _make_test_user():
        user = User.create_user(
            email='test@Qtest.com',
            first_name='test',
            last_name='user',
            date_of_birth='08/27/1975',
            password='@Password',
            )
        return user

    yield _make_test_user()
    User.close()
