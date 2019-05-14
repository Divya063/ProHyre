from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dash', views.dash, name='dash'),
    path('jobs', views.jobs, name='jobs'),
    path('accounts/', include('django.contrib.auth.urls'))
]
