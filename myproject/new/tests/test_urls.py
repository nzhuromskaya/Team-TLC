from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.http import HttpRequest

class TestUrls(SimpleTestCase):

    def test_inventory_url(self):
        response = self.client.get(reverse('inven'))
        self.assertEqual(response.status_code, 302)

    def test_home_url(self):
        response = self.client.get(reverse('home2'))
        self.assertEqual(response.status_code, 200)


