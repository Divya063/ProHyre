from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class User(AbstractUser):
	is_staff=True
	is_superuser=True
	is_candidate = models.BooleanField(default=False)
	is_hr = models.BooleanField(default=False)

class Hr(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=30, default='user')
    company = models.CharField(max_length=30)

class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=30, default='user')
    company = models.CharField(max_length=30)

class Job(models.Model):
    job_id = models.UUIDField(default=uuid.uuid4, editable=False)
    job_role = models.CharField(max_length=30)
    job_desc = models.TextField()
    location = models.TextField()
    username = models.CharField(max_length=10)
    posted_on = models.DateTimeField()
    total_applications = models.IntegerField(default=0)
    active_applications = models.IntegerField(default=0)
    offers_made = models.IntegerField(default=0)
    pending_feedbacks = models.IntegerField(default=0)
