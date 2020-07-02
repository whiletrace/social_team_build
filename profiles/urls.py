# when ready needed imports for URL router

from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [
    # Todo: Url patterns for profile
    #   create profile
    path('create_profile', views.CreateProfile.as_view(
        template_name='profiles/profile_form.html'))
    #   edit profile
    #   Display profile
    #   Delete profile?

    ]
