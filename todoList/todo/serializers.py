from rest_framework import serializers
from .models import Task

#Especificar la conversion del modelo a JSON y facilitar el trabajo al front
class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'