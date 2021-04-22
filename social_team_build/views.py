from django.views.generic import ListView

from projects.models import Position


class Home(ListView):
    model = Position

    def get_queryset(self):
        project_positions = Position.objects.all().select_related('project')

        return project_positions
