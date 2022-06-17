from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from numeroapp.forms import numero_ProfileForm, numero_ProjectForm
from .models import numero_Project, numero_Profile
from django.contrib.auth.models import User


# Create your views here.

@login_required(login_url='/accounts/login/')  
def index(request):
    numero_projects = numero_Project.objects.all()
    user = User.objects.get(username=request.user.username)

    return render(request, 'index.html', {'projects': numero_projects, 'user': user})


@login_required(login_url='/accounts/login/')  
def profile(request):
    current_user = request.user
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
    profiles = numero_Profile.objects.get(id=id)
    projects = numero_Project.objects.all()
    user = User.objects.get(username=request.user.username)
    return render(request, 'user_details.html', {'profiles': profiles,'user':user , 'projects':projects})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        searched_titles = numero_Project.search_item(search_term)

        return render(request, 'search.html', {"titles":searched_titles})
    else:
        
        return render(request, 'search.html')

