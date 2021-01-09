from rest_framework import serializers
from .models import Task

#Especificar la convesion del modelo a JSON y facilitar el trabajo al front
class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = ('id', 'pub_date', 'content_text', 'completed')