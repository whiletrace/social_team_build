from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.edit import FormView, UpdateView
from django.shortcuts import render

from .forms import ProfileForm, SkillsForm
from .models import UserProfile, Skills


# views will handle logic for each URL
# Todo: create profile
#    possible refactor
#    may just get rid of multichoice list
#   seems redundant
#   needs tests
#
def create_profile(request):

    new_skills_list = []

    if request.method == 'POST':
        form1 = ProfileForm(request.POST)
        form2 = SkillsForm(request.POST)

        if form1.is_valid():
            form1.instance.created_by = request.user
            profile = form1.save()
            profile.skills.set(form1.cleaned_data['skills'])

        if form2.is_valid():
            form2.instance.created_by = request.user
            data = form2.cleaned_data['skills_list']
            form2.save(commit=False)
            for entry in data:
                new_skill = Skills.objects.get_or_create(skill=entry)
                new_skills_list.append(new_skill[0])
            user_profile = UserProfile.objects.get(created_by=request.user.id)
            user_profile.skills.set(new_skills_list)
            form2.save_m2m()
    else:
        form1 = ProfileForm()
        form2 = SkillsForm()

    return render(request, './profiles/profile_form.html', {'form1': form1,
                                                            'form2': form2
                                                          })


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
    queryset = UserProfile.objects.all()
    context_object_name = 'profile'

    def get_object(self, queryset=queryset):
        breakpoint()
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

        data = queryset.prefetch_related('skills').filter(created_by_id=self.request.user.pk).get()
        return data
