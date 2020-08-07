from django.db import models 
#from django.contrib.postgres.fields import ArrayField

class Links:
    img: str
    url: str

class FoodItem(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.CharField(max_length=64)
    user_name = models.CharField(max_length=32)

class Food:
    name: str
    quantity: str
