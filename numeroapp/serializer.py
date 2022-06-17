from rest_framework import serializers
from .models import numero_Profile, numero_Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = numero_Profile
        fields = ('profile_name', 'bio', 'profile_picture', 'phone_number', 'email', 'github_profile', 'twitter_profile', 'linked_profile')
        

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = numero_Project
        fields = ('title', 'description', 'image_project', 'url', 'project_files')
        
