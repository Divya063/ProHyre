from django import forms

from .models import UserProfile, Skill, SchoolProject, Objective, Address, Company, Education, Experience

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields=('street', 'state', 'city', 'country', 'post')


class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields=('name')

class EducationForm(forms.ModelForm):
	class Meta:
		model = Education
		fields= ('school', 'start_date', 'end_date', 'relevant_courses', 'major', 'minor', 'type', 'present')

class ExperienceForm(forms.ModelForm):
	class Meta:
		model = Experience
		fields = ('start_date', 'end_date', 'present', 'job_duty', 'company', 'role')

class SkillForm(forms.ModelForm):
	class Meta:
		model = Skill
		fields = ('name', 'description')

class SchoolProjectForm(forms.ModelForm):
	class Meta:
		model = SchoolProject
		fields = ('name', 'description', 'date')
class ObjectiveForm(forms.ModelForm):
	class Meta:
		model = Objective
		fields= ('objective')

class PostForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'phone', 'profession', 'address', 'skill', 'experiences', 'objective', 'education', 'projects', 'linkedin', 'github',)

