from django.db import models 
#from django.contrib.postgres.fields import ArrayField

class Links:
    '''
    Information models for API recipes output
    '''
    img: str
    url: str
    name: str
    instructions: str
    count: int
   
class FoodItem(models.Model):
    '''
    Models for Food information input from the users
    '''
    name = models.CharField(max_length=32)
    quantity = models.CharField(max_length=64)
    user_name = models.CharField(max_length=32)

class Food:
    '''
    Information for Food items for the users
    '''
    name: str
    quantity: str
