from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'app/home.html')

def dash(request):
    return render(request, 'app/dash.html')
