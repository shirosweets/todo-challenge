
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views


#Con esto logramos --> /api/tasks/ traer todas las tareas
#Con api/tasks/id traemos una especifica
router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'task')


urlpatterns = [
    path('todo/', include('todo.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
