from django.db import models


class Task(models.Model):
    pub_date = models.DateTimeField('fecha de publicacion')
    content_text = models.CharField(max_length=200)
    completed = models.BooleanField(default = False)

    #para no devolver el objeto como tal devolvemos el texto
    def __str__(self):
        return self.content_text


    