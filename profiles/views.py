from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.views import User
from .models import UserProfile
from .forms import ProfileForm


# views will handle logic for each URL
# Todo: create profile
#    handle logic for skills:
#       display default list of skills
#       user choosing skills
#       user adding custom skills
#   render template:
#       form
#       return userprofile object


class CreateProfile(CreateView):
    model = UserProfile
    form_class = ProfileForm

'''
def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)'
'''



# Todo: edit profile
#    handle logic for skills:
#       display Users chosen/added skills
#       user deleting skills
#       user adding new skills
#       user updating skills
#   render template:
#       form
#       return userprofile object


class EditProfile(LoginRequiredMixin, UpdateView):
    model = UserProfile

    fields = ['bio', 'avatar']

    def get_object(self, queryset=None):
        return self.request.user


# Todo: Display Profile
#   view function or class?
#       method: GET
#       interface with database through model objects
#       read data from data base table (query)
#       render data from database table to template
#   search function:
#       search form
#       send search as database query
#       display results of query
#   render template:
#       database query
#       return query


class ProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile

    def get_object(self, queryset=None):
        """
        gets object whose data is to be outputted

        In this case that is request.user, request.user
        and user and all attr are made available to template
        through context

        :param queryset:
        :type queryset: object
        :return: User
        :rtype: user object
        """

        return self.request.user
