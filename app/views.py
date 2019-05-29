from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from .models import Job
from .forms import HrSignUpForm, CandidateSignUpForm, CreateJobForm
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
import datetime

def index(request):
    return render(request, 'app/home.html')

@login_required
def dash(request):
    res = {
        'candidates': [
            {
                'fullName': 'Sudhanshu Gautam',
                'address': 'Delhi, India',
                'jobRole': 'Sofware Engineer I',
                'status': 'Feedback Pending'
            },
            {
                'fullName': 'Sejal Kataria',
                'address': 'Delhi, India',
                'jobRole': 'User Experience Engineer',
                'status': 'Upcoming Interview II'
            },
            {
                'fullName': 'Aman Bhardwaj',
                'address': 'Mumbai, India',
                'jobRole': 'UI/UX Designer',
                'status': 'Feedback Pending'
            }
        ],
        'jobs': [
            {
                'jobRole': 'Software Engineer I',
                'location': 'Bangalore, India',
                'posted_at': '5 days ago'
            },
            {
                'jobRole': 'Senior Sofware Engineer',
                'location': 'Bangalore, India',
                'posted_at': '13 days ago'
            },
            {
                'jobRole': 'Business Intern',
                'location': 'Bangalore, India',
                'posted_at': '1 month ago'
            }
        ]
    }
    return render(request, 'app/dash.html', { 'active': 'dash', 'res': res })

@login_required
def candidate_dash(request):
    res = {
        'activeApplications': [
            {
                'jobRole': 'Software Engineer I',
                'location': 'Bangalore, India',
                'posted_at': '5 days ago',
                'status': 'Pending Feedback'
            },
            {
                'jobRole': 'User Experience Engineer',
                'location': 'Bangalore, India',
                'posted_at': '13 days ago',
                'status': 'Upcoming Interview'
            },
            {
                'jobRole': 'Business Intern',
                'location': 'Bangalore, India',
                'posted_at': '1 month ago',
                'status': 'Upcoming Screening Test'
            }
        ],
        'pastApplications': [
            {
                'jobRole': 'Software Engineer I',
                'location': 'Bangalore, India',
                'posted_at': '5 days ago'
            },
            {
                'jobRole': 'User Experience Engineer',
                'location': 'Bangalore, India',
                'posted_at': '13 days ago'
            },
            {
                'jobRole': 'Business Intern',
                'location': 'Bangalore, India',
                'posted_at': '1 month ago'
            }
        ],
    }
    return render(request, 'candidates/dash.html', {'active': 'dash', 'res': res })

@login_required
def jobs(request):
    all_jobs = Job.objects.all().values('job_role', 'job_desc', 'posted_on', 'location')
    print(all_jobs)
    res = {
        'activeJobs': all_jobs,
        'archivedJobs': [
            {
                'jobRole': 'Senior Software Engineer',
                'location': 'Bangalore, India',
                'posted_at': '5 months ago'
            },
            {
                'jobRole': 'Senior Sofware Engineer',
                'location': 'Bangalore, India',
                'posted_at': '10 months ago'
            },
        ]
    }
    return render(request, 'app/jobs.html', { 'active': 'jobs', 'res': res })

@login_required
def search_jobs(request):
    res = {
        'activeJobs': [
            {
                'jobRole': 'Software Engineer I',
                'location': 'Bangalore, India',
                'posted_at': '5 days ago'
            },
            {
                'jobRole': 'User Experience Engineer',
                'location': 'Tokyo, Japan',
                'posted_at': '13 days ago'
            },
            {
                'jobRole': 'Business Intern',
                'location': 'Bangalore, India',
                'posted_at': '1 month ago'
            },
            {
                'jobRole': 'Engineering Apprentice',
                'location': 'Bangalore, India',
                'posted_at': '1 month ago'
            },
            {
                'jobRole': 'Sales Intern',
                'location': 'Beijing, China',
                'posted_at': '2 months ago'
            },
            {
                'jobRole': 'Engineering Apprentice',
                'location': 'Bangalore, India',
                'posted_at': '1 month ago'
            },
            {
                'jobRole': 'Sales Intern',
                'location': 'Bangalore, India',
                'posted_at': '2 months ago'
            }
        ]
    }
    return render(request, 'candidates/search_jobs.html', { 'active': 'jobs', 'res': res })

@login_required
def job_desc(request):
    res = {
        'activeCandidates': [
            {
                'fullName': 'Sudhanshu Gautam',
                'address': 'Delhi, India',
                'jobRole': 'Sofware Engineer I',
                'status': 'Feedback Pending'
            },
            {
                'fullName': 'Sejal Kataria',
                'address': 'Delhi, India',
                'jobRole': 'User Experience Engineer',
                'status': 'Upcoming Interview II'
            },
            {
                'fullName': 'Aman Bhardwaj',
                'address': 'Mumbai, India',
                'jobRole': 'UI/UX Designer',
                'status': 'Feedback Pending'
            }
        ],
        'acceptedCandidates': [
            {
                'fullName': 'Sudhanshu Gautam',
                'address': 'Delhi, India',
                'jobRole': 'Sofware Engineer I',
                'status': 'Feedback Pending'
            },
            {
                'fullName': 'Sejal Kataria',
                'address': 'Delhi, India',
                'jobRole': 'User Experience Engineer',
                'status': 'Upcoming Interview II'
            },
            {
                'fullName': 'Aman Bhardwaj',
                'address': 'Mumbai, India',
                'jobRole': 'UI/UX Designer',
                'status': 'Feedback Pending'
            }
        ],
    }
    return render(request, 'app/job_desc.html', { 'active': 'jobs', 'res': res})

@login_required
def apply_job(request):
    res = {
    }
    return render(request, 'candidates/apply_job.html', { 'active': 'jobs', 'res': res})

@login_required
def candidates(request):
    res = {
        'activeCandidates': [
            {
                'fullName': 'Sudhanshu Gautam',
                'address': 'Delhi, India',
                'jobRole': 'Sofware Engineer I',
                'status': 'Feedback Pending'
            },
            {
                'fullName': 'Sejal Kataria',
                'address': 'Delhi, India',
                'jobRole': 'User Experience Engineer',
                'status': 'Upcoming Interview II'
            },
            {
                'fullName': 'Aman Bhardwaj',
                'address': 'Mumbai, India',
                'jobRole': 'UI/UX Designer',
                'status': 'Feedback Pending'
            }
        ],
        'acceptedCandidates': [
            {
                'fullName': 'Sudhanshu Gautam',
                'address': 'Delhi, India',
                'jobRole': 'Sofware Engineer I',
                'status': 'Feedback Pending'
            },
            {
                'fullName': 'Sejal Kataria',
                'address': 'Delhi, India',
                'jobRole': 'User Experience Engineer',
                'status': 'Upcoming Interview II'
            },
            {
                'fullName': 'Aman Bhardwaj',
                'address': 'Mumbai, India',
                'jobRole': 'UI/UX Designer',
                'status': 'Feedback Pending'
            }
        ],
    }
    return render(request, 'app/candidates.html', { 'active': 'candidates', 'res': res })

@login_required
def candidates_analysis(request):
    res = {
        'activeCandidates': [
            {
                'fullName': 'Sudhanshu Gautam',
                'address': 'Delhi, India',
                'jobRole': 'Sofware Engineer I',
                'status': 'Feedback Pending'
            },
            {
                'fullName': 'Sejal Kataria',
                'address': 'Delhi, India',
                'jobRole': 'User Experience Engineer',
                'status': 'Upcoming Interview II'
            },
            {
                'fullName': 'Aman Bhardwaj',
                'address': 'Mumbai, India',
                'jobRole': 'UI/UX Designer',
                'status': 'Feedback Pending'
            }
        ]
    }
    return render(request, 'app/candidates_analysis.html', { 'active': 'candidates', 'res': res })

@login_required
def candidate(request):
    return render(request, 'app/candidate.html', { 'active': 'candidates'})

@login_required
def application_status(request):
    return render(request, 'candidates/application_status.html', { 'active': 'jobs'})


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

def CreateJobView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            job_role = form.cleaned_data['job_role']
            job_desc = form.cleaned_data['job_desc']
            location = form.cleaned_data['location']
            posted_on = datetime.datetime.now()
            username = request.user.username
            job = Job.objects.create(job_role=job_role,job_desc=job_desc, posted_on=posted_on, username=username, location=location)
            # redirect to a new URL:
            return redirect('jobs')
    else:
        form = CreateJobForm()
    return render(request, 'app/add_job.html', {'form': form})


def error_404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

def error_500(request, template_name="500.html"):
    response = render_to_response("500.html")
    response.status_code = 500
    return response
