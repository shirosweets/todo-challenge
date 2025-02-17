from django.db import models
from django.utils import timezone
import datetime


class Task(models.Model):
    pub_date = models.DateTimeField("Fecha de publicacion", auto_now_add=True)
    content_text = models.CharField(max_length=200)
    completed = models.BooleanField(default = False)

    #para no devolver el objeto como tal devolvemos el texto
    def __str__(self):
        return self.content_text

    
    