from django.db import models

# Create your models here
class Ingredient(models.Model):
    name = models.CharField(max_length = 32)
    quantity = models.CharField(max_length = 64)
    user_name = models.CharField(max_length = 32)
    def __str__(self):
        return self.name

class User_Recipe(models.Model):
    author = models.CharField(max_length = 16, default='admin')
    title = models.CharField(max_length = 32)
    ingredients = models.CharField(max_length = 512)
    description = models.CharField(max_length = 512)
    steps = models.CharField(max_length=4096)
    approved = models.BooleanField(default=False)
    def __str__(self):
        return self.title

