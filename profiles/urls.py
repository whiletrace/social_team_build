# when ready needed imports for URL router

from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [

    # display profile
    path('detail/', views.ProfileView.as_view(template_name='profiles/detail.html'),
         name='detail'),
    # create profile
    path('create_profile/', views.CreateProfile.as_view(
        template_name='profiles/profile_form.html')),
    # edit profile
    path('edit_profile/', views.EditProfile.as_view(
        template_name='profiles/profile_form.html'
        ), name='edit_profile')

    #   Delete profile?

    ]
