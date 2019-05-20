from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .models import UserProfile
from django.views.decorators.cache import cache_page
#from .forms import PostForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

import sys

class Resume(TemplateView):
	template_name = 'resume.html'

	def get_context_data(self, **kwargs):
		context = {}
		context['profile'] = get_object_or_404(UserProfile)
		return context
