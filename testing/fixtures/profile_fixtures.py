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
