from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView

from . import forms

# since using custom auth and user model
# set reference to user model at view module scope
User = get_user_model()


# Create your views here.


def user_create(request):
    """
    view handles logic concerning initial user instantiation

    instantiates UserCreation and UserProfile forms
    passes forms to template as contexts if forms validates
    save method called on UserCreation form and an user object
    is instantiated form data is collected in user is authenticated
    and logged in user instance is passed to UserProfile form
    and data is saved created UserProfile instance
    which is tied to User instance through a one-to-one field
    on UserProfile model. View returns a HttpResponse obj whose
    content is filled with the call to render which in turn calls
    django.template.loader.render_to_string()with the passed arguments.

    :var
    email: form.data :type obj
    raw_password: form.data :type obj
    user = request.user

    :methods:
    authenticate
    login

    :param request:
    :type request: http request Obj
    :return: render
    :rtype: Http response obj

    """
    # for instantiation
    form = forms.UserCreationForm
    profile_form = forms.UserProfileForm

    # if the request action is post
    if request.method == 'POST':
        # request object with post method passed to forms as param
        form = forms.UserCreationForm(request.POST)
        # profile form has additional request obj method because uploading file
        profile_form = forms.UserProfileForm(request.POST, request.FILES)

        #  if forms pass all validations
        if form.is_valid() and profile_form.is_valid():
            # UserCreationForm save method is called
            # user is instantiated
            form.save()
            # form data
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            # authenticate user based on input
            user = authenticate(email=email, password=raw_password)
            # user is logged in
            login(request, user)
            # user is set to request.user object
            user = request.user
            # user passed to UserProfileForm
            profile_form.instance.user = user
            # UserProfileForm data is saved to database
            # UserProfile obj instance instantiated
            profile_form.save()

            # success message displayed to User
            messages.add_message(request, messages.SUCCESS,
                                 '{} {} your profile has been created'.format
                                 (form.cleaned_data['first_name'],
                                  form.cleaned_data['last_name'])
                                 )
            # User redirected to Profile
            return HttpResponseRedirect(User().get_absolute_url())

    return render(request, 'user_profile/profileForm.html',
                  {'form': form,
                   'profile_form': profile_form,
                   'user':request.user
                   })


@login_required
def edit_profile(request):
    """
    view handles logic concerning update user data

    instantiates EditUser and UserProfile forms
    retrieves user data and populates forms with data if forms validates
    save method called and user object attributes are updated
    View returns a HttpResponse obj whose
    content is filled with the call to render() which in turn calls
    django.template.loader.render_to_string() with the passed arguments.

    :param request:
    :type request: http request Obj
    :return: render
    :rtype: Http response obj

    :var
    user : request. user:type obj
    form : forms.modelform :type obj
    profile_form :forms.modelform :type obj
    """
    # form instantiation and instance set to user
    # forms retrieve user data from models
    # fields are populated
    user = request.user
    form = forms.EditUserForm(instance=user)
    profile_form = forms.UserProfileForm(instance=user.userprofile)

    if request.method == 'POST':
        form = forms.EditUserForm(data=request.POST, instance=user)
        profile_form = forms.UserProfileForm(
            request.POST,
            request.FILES,
            instance=user.userprofile
            )
        # if form data is validated
        # form data is saved user and profileuser attr are updated
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            # success message outputted informing of profile update
            messages.add_message(request, messages.SUCCESS,
                                 'updated {} {}'.format
                                 (form.cleaned_data['first_name'],
                                  form.cleaned_data['last_name'])
                                 )
            # user redirected to profile
            return HttpResponseRedirect(User().get_absolute_url())

    return render(request, 'user_profile/profileForm.html',
                  {'form':form,
                   'profile_form':profile_form,
                   'user':request.user
                   })


#using this just as a general pattern not trying to memorize things

# class based view subclassed from django generic DetailView
class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    queryset = User.objects.all()

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
