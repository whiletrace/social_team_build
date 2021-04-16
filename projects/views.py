from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from .models import UserProject


class CreateProject(LoginRequiredMixin, CreateView):
    model = UserProject

    fields = ['title', 'description', 'timeline', 'requirements']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
