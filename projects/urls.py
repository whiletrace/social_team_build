from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [

    path('create_project/', views.CreateProject.as_view(
        template_name='projects/project_form.html')),

    path('detail/<int:pk>/', views.ProjectDetail.as_view(), name='detail'),

    path('create_applicant/<int:position>/', views.CreateApplicant.as_view(),
         name='apply')


    ]
