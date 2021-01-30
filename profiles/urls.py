# when ready needed imports for URL router

from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [

    # create profile
    path('create_profile/', views.create_profile, name='create_profile'),

    # display profile
    path('detail/<int:pk>/',
         views.ProfileView.as_view(template_name='profiles/detail.html'),
         name='detail'),

    # edit profile
    path('edit_profile/', views.EditProfile.as_view(
        template_name='profiles/profile_form.html'
        ), name='edit_profile')

    ]
