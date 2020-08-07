from django.db import models

# Create your models here
class Ingredient(models.Model):
    name = models.CharField(max_length = 32)
    quantity = models.CharField(max_length = 64)
    user_name = models.CharField(max_length = 32)
    def __str__(self):
        return self.name

