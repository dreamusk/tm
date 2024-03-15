# models.py
#this is the model.py is used for creating database using sql 
#urls are used 
#that views are like 

from django.db import models

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Employee(models.Model):
    empid = models.CharField(max_length=255, primary_key=True)
    employee = models.CharField(max_length=255)

class Work(models.Model):
    id = models.AutoField(primary_key=True)
   # team = models.ForeignKey(Team, on_delete=models.CASCADE)
    empid = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Project(models.Model):
    pid = models.CharField(max_length=255, primary_key=True)
    pname = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=255)

class Manage(models.Model):
    pid = models.ForeignKey(Work, on_delete=models.CASCADE)
    empid = models.ForeignKey(Project, on_delete=models.CASCADE)
