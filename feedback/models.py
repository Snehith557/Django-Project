from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
# we need to create some classes that denotes the tables in the database
# models.py
class feedBacks(models.Model):
    name = models.CharField(null=False,max_length=200)
    email = models.CharField(null=False,max_length=100)
    description = models.CharField(null=True,blank=True,max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ['-updated','created']


    def __str__(self):
        return self.name
    
