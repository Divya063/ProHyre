from django.urls import path, include

from . import views

urlpatterns = [
    path('log', views.home, name='home'),
    path('dash', views.dash, name='dash'),
    path('jobs', views.jobs, name='jobs'),
    path('job_desc', views.job_desc, name='job_desc'),
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
