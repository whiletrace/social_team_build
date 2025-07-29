import pytest
from django.contrib.messages import get_messages

from projects.models import UserProject, Position, Applicant


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


@pytest.mark.django_db
def test_project_owner_cannot_apply_to_own_position(client, make_test_user):
    """Test that project owners cannot apply to positions in their own projects"""
    user = make_test_user
    client.force_login(user)
    
    # Create a project
    project = UserProject.objects.create(
        created_by=user,
        title='Test Project',
        description='Test description',
        timeline='1 month',
        requirements='Python skills'
    )
    
    # Create a position for the project
    position = Position.objects.create(
        project=project,
        title='Developer',
        description='Python developer needed'
    )
    
    # Attempt to apply to own position
    response = client.post(f'/projects/create_applicant/{position.id}/', {
        'position': position.id,
        'hired': False
    })
    
    # Should redirect back to project detail
    assert response.status_code == 302
    
    # Should not create an application
    assert Applicant.objects.filter(applicant=user, position=position).count() == 0
    
    # Should show error message
    messages = list(get_messages(response.wsgi_request))
    assert any('cannot apply to positions in your own project' in str(message) for message in messages)
