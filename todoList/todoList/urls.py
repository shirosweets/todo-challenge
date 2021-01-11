
from django.contrib import admin
from django.urls import path, include
from todo import views




urlpatterns = [
    path('api/task-list/', views.task_list, name = 'task-list'),
    path('todo/', include('todo.urls')),
    path('api/task-detail/<int:pk>/', views.get_a_task, name = 'task-detail'),
    path('api/task-create/', views.create_task, name = 'task-create'),
    path('api/task-update/<int:pk>/', views.update_task, name = 'task-update'),
    path('api/task-delete/<int:pk>/', views.delete_task, name = 'task-delete'),
    path('api/', views.apiOverview, name='api-overview'),
    path('admin/', admin.site.urls),
]
