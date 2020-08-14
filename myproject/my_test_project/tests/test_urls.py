from django.test import SimpleTestCase, Client, TestCase
from django.urls import reverse, resolve
from django.http import HttpRequest
from django.contrib.auth.models import User
class TestUrls(SimpleTestCase):
    '''
    We want to see if an unlogged user is redirected when trying to access inventory
    '''
    def test_inventory_url(self):
        response = self.client.get(reverse('inven'))
        self.assertEqual(response.status_code, 302)
    '''
    Testing if home2 is accessible
    '''
    def test_home2_url(self):
        response = self.client.get(reverse('home2'))
        self.assertEqual(response.status_code, 200)
    '''
    Testing if about us is accessible
    '''
    def test_aboutus_url(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
    '''
    Testing if the search recipes page is accessible
    '''
    def test_popularRecipes_url(self):
        response = self.client.get(reverse('popular'))
        self.assertEqual(response.status_code, 200)
    '''
    Testing if the login page is accessible
    '''
    def test_login_url(self):
        response = self.client.get(reverse('logs'))
        self.assertEqual(response.status_code, 200)
    '''
    Testing if home1 is accessible
    '''
    def test_home1_url(self):
        response = self.client.get(reverse('home1'))
        self.assertEqual(response.status_code, 200)
    '''
    Testing if the user profile is unaccessible for an unlogged user
    '''
    def test_userP1_url(self):
        response = self.client.get(reverse('user'))
        self.assertEqual(response.status_code, 302)
    '''
    Testing if home1 is accessible by user
    '''
    def test_home1_url(self):
        response = self.client.get(reverse('home1'))
        self.assertEqual(response.status_code, 200)
    '''
    Testing if the signup page is accessible by user
    '''
    def test_signUp_url(self):
        response = self.client.get(reverse('sign2'))
        self.assertEqual(response.status_code, 200)
    '''
    Testing if the add recipe is unaccessible by an unlogged user
    '''
    def test_reci_url(self):
        response = self.client.get(reverse('reci'))
        self.assertEqual(response.status_code, 302)


class LoggedinTestUrls(TestCase):
    '''
    Testing if page is accessible with a logged in user
    '''
    def test_inventory_login_url(self):
        user = User.objects.create(username='test57')
        user.set_password('1234567*')
        user.save()
        self.client.login(username='test57', password='1234567*')
        response = self.client.get(reverse('inven'))
        self.assertEqual(response.status_code, 200)

    '''
    Testing if the page is accessible with a logged in user
    '''
    def test_userP1_login_url(self):
        user = User.objects.create(username='test57')
        user.set_password('1234567*')
        user.save()
        self.client.login(username='test57', password='1234567*')
        response = self.client.get(reverse('user'))
        self.assertEqual(response.status_code, 200)

    '''
    Testing if the page is accessible for a logged in user
    '''
    def test_recipe_login_url(self):
        user = User.objects.create(username='test57')
        user.set_password('1234567*')
        user.save()
        self.client.login(username='test57', password='1234567*')
        response = self.client.get(reverse('reci'))
        self.assertEqual(response.status_code, 200)

