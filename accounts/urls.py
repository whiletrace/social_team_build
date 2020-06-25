from django.contrib.auth import views as auth_views
from django.urls import path

app_name = 'accounts'

from . import views

urlpatterns = [
    path('',
         views.ProfileView.as_view(template_name='user_profile/detail.html'),
         name='user_detail'),

    path('edit_profile/',
         views.edit_profile, name='edit_profile'),

    path('user_register/', views.user_create, name='register_user'),

    path('login/',
         auth_views.LoginView.as_view(template_name='accounts/login.html',
                                      redirect_field_name='goto'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='accounts/logout.html'), name='logout'),

    path('change-password/', auth_views.PasswordChangeView.as_view(
        success_url='password_change_done',
        template_name='user_profile/passwordChange.html'),
         name='change_password'
         ),

    path('change-password/password_change_done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='user_profile/passwordChangeSuccess.html'),
         name='password_change_done')
    ]
