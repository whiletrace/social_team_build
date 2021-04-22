from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.views.generic import CreateView

from .forms import ProjectForm, project_position_formset
from .models import UserProject


class CreateProject(LoginRequiredMixin, CreateView):
    model = UserProject
    form_class = ProjectForm
    template_name = 'projects/project_form.html'

    def get_context_data(self, **kwargs):
        breakpoint()
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['position'] = project_position_formset(self.request.POST)
        else:
            context['position'] = project_position_formset()
        return context

    def form_valid(self, form):
        breakpoint()
        context = self.get_context_data()
        position = context['position']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            created_project = form.save()
            if position.is_valid():
                position.instance = created_project
                position.save()

        return super().form_valid(form)
