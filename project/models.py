from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    name= models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    link=models.CharField(max_length=50)
    Image= models.CharField(max_length=20)

