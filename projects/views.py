from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import redirect
from django.views import View
from django.views.generic import CreateView, DetailView

from .forms import ProjectForm, project_position_formset
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


class CreateApplicant(View):
    model = UserProject

    def get(self, request, *args, **kwargs):
        position = Position.objects.get(id=kwargs['position'])

        Applicant(applicant=self.request.user,
                  hired=False, position=position).save()
        messages.success(request, 'Your application has been saved')
        return redirect('projects:detail', pk=position.project.id)
