import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
from django.conf import settings
from pytest_django.asserts import assertTemplateUsed

from conftest import make_test_user
# test models
from profiles.models import Skills, UserProfile

User = get_user_model()

@pytest.mark.django_db
def test_skills_model(make_skill):
    skill = make_skill

    assert isinstance(skill, Skills)

@pytest.mark.django_db
def test_many(make_test_user, make_skill):
    user = make_test_user
    skill = make_skill
    profile = UserProfile.objects.get(created_by=user)
    profile.skills.add(skill)
    assert profile.skills.all()[0].skill == 'Django'

#test profile_update
@pytest.mark.django_db
def test_update_url(client, make_test_user):
    user = make_test_user
    client.force_login(user)

    response = client.get('/profiles/edit_profile/')
    print(response.client)
    assert response.status_code == 200

#test profile_update
@pytest.mark.django_db
def test_update_profile(client, make_test_user):
    user = make_test_user

    client.force_login(user)
    profile= UserProfile.objects.get(created_by=user)
    data = {
        'username': 'unguy',
        'bio': 'this is a bio and its going to be good',
        }

    response = client.post(reverse('profiles:edit_profile'), data)
    profile.refresh_from_db()
    assert profile.username == 'unguy'

# Test signal functionality
@pytest.mark.django_db
def test_profile_created_when_user_created(make_test_user):
    """Test that UserProfile is automatically created when a new user is created"""
    # Create a new user
    user = make_test_user
    
    # Assert that a profile was automatically created
    assert UserProfile.objects.filter(created_by=user).exists()
    profile = UserProfile.objects.get(created_by=user)
    assert profile.created_by == user

# Test model field relationship
@pytest.mark.django_db
def test_created_by_field_is_onetoonefield():
    """Test that created_by field is a OneToOneField with AUTH_USER_MODEL"""
    # Get the field from the model
    created_by_field = UserProfile._meta.get_field('created_by')
    
    # Assert it's a OneToOneField
    assert isinstance(created_by_field, models.OneToOneField)
    
    # Assert it references the AUTH_USER_MODEL
    assert created_by_field.related_model == User
    assert created_by_field.related_model._meta.label == settings.AUTH_USER_MODEL
