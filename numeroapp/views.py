from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from numeroapp.forms import numero_ProfileForm, numero_ProjectForm
from .models import numero_Project, numero_Profile
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from numeroapp.serializer import ProfileSerializer, ProjectSerializer




# Create your views here.

@login_required(login_url='/accounts/login/')  
def index(request):
    numero_projects = numero_Project.objects.all()
    user = User.objects.get(username=request.user.username)

    return render(request, 'index.html', {'projects': numero_projects, 'user': user})


@login_required(login_url='/accounts/login/')  
def profile(request):
    if numero_Profile.objects.filter(user_id=request.user.id).exists():
        profile = numero_Profile.objects.get(user_id=request.user.id)
        projects = numero_Project.objects.filter(user_id = request.user.id).all()
    else:
        profile = None
        projects = None

    
    return render(request, 'profile.html', {'profile': profile,'projects': projects})




@login_required(login_url='/accounts/login/')
def add_project(request):
    if request.method == 'POST':
        form = numero_ProjectForm(request.POST, request.FILES)
        if form.is_valid():
           project= form.save(commit=False)
           project.user = request.user
           project.save()
           return redirect('index')
    else:
        form = numero_ProjectForm()

    return render(request, 'forms/new_project.html', {'form': form})

@login_required(login_url='/accounts/login/')   
def add_profile(request):
    if request.method == 'POST':
        form = numero_ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = numero_ProfileForm()

    return render(request, 'forms/update_profile.html', {'form': form})

@login_required(login_url='/accounts/login/')
def project_details(request,id):
    projects = numero_Project.objects.get(id=id)
    return render(request, 'project_details.html', {'projects': projects})

@login_required(login_url='/accounts/login/')
def numerologers(request):
    profiles = numero_Profile.objects.all()

    return render(request, 'users.html', {'profiles': profiles})

@login_required(login_url='/accounts/login/')
def numerologer(request, id):
    if numero_Profile.objects.filter(user_id=id).exists():
        profile = numero_Profile.objects.get(user_id=id)
        projects = numero_Project.objects.filter(user_id = id).all()
    else:
        profile = None
        projects = None

    return render(request, 'user_details.html', {'profile': profile,'projects': projects})
@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        searched_titles = numero_Project.search_item(search_term)

        return render(request, 'search.html', {"titles":searched_titles})
    else:
        
        return render(request, 'search.html')

class ProjectView(APIView):
     #APIView as a base class for our API view function.
    def get(self, request, format=None):
        #define a get method where we query the database to get all the MoringaMerchobjects
        projectsZote = numero_Project.objects.all()
        #serialize the Django model objects and return the serialized data as a response.
        serializers = ProjectSerializer(projectsZote, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        # post method will be triggered when we are getting form data
        serializers = ProjectSerializer(data=request.data)
        # serialize the data in the request
        if serializers.is_valid():
            # If valid we save the new data to the database and return the appropriate status code.
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
     #APIView as a base class for our API view function.
    def get(self, request, format=None):
        #define a get method where we query the database to get all the MoringaMerchobjects
        projectsZote = numero_Profile.objects.all()
        #serialize the Django model objects and return the serialized data as a response.
        serializers = ProfileSerializer(projectsZote, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        # post method will be triggered when we are getting form data
        serializers = ProfileSerializer(data=request.data)
        # serialize the data in the request
        if serializers.is_valid():
            # If valid we save the new data to the database and return the appropriate status code.
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
