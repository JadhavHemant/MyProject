from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name =models.CharField(max_length=100)
    employee_code=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    salary=models.FloatField()
    class Meta:
        db_table="employeestbl" 
        
class StudentUserId(models.Model):
    Student_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    class Meta:
        db_table="tbl_user_student"      