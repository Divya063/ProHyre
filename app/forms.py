from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from .models import User


class HrSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    company=forms.CharField(max_length=40)
    class Meta(UserCreationForm.Meta):
        model = User
        fields=("username", "email", "company", "password1", "password2")

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.company=self.cleaned_data["company"]
        user.is_hr = True
        if commit:
            user.save()
        return user


class CandidateSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        return user

class CreateJobForm(forms.Form):
    job_role = forms.CharField(label='Job Role', max_length=30)
    job_desc = forms.CharField(widget=forms.Textarea, label='Job Description', max_length=2000)
    location = forms.CharField(label='Job Location', max_length=100)
