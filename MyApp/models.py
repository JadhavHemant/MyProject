from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name =models.CharField(max_length=100)
    employee_code=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    salary=models.FloatField()

class City(models.Model):
<<<<<<< HEAD
    city_name=models.CharField(max_length=100) 

class State(models.Model):
    state_name=models.CharField(max_length=100)       
=======
    city_name=models.CharField(max_length=100)  
    
class Student(models.Model):
    student_name=models.CharField(max_length=100)

<<<<<<< HEAD
      
>>>>>>> 0cc9f2a88b241467874cefa63a3a2d74636b0153
=======
    
>>>>>>> 4804960173692685c3974b22b411fd35769a5ee1
