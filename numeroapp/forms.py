from django import forms
from .models import numero_Project, numero_Profile

class numero_ProjectForm(forms.ModelForm):
    class Meta:
        model = numero_Project
        fields = ('title', 'description', 'image_project', 'url')
        exclude = ['user']

class numero_ProfileForm(forms.ModelForm):
    class Meta:
        model = numero_Profile
        fields = ( 'profile_name', 'bio', 'profile_picture', 'phone_number', 'email', 'github_profile', 'twitter_profile', 'linked_profile')
        exclude = ['user']