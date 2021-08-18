from django.db import models

# Create your models here.
class Post(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=40)