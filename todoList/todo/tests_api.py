from rest_framework.test import APIClient
from rest_framework.test import RequestsClient
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task


'''# Probamos el metodo post
client = APIClient()
client.post('http:/api/task-create/', {'content_text': 'Nueva nota'}, content_type='application/json')

#Probamos el metodo get
client = RequestsClient()
response = client.get('/api/task-list/')
assert response.status_code == 200
'''
class TaskTests(APITestCase):
    #Intentamos crear una tarea
    def test_create_task(self):  
        url = reverse('task-create')
        client = APIClient()
        data = {"content_text": "Nueva nota"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(Task.objects.all().count(), 1)

    #Obtenemos las tareas
    def test_get_task(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
