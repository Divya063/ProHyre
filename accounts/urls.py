from django.urls import path

from . import views


urlpatterns = [
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
]