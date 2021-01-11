from django.shortcuts import render

from .models import Task
from rest_framework import viewsets          
from .serializers import TaskSerializer      
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'List': '/task-list/',
    'Detail': '/task-detail/<int:pk>/',
    'Create': '/task-create',
    'Update': '/task-update/<int:pk>',
    'Delete': '/task-delete/<int:pk>',
  }
  return  Response(api_urls)


#Viewsets nos facilita las tareas de CRUD
'''class TaskView(viewsets.ModelViewSet):       
  serializer_class = TaskSerializer          
  queryset = Task.objects.all()              
'''

#Obtenemos todas las tareas
@api_view(['GET'])
def task_list(request):
  tasks = Task.objects.all()
  serializer = TaskSerializer(tasks, many=True)
  return Response(serializer.data)

#Obtenemos una tarea

@api_view(['GET'])
def get_a_task(request, pk):
  task = Task.objects.get(id=pk)
  serializer = TaskSerializer(task, many=False)
  try:
    return Response(serializer.data)
  except:
    Response("Error")


#Creamos una tarea

@api_view(['POST'])
def create_task(request):
  serializer = TaskSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

#Actualizamos una tarea

@api_view(['POST'])
def update_task(request, pk):
  task = Task.objects.get(id=pk)
  serializer = TaskSerializer(instance = task, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

#Borramos una tarea

@api_view(['DELETE'])
def delete_task(request, pk):
  try:
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Se borro la tarea correctamente", status=200)
  except:
    return Response("La tarea no existe", status=400)
  
  


#Front
def index(request):
    tasks = TaskView.queryset
    context = {
    'tasks' : tasks
  }
    return render(request, 'todo/index.html', context)

