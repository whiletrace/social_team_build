from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .forms import ProfileForm
from .models import UserProfile


# views will handle logic for each URL
# Todo: create profile
#    handle logic for skills:
#
class CreateProfile(CreateView):
    model = UserProfile
    form_class = ProfileForm
    success_url = 'detail'

    def form_valid(self, form):
        import pdb;

        pdb.set_trace()
        chosen_skills = form.cleaned_data['skills']
        username = form.cleaned_data['username']
        bio = form.cleaned_data['bio']
        avatar = form.cleaned_data['avatar']

        profile = UserProfile(username=username, bio=bio, avatar=avatar,
                              created_by_id=self.request.user.pk)
        #profile.save()

        for skill in chosen_skills:
            profile.skills.add(skill)

        return super().form_valid(form)


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

    fields = ['bio', 'avatar', 'skills']

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return super().form_valid(form)


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

    queryset = model.objects.all()

    context_object_name = 'profile'

    def get_queryset(self):
        query = self.queryset.prefetch_related('skills')

        return query

    def get_object(self, queryset=None):
        import pdb;

        pdb.set_trace()
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
        #import pdb;pdb.set_trace()

        queryset = self.get_queryset()

        data = queryset.filter(created_by_id=self.request.user.pk).get()
        return data
