# when ready needed imports for URL router

from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [



    # display profile
    path('detail/<int:pk>/',
         views.ProfileView.as_view(template_name='profiles/detail.html'),
         name='detail'),

    # edit profile
    path('edit_profile/', views.edit_profile, name='edit_profile')

    ]
