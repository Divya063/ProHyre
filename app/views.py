from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from .forms import HrSignUpForm, CandidateSignUpForm
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response


def index(request):
    return render(request, 'app/home.html')

@login_required
def dash(request):
    return render(request, 'app/dash.html', { 'active': 'dash'})

@login_required
def candidate_dash(request):
    return render(request, 'candidates/dash.html', {'active': 'dash'})

@login_required
def jobs(request):
    return render(request, 'app/jobs.html', { 'active': 'jobs'})

@login_required
def job_desc(request):
    return render(request, 'app/job_desc.html', { 'active': 'jobs'})

@login_required
def candidates(request):
    return render(request, 'app/candidates.html', { 'active': 'candidates'})

@login_required
def candidates_analysis(request):
    return render(request, 'app/candidates_analysis.html', { 'active': 'candidates'})

@login_required
def candidate(request):
    return render(request, 'app/candidate.html', { 'active': 'candidate'})

@login_required
def profile(request):
    return render(request, 'app/profile.html', { 'active': 'profile'})

@login_required
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


def error_404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

def error_500(request, template_name="500.html"):
    response = render_to_response("500.html")
    response.status_code = 500
    return response


