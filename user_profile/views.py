from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from . import forms
from django.forms import ValidationError

# since using custom auth and user model
# set reference to user model at view module scope
User = get_user_model()

# Create your views here.


def user_create(request):

    form = forms.UserCreationForm
    profile_form = forms.UserProfileForm

    if request.method == 'POST':

        form = forms.UserCreationForm(request.POST)
        profile_form = forms.UserProfileForm(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            user = request.user
            profile_form.instance.user = user
            profile_form.save()

            messages.add_message(request, messages.SUCCESS,
                                 '{} {} your profile has been created'.format
                                 (form.cleaned_data['first_name'],
                                  form.cleaned_data['last_name'])
                                 )
            return HttpResponse("hey great job thanks for the nuggets of data")
        else:
            messages.add_message(request, messages.ERROR,
                                 message='could not create a user because{}'.
                                 format(print(form.errors)))

    return render(request, 'user_profile/profileForm.html',
                  {'form': form,
                   'profile_form': profile_form,
                   'user': request.user})


def edit_profile(request):

    user = request.user
    form = forms.EditUserForm(instance=user)
    profile_form = forms.UserProfileForm(instance=user)
    if request.method == 'POST':
        form = forms.EditUserForm(request.POST, instance=user)
        profile_form = forms.UserProfileForm(
            request.POST,
            instance=user
            )

        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.user = user
            profile_form.save()

            messages.add_message(request, messages.SUCCESS,
                                 'updated {} {}'.format
                                 (form.cleaned_data['first_name'],
                                  form.cleaned_data['last_name'])
                                 )
            return HttpResponseRedirect(User.get_absolute_url())
    return render(request, 'user_profile/profileForm.html',
                  {'form': form,
                   'profile_form': profile_form,
                   'user': user})

#using this just as a general pattern not trying to memorize things


class ProfileView(DetailView):
    model = User

    queryset = User.objects.all()

    def get_object(self, queryset=None):
        return self.request.user


'''
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user_profile'] = UserProfile.objects.all()

        return context
'''
