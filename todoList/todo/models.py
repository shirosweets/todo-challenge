from django.db import models

# Create your models here.

class Task(models.Model):
    pub_date = models.DateTimeField('fecha de publicacion')
    content_text = models.CharField(max_length=200)
    completed = models.BooleanField(completed = False)

    