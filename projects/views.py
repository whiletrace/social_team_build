from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import redirect, render
from django.http import request
from django.views import View
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.detail import (
    SingleObjectMixin,
    SingleObjectTemplateResponseMixin
    )
from django.forms import ModelChoiceField
from .forms import ProjectForm, project_position_formset, ApplicantForm
from .models import Applicant, Position, UserProject


class CreateProject(LoginRequiredMixin, CreateView):
    model = UserProject
    form_class = ProjectForm
    template_name = 'projects/project_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['position'] = project_position_formset(self.request.POST)
        else:
            context['position'] = project_position_formset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        position = context['position']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            created_project = form.save()
            if position.is_valid():
                position.instance = created_project
                position.save()

        return super().form_valid(form)


class ProjectDetail(DetailView):
    model = UserProject
    context_object_name = 'project'

    def get_queryset(self):
        query = UserProject.objects.all()

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['positions'] = Position.objects.filter(
            project_id=self.object.id)

        return context


def create_applicant(request, **kwargs):
    breakpoint()
    if request.method == 'POST':
        form = ApplicantForm(request.POST)

        if form.is_valid():
            breakpoint()
            position = Position.objects.get(id=kwargs['position'])
            data = {
                'applicant': request.user,
                'hired': False,
                'position': position
            }
            form.data = data
            form.save()
    else:
        form = ApplicantForm()
    return render(request, 'projects/userproject_detail.html', {'form': form} )
"""
class CreateApplicant(View):
    model = UserProject

    def get(self, request, *args, **kwargs):
        position = Position.objects.get(id=kwargs['position'])

        Applicant(applicant=self.request.user,
                  hired=False, position=position).save()
        messages.success(request, 'Your application has been saved')
        return redirect('projects:detail', pk=position.project.id)

"""


class ApplicantList(ListView):
    template_name = 'projects/applications.html'
    context_object_name = 'applicant_list'

    def get_queryset(self):
        created_by = self.request.user
        applicants = Applicant.objects.filter(
            position__project__created_by=created_by)
        return applicants

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new'] = self.get_queryset().last()
        context['accepted'] = self.get_queryset().filter(hired=True)
        context['rejected'] = self.get_queryset().filter(hired=False)
        return context


class ApplicantApprove(SingleObjectMixin, SingleObjectTemplateResponseMixin,
                       View):


    def get_object(self, queryset=None, **kwargs):
        applicant = Applicant.objects.get(id=kwargs['pk'])

        return applicant

    def get(self, request, *args, **kwargs):
        breakpoint()
        applicant = Applicant.objects.get(id=kwargs['pk'])
        applicant.hired = True
        applicant.save()
        messages.success(request, 'Your application has been saved')
        return redirect('projects:applicants')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['approved'] = self.approve()
        context['rejected'] = self.reject()
        return context


class ApplicantReject(SingleObjectMixin, SingleObjectTemplateResponseMixin,
                      View):


    def get(self, request, *args, **kwargs):
        applicant = Applicant.objects.get(id=kwargs['pk'])
        applicant.hired = False
        applicant.save()
        messages.success(request, 'Your application has been saved')
        return redirect('projects:applicants')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['approved'] = self.approve()
        context['rejected'] = self.reject()
        return context
