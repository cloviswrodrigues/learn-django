from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.

def projects(request):
    projects = Project.objects.all()
    print(projects)
    context = { 'projects': projects }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project = Project.objects.get(id = pk)
    context = { 'project': project }
    return render(request, 'projects/single-project.html', context)   