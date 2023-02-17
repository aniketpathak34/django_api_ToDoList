from django.db import models

# Create your models here.
#this ToDo class will create all fields, that will creart tables for your data
class ToDo(models.Model):
    
    Title = models.CharField(max_length=100,blank=False)
    
    Description = models.TextField(blank=True)
    
    Date = models.DateField(blank=False)
    
    Completed = models.BooleanField(default=False)


    def __str__(self):
        return self.Title
         
