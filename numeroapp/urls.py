#importations
from django.urls import path
from django import views
from . import views

#urls paths
urlpatterns = [
path('', views.index, name='index'),
path('newProject', views.add_project, name='new_project'),
]