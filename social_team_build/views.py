from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from projects.models import UserProject


class Home(ListView):
    model = UserProject

    context_object_name = 'project_list'
    queryset = UserProject.objects.all()
    template_name = 'home.html'


def project_search(request):
    term = request.GET.get('q')

    project_list = UserProject.objects.filter(
        Q(title__icontains=term) | Q(description__icontains=term))

    return render(request, 'home.html', {'project_list':project_list})
