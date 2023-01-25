from pyclbr import Class
from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=255)
    alter_ego  = models.CharField(max_length=255) 
    primary_ability = models.CharField(max_length=255) 
    scondary_ability = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey()
    
