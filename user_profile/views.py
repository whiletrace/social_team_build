from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .models import ProfileUser, UserProfile

# since using custom auth and user model
# set reference to user model at view module scope
user = get_user_model()

# Create your views here.


def create_user(request):
    return HttpResponse('Hello this route is working and operational')

    # Todo: create_user:
#       instantiate registration form
#       validate form
#       if form validates
#       save form
#       redirect to profile pg
#       render template

def user_detail(request):
    return HttpResponse('this is going to be a profile view likely'
                        ' a class based view')
#Todo profile view:
#   default view
#   get user pk
#   for user data:
#   make user object available as context
#   info to be looped through in template
#   render template using proper url


def edit_profile(request):
    return HttpResponse('This is where you can edit your profile'
                        'dont forget to users pk')
#Todo edit profile view:
#   get user pk
#   for user data:
#   make user object available as context
#   info to be looped through in template
#   render template using proper url



