from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name =models.CharField(max_length=100)
    employee_code=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    salary=models.FloatField()

class City(models.Model):
    city_name=models.CharField(max_length=100) 

class State(models.Model):
    state_name=models.CharField(max_length=100)       

class CityModel(models.Model):
    city_name=models.CharField(max_length=100)  
    
class Student(models.Model):
    student_name=models.CharField(max_length=100)

class Github(models.Model):
    Git_Hub=models.CharField(max_length=100)
    