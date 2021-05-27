from django.views.generic import ListView

from projects.models import UserProject


class Home(ListView):
    model = UserProject

    context_object_name = 'project_list'
    queryset = UserProject.objects.all()
    template_name = 'home.html'
