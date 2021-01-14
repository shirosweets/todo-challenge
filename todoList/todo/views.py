from django.shortcuts import render, redirect

from .models import Task
from rest_framework import viewsets          
from .serializers import TaskSerializer      
from rest_framework.response import Response
from rest_framework.decorators import api_view

import requests
import logging
import datetime


logger = logging.getLogger('myLogger')

@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'List': '/task-list/',
    'Detail': '/task-detail/',
    'Create': '/task-create',
    'Update': '/task-update/<str:pk>',
    'Delete': '/task-delete/<str:pk>',
  }
  return  Response(api_urls)


#Obtenemos todas las tareas
@api_view(['GET'])
def task_list(request):
  tasks = Task.objects.all()
  tasks=tasks.order_by('-pub_date')
  serializer = TaskSerializer(tasks, many=True)
  return Response(serializer.data)

#Obtenemos una tarea

@api_view(['GET'])
def get_a_task(request):
  txt = request.GET['content_text']
  if(txt!=''):
    task = Task.objects.filter(content_text__icontains=txt)
    if (task):
      serializer = TaskSerializer(task, many=False)
      context = {
        'tasks': task
      }
      return render(request, 'todo/index.html',context)
    
    else:
      #A pesar de que este else es innecesario, la app no funciona sino
      return redirect('http://localhost:8000/todo/')

  else:

    return redirect('http://localhost:8000/todo/')


  '''
  Para implementacion de API
  try:
    return Response(serializer.data)
  except:
    Response("Error")
  '''



#Creamos una tarea

@api_view(['POST'])
def create_task(request):
  serializer = TaskSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()
    
  #Para una implementacion de API cambiar a return Response(serializer.data)
  return redirect('/todo')


#Actualizamos una tarea

@api_view(['POST', 'GET'])
def update_task(request, pk):
  task = Task.objects.get(id=pk)
  
  serializer = TaskSerializer(instance = task, data=request.data)
  serializer.is_valid()
  logger.error('Putoooooooooooooooo')
  logger.error(request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


#Completamos o descompletamos una tarea de manera mas rapida

@api_view(['POST', 'GET'])
def complete_task(request, pk):
  task = Task.objects.get(id=pk)
  new_data = request.data
  if(task.completed == False):
    new_data["completed"] = True
  else:
    new_data["completed"] = False
  serializer = TaskSerializer(instance = task, data=new_data, partial = True)
  logger.error(serializer.is_valid())
  logger.error(serializer.errors)
  
  if serializer.is_valid():
    serializer.save()
  return redirect('/todo')
  #Para API
  #return Response(serializer.data)

#Borramos una tarea

@api_view(['GET','DELETE'])
def delete_task(request, pk):
  #try:
  task = Task.objects.get(id=pk)
  task.delete()
    #Para una implementacion de API descomentar el retorno de response
  return redirect('/todo')  
    #return Response("Se borro la tarea correctamente", status=200)
  #except:
    
    #return Response("La tarea no existe", status=400)
  
  


#FrontEnd
def index(request):
    tasks = requests.get('http://localhost:8000/api/task-list')
    tasks = tasks.json()
  
    #Parseo de la fecha debido a que serializer la almacena como str para manipulacion en JSON
    for task in tasks:
      task['pub_date'] = datetime.datetime.strptime(task['pub_date'], "%Y-%m-%dT%H:%M:%S.%f%z").ctime()
    context = {
    'tasks' : tasks,
    
  }
    return render(request, 'todo/index.html', context)

