from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [

    path('create_project/', views.CreateProject.as_view(
        template_name='projects/project_form.html'), name='create_project'),

    path('detail/<int:pk>/', views.ProjectDetail.as_view(), name='detail'),

    path('create_applicant/<int:position>/', views.CreateApplicant.as_view(),
         name='apply'),

    path('applicant_list/', views.ApplicantList.as_view(
        template_name='projects/applications.html'), name='applicants'),

    path('applicant_new/', views.ApplicantList.as_view(
        template_name='projects/new_applications.html'
        ), name='latest_applicants'),
    path('applicant_accepted/', views.ApplicantList.as_view(
        template_name='projects/applications_accepted.html'
        ), name='accepted_applicants'),
    path('applicant_rejected/', views.ApplicantList.as_view(
        template_name='projects/applications_rejected.html'
        ), name='rejected_applicants'),
    path('approve_applicant/<int:pk>/', views.ApplicantApprove.as_view()
         , name='approve'),

    path('reject_applicant/<int:pk>/', views.ApplicantReject.as_view()
         , name='reject'),

    ]
