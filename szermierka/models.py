from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=256, blank=False)
    surname = models.CharField(max_length=256, blank=False)
    data = models.Dat


