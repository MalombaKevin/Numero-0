from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class numero_Project(models.Model):  
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=10000)
    image_project=models.ImageField(upload_to='images/')
    url=models.URLField(max_length=200)
    project_files =models.URLField(max_length=200, blank=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   

    def __str__(self):
        return self.title
    
    def save_numero_Project(self):
        self.save()
    
    def update_numero_project(self):
        self.update()
    
    def delete_numero_Profile(self):
        self.delete()
   
    @classmethod
    def search_item(cls, search_term):
        results = cls.objects.filter(title__icontains=search_term)
        return results
    
     
    
    


class numero_Profile(models.Model):
    profile_name = models.CharField(max_length=200, null=True)
    bio= models.TextField(max_length=1000)
    profile_picture=models.ImageField(upload_to='images/')
    phone_number=models.CharField(max_length=10, blank=True)
    email=models.EmailField(max_length=200, blank=True)
    github_profile =models.URLField(max_length=200, blank=True)
    twitter_profile=models.URLField(max_length=200, blank=True)
    linked_profile=models.URLField(max_length=200, blank=True)   
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.bio
    
    def save_numero_Profile(self):
        self.save()



    
