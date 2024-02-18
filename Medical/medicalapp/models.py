from django.db import models

# Create your models here.

class Task(models.Model):
    task=models.TextField()
    priority=models.IntegerField()
    date = models.DateField()
    created=models.DateTimeField(auto_now_add=True)

class Credential(models.Model):
    username=models.CharField(max_length=250,unique=True)
    password=models.CharField(max_length=250)

    