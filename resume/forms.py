from django import forms

from .models import UserProfile

class PostForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('user', 'phone', 'profession', 'address', 'skill', 'experiences', 'objective', 'education', 'projects', 'linkedin', 'github',)