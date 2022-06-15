from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from numeroapp.forms import numero_ProfileForm, numero_ProjectForm
from .models import numero_Project, numero_Profile

# Create your views here.


def index(request):
    numero_projects = numero_Project.objects.all()

    return render(request, 'index.html', {'projects': numero_projects})


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
            return redirect('index')
    else:
        form = numero_ProfileForm()

    return render(request, 'forms/update_profile.html', {'form': form})

