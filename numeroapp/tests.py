from django.test import TestCase

from numeroapp.models import numero_Profile, numero_Project

# Create your tests here.
def numero_Project_test():
    def setup(self):
        self.new_numero_project = numero_Project(name='Test Project', description='Test Description', image='Test Image')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_numero_project, numero_Project))
    
    def test_save_numero_project(self):
        self.new_numero_project.save_numero_project()
        numero_projects = numero_Project.objects.all()
        self.assertTrue(len(numero_projects) > 0)

def numero_Profile_test():
    def setup(self):
        self.new_numero_profile = numero_Profile(name='Test Profile', description='Test Description', image='Test Image')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_numero_profile, numero_Profile))
    
    def test_save_numero_profile(self):
        self.new_numero_profile.save_numero_profile()
        numero_profiles = numero_Profile.objects.all()
        self.assertTrue(len(numero_profiles) > 0)
