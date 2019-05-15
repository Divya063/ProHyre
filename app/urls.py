from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dash', views.dash, name='dash'),
    path('jobs', views.jobs, name='jobs'),
    path('job_desc', views.job_desc, name='job_desc'),
    path('candidates', views.candidates, name='candidates'),
    path('candidates/analysis', views.candidates_analysis, name='candidates'),
    path('feedbacks', views.feedbacks, name='feedbacks'),
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('accounts/', include('django.contrib.auth.urls'))
]
