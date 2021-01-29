from . import views

from django.contrib.auth import views as auth_views
from django.urls import path

app_name = 'accounts'

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        template_name='accounts/logout.html'), name='logout'
         ),

    path('user_register/', views.CreateUser.as_view(
        template_name='accounts/registration_form.html'),
         name='register_user'
         ),

    path('user_reg_succ/<int:pk>/', views.AccountDet.as_view(
        template_name='accounts/reg_success.html'
        ), name="register_success"),

    path('edit_account/', views.EditAccount.as_view(
        template_name='accounts/registration_form.html'),
        name='edit_user'
         ),

    path('change-password/', auth_views.PasswordChangeView.as_view(
        success_url='password_change_done',
        template_name='accounts/passwordChange.html'),
         name='change_password'
         ),

    path('change-password/password_change_done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='accounts/passwordChangeSuccess.html'),
         name='password_change_done'
         )
    ]
