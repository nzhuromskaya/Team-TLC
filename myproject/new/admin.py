from django.contrib import admin

# Register your models here.

from .models import Ingredient, User_Recipe

admin.site.register(Ingredient)
admin.site.register(User_Recipe)
