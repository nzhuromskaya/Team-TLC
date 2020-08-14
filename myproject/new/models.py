from django.db import models

# Create your models here
class Ingredient(models.Model):
    '''
    Models for Ingredients for the users 
    '''
    name = models.CharField(max_length = 32)
    quantity = models.CharField(max_length = 64)
    user_name = models.CharField(max_length = 32)
    def __str__(self):
        return self.name

class User_Recipe(models.Model):
    '''
    Models for User recipes for the users
    '''
    author = models.CharField(max_length = 16, default='admin')
    title = models.CharField(max_length = 32)
    ingredients = models.TextField(max_length = 512)
    description = models.TextField(max_length = 512)
    steps = models.TextField(max_length=4096)
    approved = models.BooleanField(default=False)
    def __str__(self):
        return self.title

