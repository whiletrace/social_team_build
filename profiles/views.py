from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView

from .forms import ProfileForm
from .models import Skills, UserProfile

User = get_user_model()


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            if request.user.is_authenticated:
                form.instance.created_by = request.user
                data = form.cleaned_data['skills'].split(',')
                profile = form.save()
                for item in data:
                    saved_skill = Skills.objects.get_or_create(skill=item)
                    profile.skills.add(saved_skill[0])

                redirect('profiles:detail', pk=profile.id)
            else:
                print('user is not authenticated')

    else:
        form = ProfileForm()

    return render(request, 'profiles/profile_form.html', {'form':form})


def edit_profile(request):

    queryset = UserProfile.objects.all().prefetch_related('skills')
    profile = get_object_or_404(queryset, created_by=request.user)
    skill_list = [skill.skill for skill in profile.skills.all()]

    if request.method == 'GET':
        form = ProfileForm(instance=profile,
                           initial={'skills': ', '.join(skill_list)})

    elif request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile,
                           initial={'skills':', '.join(skill_list)})
        if form.has_changed():
            form.save(commit=False)
            profile.skills.clear()
            if form.is_valid():
                data = form.cleaned_data['skills'].split(',')
                for item in data:
                    saved_skill = Skills.objects.get_or_create(skill=item)
                    profile.skills.add(saved_skill[0])
            form.save()
        return redirect('profiles:detail', pk=profile.id)
    else:
        form = ProfileForm()

    return render(request, 'profiles/profile_form.html', {'form': form})


class ProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    queryset = UserProfile.objects.prefetch_related('skills').all()

    def get_object(self, queryset=queryset):
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
