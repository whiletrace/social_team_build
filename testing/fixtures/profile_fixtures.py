import pytest

from profiles.models import Skills, UserProfile


@pytest.fixture
def make_skill():
    def _make_skill():
        skill = Skills(
            skill='Django'
            )
        skill.save()
        return skill
    yield _make_skill()


@pytest.fixture
def make_test_profile(make_test_user, make_skill):

    def _make_test_profile():

        test_profile = UserProfile(
            created_by=make_test_user,
            username= 'testuser',
            bio= 'this is a bio and its going to be outrageous',
            avatar= 'a picture here',

            )
        test_profile.save()
        test_profile.skills.add(make_skill)
        return test_profile
    yield _make_test_profile()