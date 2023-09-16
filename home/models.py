from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    create = models.DateTimeField()

# Create your models here.
