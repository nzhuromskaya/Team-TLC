from new.models import Ingredient, User_Recipe
import pytest
from django.test import TestCase

@pytest.mark.django_db
class TestModels(TestCase):

    def test_ingredient_name(self):
        '''
        Test for ingredient.name model
        '''
        ingredient = Ingredient()
        ingredient.name = 'carrot'
        ingredient.user_name = 'ted'
        self.assertEqual(ingredient.name, 'carrot')

    def test_ingredient_quant(self):
        '''
        Test for ingredient.quantity
        '''
        ingredient = Ingredient()
        ingredient.quantity = '200 grams'
        self.assertEqual(ingredient.quantity, '200 grams')

    def test_ingredient_user_name(self):
        '''
        Test for ingredient.user_name
        '''
        ingredient = Ingredient()
        ingredient.user_name = 'ted'
        self.assertEqual(ingredient.user_name, 'ted')

    def test_ingredient__str__(self):
        '''
        Test for ingredient.str
        '''
        ingredient = Ingredient()
        ingredient.name = 'egg'
        self.assertEqual(str(ingredient), 'egg')

    def test_user_recipe_author(self):
        '''
        Test for user_recipe.author
        '''
        recipe = User_Recipe()
        recipe.author = 'todd'
        self.assertEqual(recipe.author, 'todd')

    def test_user_recipe_title(selfi):
        '''
        Test for user_recipe.title
        '''
        recipe = User_Recipe()
        recipe.title = 'pancakes'
        self.assertEqual(recipe.title, 'pancakes')

    def test_user_recipe_ingredients(self):
        '''
        Test for user_recipe.ingredients
        '''
        recipe = User_Recipe()
        recipe.ingredients = 'egg'
        self.assertEqual(recipe.ingredients, 'egg')

    def test_user_recipe_desc(self):
        '''
        Test for user_recipe.desc
        '''
        recipe = User_Recipe()
        recipe.description = 'fluffy'
        self.assertEqual(recipe.description, 'fluffy')

    def test_user_recipe_steps(self):
        '''
        Test for user_recipe.steps
        '''

        recipe = User_Recipe()
        recipe.steps = 'fry'
        self.assertEqual(recipe.steps, 'fry')

    def test_user_recipe_str(self):
        '''
        Test for user_recipe.str
        '''
        recipe=User_Recipe()
        recipe.title = 'tasty'
        self.assertEqual(str(recipe), 'tasty')
