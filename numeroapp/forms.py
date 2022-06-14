from django import forms
from .models import numero_Project, numero_Profile

class numero_ProjectForm(forms.ModelForm):
    class Meta:
        model = numero_Project
        fields = ('title', 'description', 'image', 'url')

class numero_ProfileForm(forms.ModelForm):
    class Meta:
        model = numero_Profile
        fields = ('bio', 'profile_picture', 'phone_number', 'email', 'github_profile', 'twitter_profile')