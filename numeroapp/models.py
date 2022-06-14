from django.db import models

# Create your models here.
class numero_Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=10000)
    image=models.ImageField(upload_to='images/')
    url=models.URLField(max_length=200)
    profile = models.ForeignKey('numero_Profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def save_numero_Project(self):
        self.save()


class numero_Profile(models.Model):
    bio= models.TextField(max_length=1000)
    profile_picture=models.ImageField(upload_to='images/')
    phone_number=models.CharField(max_length=10, blank=True)
    email=models.EmailField(max_length=200, blank=True)
    github_profile =models.URLField(max_length=200, blank=True)
    twitter_profile=models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.bio
    
    def save_numero_Profile(self):
        self.save()



    
