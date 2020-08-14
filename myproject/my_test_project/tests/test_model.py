from my_test_project.models import Links, FoodItem, Food
from django.test import TestCase

class test_Models(TestCase):

    def test_Link_img(self):
        link = Links()
        link.img = 'Picture here'
        self.assertEqual(link.img, 'Picture here')

    def test_Link_url(self):
        link = Links()
        link.url = 'URL Here'
        self.assertEqual(link.url, 'URL Here')

    def test_Link_title(self):
        link = Links()
        link.title = 'Ham sandwhich'
        self.assertEqual(link.title, 'Ham sandwhich')
    
    def test_Link_img(self):
        link = Links()
        link.img = 'Picture here'
        self.assertEqual(link.img, 'Picture here')

    def test_Link_instructions(self):
        link = Links()
        link.instructions = 'Get a Ham'
        self.assertEqual(link.instructions, 'Get a Ham')

    def test_Link_count(self):
        link = Links()
        link.count = 1
        self.assertEqual(link.count, 1)

    def test_FoodItem_name(self):
        fooditem = FoodItem()
        fooditem.name = 'Chicken Legs'
        self.assertEqual(fooditem.name, 'Chicken Legs')

    def test_FoodItem_item(self):
        fooditem = FoodItem()
        fooditem.quantity = '5'
        self.assertEqual(fooditem.quantity, '5')

    def test_FoodItem_user_name(self):
        fooditem = FoodItem()
        fooditem.user_name = 'test54'
        self.assertEqual(fooditem.user_name, 'test54')

    def test_Food_name(self):
        food = Food()
        food.name = 'Hotdog'
        self.assertEqual(food.name, 'Hotdog')

    def test_Food_name(self):
        food = Food()
        food.quantity = '200'
        self.assertEqual(food.quantity, '200')







