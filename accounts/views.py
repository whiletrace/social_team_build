from django.conf import settings
from django.contrib.auth import get_user_model, authenticate, login

from django.http import request
from django.shortcuts import reverse, redirect
from django.views.generic import CreateView, DetailView, UpdateView

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


    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data.get('email'),
                            password=form.cleaned_data.get('password1'))
        if user is not None:
            login(request, user)

        return super().form_valid(form)


class AccountDet(DetailView):
    queryset = User.objects.all()

    def get_obj(self):
        obj = super().get_object()
        obj.id = self.request.user.id

        return obj


class EditAccount(UpdateView):
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
    model = User

    fields = ['email', 'first_name', 'last_name', 'date_of_birth']

    queryset = User.objects.all()

    def get_object(self, queryset=queryset):
        obj = queryset.get(id__exact=self.request.user.id)

        return obj


        # success message outputted informing of profiles update

        # user redirected to profiles


# class based view subclassed from django generic DetailView
