from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'app/home.html')

def dash(request):
    return render(request, 'app/dash.html', { 'active': 'dash'})

def jobs(request):
    return render(request, 'app/jobs.html', { 'active': 'jobs'})

def candidates(request):
    return render(request, 'app/candidates.html', { 'active': 'candidates'})

def feedbacks(request):
    return render(request, 'app/feedbacks.html', { 'active': 'feedbacks'})

def profile(request):
    return render(request, 'app/profile.html', { 'active': 'profile'})

def settings(request):
    return render(request, 'app/settings.html', { 'active': 'settings'})
