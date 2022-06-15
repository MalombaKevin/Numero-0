from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from numeroapp.forms import numero_ProfileForm, numero_ProjectForm
from .models import numero_Project, numero_Profile
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='/accounts/login/')  
def index(request):
    numero_projects = numero_Project.objects.all()

    return render(request, 'index.html', {'projects': numero_projects})


@login_required(login_url='/accounts/login/')  
def profile(request):
    profiles = numero_Profile.objects.all()
    user = User.objects.get(username=request.user.username)
    projects = numero_Project.objects.all()
    

    return render(request, 'profile.html', {'profiles': profiles, 'user': user, 'projects': projects})




@login_required(login_url='/accounts/login/')
def add_project(request):
    if request.method == 'POST':
        form = numero_ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = numero_ProjectForm()

    return render(request, 'forms/new_project.html', {'form': form})

@login_required(login_url='/accounts/login/')   
def add_profile(request):
    if request.method == 'POST':
        form = numero_ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = numero_ProfileForm()

    return render(request, 'forms/update_profile.html', {'form': form})
