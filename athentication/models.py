from django.db import models
from pyexpat import model
# Create your models here.

class Role(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.title}'

class Workshop(models.Model) :
    title = models.CharField(max_length=31)
    disciption = models.TextField()
    
    def __str__(self):
        return f'{self.title}'
class User(models.Model):
    personalID = models.CharField(max_length=11)
    password = models.CharField(max_length=16)
    email = models.EmailField(max_length=255)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.personalID}'