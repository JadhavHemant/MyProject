from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name =models.CharField(max_length=100)