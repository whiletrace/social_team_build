from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView

from projects.models import Applicant
from .forms import ProfileForm
from .models import UserProfile

User = get_user_model()


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():

            form.instance.created_by = request.user

            skills = form.cleaned_data['skills']
            profile = form.save()
            for item in skills:
                profile.skills.add(item)
        return redirect('profiles:detail', pk=profile.id)

    else:
        form = ProfileForm()

    return render(request, 'profiles/profile_form.html', {'form':form})


def edit_profile(request):

    queryset = UserProfile.objects.all().prefetch_related('skills')
    profile = get_object_or_404(queryset, created_by=request.user)

    if request.method == 'GET':
        form = ProfileForm(instance=profile)

    elif request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.has_changed():
            form.save(commit=False)
            if form.is_valid():
                data = form.cleaned_data['skills']

                for item in data:
                    profile.skills.add(item)

            form.save()
        return redirect('profiles:detail', pk=profile.id)
    else:
        form = ProfileForm()

    return render(request, 'profiles/profile_form.html', {'form': form})


class ProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    queryset = UserProfile.objects.prefetch_related('skills').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['positions_applied'] = Applicant.objects.filter(
            applicant_id=self.request.user)
        return context

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
