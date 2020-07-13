from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def inventory(request):
    return render(request, 'inventory.html')

def aboutUsPage(request):
    return render(request, 'aboutUs.html')

def popularRecipesPage(request):
    return render(request, 'popularRecipes.html')

def loginPage(request):
    return render(request, 'login.html')

def usPage(request):
    return render(request, 'userP1.html')

def ind2Page(request):
    return render(request, 'index2.html')
