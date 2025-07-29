from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from projects.models import Position, UserProject


class Home(ListView):
    model = UserProject

    context_object_name = 'project_list'
    queryset = UserProject.objects.all()
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['position_list'] = Position.objects.order_by().values_list(
            'title', flat=True).distinct()
        return context


def project_search(request):
    term = request.GET.get('q')

    project_list = UserProject.objects.filter(
        Q(title__icontains=term) | Q(description__icontains=term))

    return render(request, 'home.html', {'project_list':project_list})

def position_filter(request):
    """
    view takes takes care of mineral group query logic and outputs to
    template index.html

    takes request object as argument queries the database for
    var group
    passes the value of parameter too index as context1
    :rtype: django.http.response.HttpResponse
    """
    position_list = Position.objects.order_by().values_list('title',
                                                            flat=True).distinct()
    position = request.GET.get('position')
    project_list = UserProject.objects.filter(position__title__exact=position)

    return render(request, 'home.html', {'project_list':project_list,
                                         'position':position,
                                         'position_list':position_list
                                         })
