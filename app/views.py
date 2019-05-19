from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from .forms import HrSignUpForm, CandidateSignUpForm
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render


def index(request):
    return render(request, 'app/home.html')

def dash(request):
    return render(request, 'app/dash.html', { 'active': 'dash'})

def candidate_dash(request):
    return render(request, 'candidates/dash.html', {'active': 'dash'})

def jobs(request):
    return render(request, 'app/jobs.html', { 'active': 'jobs'})

def job_desc(request):
    return render(request, 'app/job_desc.html', { 'active': 'jobs'})

def candidates(request):
    return render(request, 'app/candidates.html', { 'active': 'candidates'})

def candidates_analysis(request):
    return render(request, 'app/candidates_analysis.html', { 'active': 'candidates'})

def candidate(request):
    return render(request, 'app/candidate.html', { 'active': 'candidate'})

def profile(request):
    return render(request, 'app/profile.html', { 'active': 'profile'})

def settings(request):
    return render(request, 'app/settings.html', { 'active': 'settings'})

class SignUpView(TemplateView):
    template_name = 'signup_form.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_hr:
            return redirect('dash')
        else:
            return redirect('candidate_dash')
    return render(request, 'login')

class HrSignUpView(CreateView):
    model = User
    form_class = HrSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'hr'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('dash')

class CandidateSignUpView(CreateView):
    model = User
    form_class = CandidateSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'candidate'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        user.is_staff=True
        login(self.request, user)
        return redirect('candidate_dash')
