from django.db import models 

class Entity1(models.Model): 
    Col001 = models.CharField(max_length=50) 
    Col002 = models.CharField(max_length=50) 
    Col003 = models.CharField(max_length=50) 
    Col004 = models.CharField(max_length=50) 
    Col005 = models.CharField(max_length=50) 

    class Meta: 
        db_table = "entity1" 

