from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

@login_required
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def exit(request):
    logout(request)
    return redirect('inicio')