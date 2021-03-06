# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-14 05:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=70, verbose_name='Street Name')),
                ('state', models.CharField(max_length=10, verbose_name='State')),
                ('city', models.CharField(max_length=20, verbose_name='City')),
                ('country', models.CharField(max_length=20, verbose_name='Country')),
                ('postal', models.CharField(max_length=10, verbose_name='Postal Code')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Company Name')),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Started')),
                ('end_date', models.DateField(verbose_name='Ended')),
                ('relevant_courses', models.TextField(blank=True, verbose_name='Relevant Course Work')),
                ('major', models.TextField(blank=True, verbose_name='Major')),
                ('minor', models.TextField(blank=True, verbose_name='Minor')),
                ('type', models.CharField(max_length=30, verbose_name='Type')),
                ('present', models.BooleanField(verbose_name='Present')),
            ],
            options={
                'ordering': ('-start_date',),
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Started')),
                ('end_date', models.DateField(verbose_name='Ended')),
                ('present', models.BooleanField(verbose_name='Present')),
                ('job_duty', models.TextField(verbose_name='Job Duty')),
                ('role', models.CharField(max_length=50, verbose_name='Role')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Company')),
            ],
            options={
                'ordering': ('start_date',),
            },
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='School Name')),
                ('city', models.CharField(max_length=40, verbose_name='City')),
                ('country', models.CharField(max_length=40, verbose_name='Country')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Project Name')),
                ('description', models.TextField(verbose_name='Project Description')),
                ('date', models.DateField(verbose_name='Date Completed')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Skill Name')),
                ('description', models.TextField(verbose_name='Skill Description')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('profession', models.CharField(max_length=40, verbose_name='Profession')),
                ('linkedin', models.CharField(max_length=80, verbose_name='LinkedIn')),
                ('github', models.CharField(max_length=40, verbose_name='GitHub')),
                ('address', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='resume.Address')),
                ('education', models.ManyToManyField(to='resume.Education')),
                ('experiences', models.ManyToManyField(to='resume.Experience')),
                ('objective', models.ManyToManyField(to='resume.Objective')),
                ('projects', models.ManyToManyField(to='resume.SchoolProject')),
                ('skill', models.ManyToManyField(to='resume.Skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='education',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.School'),
        ),
    ]
