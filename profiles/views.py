from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.edit import FormView, UpdateView
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .forms import ProfileForm
from .models import UserProfile, Skills

User = get_user_model()


def create_profile(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            skills_list =[]
            breakpoint()
            if request.user.is_authenticated:
                form.instance.created_by = request.user
                data = form.cleaned_data['skills'].split(',')
                profile = form.save()
                for item in data:
                    saved_skill = Skills.objects.get_or_create(skill=item)
                    profile.skills.add(saved_skill[0])

            else:
                print('user is not authenticated')

    else:
        form = ProfileForm()

    return render(request, 'profiles/profile_form.html', {'form': form})


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

    fields = ['username', 'bio', 'avatar', 'skills']

    queryset = UserProfile.objects.all()

    def get_object(self, queryset=queryset):
        obj = queryset.get(id__exact=self.request.user.id)

        return obj


class ProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    queryset = UserProfile.objects.prefetch_related('skills').all()

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

        obj = queryset.get(created_by__id=self.request.user.id)
        return obj
