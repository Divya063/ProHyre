from django.urls import path, include

from . import views

urlpatterns = [
    path('log', views.home, name='home'),
    path('dash', views.dash, name='dash'),
    path('candidate_dash', views.candidate_dash, name='candidate_dash'),
    path('jobs', views.jobs, name='jobs'),
    path('search_jobs', views.search_jobs, name='search_jobs'),
    path('job_desc', views.job_desc, name='job_desc'),
    path('apply_job', views.apply_job, name='apply_job'),
    path('application_status', views.application_status, name='application_status'),
    path('candidates', views.candidates, name='candidates'),
    path('candidates/candidate', views.candidate, name='candidate'),
    path('candidates/analysis', views.candidates_analysis, name='candidates'),
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', views.CandidateSignUpView.as_view(), name='candidates_signup'),
    path('accounts/signup/hr/', views.HrSignUpView.as_view(), name='hr_signup'),
]
