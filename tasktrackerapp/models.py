from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    department=models.CharField(max_length=15)
    designation=models.CharField(max_length=15)
    
class Project(models.Model):
    proj_name=models.CharField(max_length=20)
    description=models.CharField(max_length=50)
    deadline=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.proj_name



class Tasks(models.Model):
    task_name=models.CharField(max_length=20)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    start_time=models.TimeField()
    end_time=models.TimeField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.task_name

   
        
    

