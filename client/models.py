from django.db import models
from django.contrib.auth.models import User

# Create your models here.

   
class Account(models.Model):
    name =  models.CharField(max_length=1024, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    users = models.ManyToManyField(User)
    
    def __str__(self):
        return self.name    

class Site(models.Model):
    name = models.CharField(max_length=1024, unique=True)
    create_date = models.DateTimeField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)    
    
    def __str__(self):
        return self.name
    
    
    
    

    