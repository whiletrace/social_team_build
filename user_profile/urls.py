from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from . import forms
# Todo: app specific URL:
#   create_user
#   edit_user
#   login
#  user_profile
#   edit user credentials
app_name = 'user_profile'


# Todo: URL
#  make main URL and namespacing
#  should be Profile pg
urlpatterns = [
    path('', views.user_detail, name='user_detail'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('user_register/', views.create_user, name='register_user'),
    path('login/', auth_views.LoginView.as_view(template_name='user_profile/login.html')),
    path('logout',auth_views.LogoutView.as_view()),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='user_profile/passwordChange.html')),

]