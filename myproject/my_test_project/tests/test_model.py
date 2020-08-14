from my_test_project.models import Links, FoodItem, Food
from django.test import TestCase

class test_Models(TestCase):
    '''
    Testing whether an image is saved
    '''
    def test_Link_img(self):
        link = Links()
        link.img = 'Picture here'
        self.assertEqual(link.img, 'Picture here')
    '''
    Testing if the URL is saved
    '''
    def test_Link_url(self):
        link = Links()
        link.url = 'URL Here'
        self.assertEqual(link.url, 'URL Here')
    '''
    Testing whether the title of the recipe is saved
    '''
    def test_Link_title(self):
        link = Links()
        link.title = 'Ham sandwhich'
        self.assertEqual(link.title, 'Ham sandwhich')
    '''
    Testing whether the picture is
    '''
    def test_Link_img(self):
        link = Links()
        link.img = 'Picture here'
        self.assertEqual(link.img, 'Picture here')
    '''
    Testing whether the link shows the instructions
    '''
    def test_Link_instructions(self):
        link = Links()
        link.instructions = 'Get a Ham'
        self.assertEqual(link.instructions, 'Get a Ham')
    '''
    Testing whether the amount of links is saved
    '''
    def test_Link_count(self):
        link = Links()
        link.count = 1
        self.assertEqual(link.count, 1)
    '''
    Testing whether the food name is saved
    '''
    def test_FoodItem_name(self):
        fooditem = FoodItem()
        fooditem.name = 'Chicken Legs'
        self.assertEqual(fooditem.name, 'Chicken Legs')
    '''
    Testing whether the quantity is saved
    '''
    def test_FoodItem_item(self):
        fooditem = FoodItem()
        fooditem.quantity = '5'
        self.assertEqual(fooditem.quantity, '5')
    '''
    Testing whether the name of the user becomes attached to the food
    '''
    def test_FoodItem_user_name(self):
        fooditem = FoodItem()
        fooditem.user_name = 'test54'
        self.assertEqual(fooditem.user_name, 'test54')
    '''
    Testing whether the name is saved
    '''
    def test_Food_name(self):
        food = Food()
        food.name = 'Hotdog'
        self.assertEqual(food.name, 'Hotdog')
    '''
    Testing whether the quantity is saved
    '''
    def test_Food_name(self):
        food = Food()
        food.quantity = '200'
        self.assertEqual(food.quantity, '200')







