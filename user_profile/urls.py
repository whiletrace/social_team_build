from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import ProfileView



app_name = 'user_profile'

urlpatterns = [
    path('',
         ProfileView.as_view(template_name='user_profile/detail.html'),
         name='user_detail'),

    path('edit_profile/',
         views.edit_profile, name='edit_profile'),

    path('user_register/', views.user_create, name='register_user'),

    path('login/',
         auth_views.LoginView.as_view(template_name='user_profile/login.html',
                                      redirect_field_name='goto'),
         name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('change-password/',
         auth_views.PasswordChangeView.as_view(
             template_name='user_profile/passwordChange.html'
             )
         ),
]



