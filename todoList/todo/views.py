from django.shortcuts import render

from .models import Task

#Traemos las tareas para mostrarlas

def index(request):
    return render(request, 'todo/index.html')
