from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=32)
    content = models.TextField()
    title = models.CharField(max_length=200, default='Hola Mundo')

    def __str__(self):
        return self.name
