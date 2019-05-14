from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dash', views.dash, name='dash'),
    path('jobs', views.jobs, name='jobs'),
    path('candidates', views.candidates, name='candidates'),
    path('feedbacks', views.feedbacks, name='feedbacks'),
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('accounts/', include('django.contrib.auth.urls'))
]
