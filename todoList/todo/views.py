from django.shortcuts import render

from .models import Task
from rest_framework import viewsets          
from .serializers import TaskSerializer      


#Viewsets nos facilita las tareas de CRUD
class TaskView(viewsets.ModelViewSet):       
  serializer_class = TaskSerializer          
  queryset = Task.objects.all()              


