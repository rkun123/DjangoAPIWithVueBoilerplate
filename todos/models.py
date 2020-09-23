from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

# class User(models.Model):
    # name = models.CharField(max_length=255, null=False, blank=False)