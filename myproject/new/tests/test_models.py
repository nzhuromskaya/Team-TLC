from new.models import Ingredient, User_Recipe
import pytest
from django.test import TestCase

@pytest.mark.django_db
class TestModels(TestCase):

    def test_ingredient_name(self):
        ingredient = Ingredient()
        ingredient.name = 'carrot'
        ingredient.user_name = 'ted'
        self.assertEqual(ingredient.name, 'carrot')

    def test_ingredient_quant(self):
        ingredient = Ingredient()
        ingredient.quantity = '200 grams'
        self.assertEqual(ingredient.quantity, '200 grams')

    def test_ingredient_user_name(self):
        ingredient = Ingredient()
        ingredient.user_name = 'ted'
        self.assertEqual(ingredient.user_name, 'ted')

    def test_ingredient__str__(self):
        ingredient = Ingredient()
        ingredient.name = 'egg'
        self.assertEqual(str(ingredient), 'egg')

    def test_user_recipe_author(self):
        recipe = User_Recipe()
        recipe.author = 'todd'
        self.assertEqual(recipe.author, 'todd')

    def test_user_recipe_title(self):
        recipe = User_Recipe()
        recipe.title = 'pancakes'
        self.assertEqual(recipe.title, 'pancakes')

    def test_user_recipe_ingredients(self):
        recipe = User_Recipe()
        recipe.ingredients = 'egg'
        self.assertEqual(recipe.ingredients, 'egg')

    def test_user_recipe_desc(self):
        recipe = User_Recipe()
        recipe.description = 'fluffy'
        self.assertEqual(recipe.description, 'fluffy')

    def test_user_recipe_steps(self):
        recipe = User_Recipe()
        recipe.steps = 'fry'
        self.assertEqual(recipe.steps, 'fry')

    def test_user_recipe_str(self):
        recipe=User_Recipe()
        recipe.title = 'tasty'
        self.assertEqual(str(recipe), 'tasty')
