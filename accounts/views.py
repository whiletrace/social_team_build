from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from accounts import forms
from .forms import UserCreationForm

User = get_user_model()


class CreateUser(CreateView):
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
    model = settings.AUTH_USER_MODEL
    form_class = UserCreationForm

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

    if request.method == 'POST':
        form = forms.EditUserForm(data=request.POST, instance=user)
        # if form data is validated
        # form data is saved user updated
        if form.is_valid():
            form.save()
            # success message outputted informing of profiles update
            messages.add_message(request, messages.SUCCESS,
                                 'updated {} {}'.format
                                 (form.cleaned_data['first_name'],
                                  form.cleaned_data['last_name'])
                                 )
            # user redirected to profiles
            return HttpResponseRedirect(User().get_absolute_url())

    return render(request, 'user_profile/registration_form.html',
                  {'form':form,
                   'user':request.user
                   })


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
