from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.detail import (
    SingleObjectMixin,
    SingleObjectTemplateResponseMixin
    )

from .forms import ApplicantForm, ProjectForm, project_position_formset
from .models import Applicant, Position, UserProject


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            breakpoint()
            form.instance.created_by = request.user
            saved_project = form.save()
            project = UserProject.objects.get(id=saved_project.id)
            formset = project_position_formset(request.POST, instance=project)
            if formset.is_valid():
                formset.save()
            return redirect('home')

    else:
        form = ProjectForm()
        formset = project_position_formset()

    return render(request, 'projects/project_form.html', {'form':form,
                                                          'formset':formset
                                                          })


'''
User = get_user_model()


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            if request.user.is_authenticated:
                form.instance.created_by = request.user
                data = form.cleaned_data['skills'].split(',')
                profile = form.save()
                for item in data:
                    saved_skill = Skills.objects.get_or_create(skill=item)
                    profile.skills.add(saved_skill[0])

                redirect('profiles:detail', pk=profile.id)
            else:
                print('user is not authenticated')

    else:
        form = ProfileForm()

    return render(request, 'profiles/profile_form.html', {'form': form})

'''

class ProjectDetail(DetailView):
    model = UserProject
    context_object_name = 'project'

    def get_queryset(self):
        query = UserProject.objects.all()

        return query

    def get_context_data(self, **kwargs):
        form = ApplicantForm()
        context = super().get_context_data(**kwargs)
        context['form'] = form
        context['positions'] = Position.objects.filter(
            project_id=self.object.id)

        return context


class CreateApplicant(View):
    model = UserProject

    def post(self, request, *args, **kwargs):
        position_id = request.POST.get('position')
        position = Position.objects.get(id=int(position_id))
        Applicant(applicant=self.request.user,
                  hired=False, position=position).save()
        messages.success(request, 'Your application has been saved')
        return redirect('projects:detail', pk=position.id)


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
        applicant = Applicant.objects.get(id=kwargs['pk'])
        applicant.hired = True
        applicant.save()
        messages.success(request, 'Your application has been saved')
        return redirect('projects:applicants')


class ApplicantReject(SingleObjectMixin, SingleObjectTemplateResponseMixin,
                      View):

    def get(self, request, *args, **kwargs):
        applicant = Applicant.objects.get(id=kwargs['pk'])
        applicant.hired = False
        applicant.save()
        messages.success(request, 'Your application has been saved')
        return redirect('projects:applicants')

