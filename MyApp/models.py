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

<<<<<<< HEAD
class Github(models.Model):
    Git_Hub=models.CharField(max_length=100)
    
=======
<<<<<<< HEAD
<<<<<<< HEAD
      
>>>>>>> 0cc9f2a88b241467874cefa63a3a2d74636b0153
=======
    
>>>>>>> 4804960173692685c3974b22b411fd35769a5ee1
=======
>>>>>>> 91115c574e6a30845a959988832606a3fbe85c1d
>>>>>>> 89ca399099c3897f3d63d8e94f6dac0697fa5c38
