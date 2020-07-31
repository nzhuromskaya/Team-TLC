from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import userP1form
from django import forms
from .models import Links
import http.client
import urllib.parse
import json
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def homepage(request):
    return render(request, 'index.html')

def signUp(request):
    return render(request, 'signUp.html')

def inventory(request):
    return render(request, 'inventory.html')

def aboutUsPage(request):
    return render(request, 'aboutUs.html')

def popularRecipesPage(request):
    return render(request, 'popularRecipes.html')

def loginPage(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/userP1')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_auth(request):
    #render(request, 'login.html')
    #print('testing!')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/userP1')
    return render(request, 'login.html')

def usPage(request):
    return render(request, 'userP1.html')

def ind2Page(request):
    return render(request, 'index2.html')

def getRecipe(request):
    form = userP1form()
    args = {'form': form}

    link1 = Links()
    link1.img = ''
    link2 = Links()
    link3 = Links()
    link4 = Links()
    link5 = Links()

    links = [link1, link2, link3, link4, link5]

    if request.method == "POST":

        form = userP1form(request.POST)
        if form.is_valid():
            text = form.cleaned_data['content']

            conn = http.client.HTTPSConnection("spoonacular-recipe-food-nutrition-v1.p.rapidapi.com")


            headers = {
                'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                'x-rapidapi-key': "d4ace78f44msh2dbd22f00887354p143b3fjsn0ad1dbb9ca73"
            }

            q = urllib.parse.quote(text)

    #First API
            conn.request("GET", "/recipes/findByIngredients?number=5&ranking=1&ignorePantry=false&ingredients=" + q, headers=headers)

            res = conn.getresponse()
            data = res.read()
            d = data.decode("utf-8")

            res = json.loads(d)
            s = ''

    #Getting id list from the first API
            for i, x in enumerate(res):
                if i:
                    s += ','
                for key, value in x.items():
                    if key == 'id':
                        s += str(value)

            print(s + '\n')

    #Second API
            u = urllib.parse.quote(s)

            conn.request("GET", "/recipes/informationBulk?ids=" + u, headers=headers)

            res = conn.getresponse()
            data = res.read()
            d = data.decode("utf-8")

            res = json.loads(d)
            s = ''
           # seperated=''
           # instruct=''
           # temp=''
            counter = 0

            for i in res:
                for key, value in i.items():
                    '''
                    if key == 'title':
                        s += 'Name: ' + str(value) + '\n'
                    elif key == 'instructions':
                        s += 'Instructions: \n'
                        count = 1
                        temp='' 
                        instruct = str(value)
                        instructions = instruct.split(".")
                        for seperated in instructions:
                            #print(seperated)
                            if seperated != "":
                                temp += "\t\t" + str(count) + ". " + seperated + '.\n'
                                count += 1
                        s += temp + '\n'
                    elif key == 'image':
                        s += 'Image: ' + str(value) + '\n' 
                    '''
                    if key == 'image':
                        s += str(value)
                        links[counter].img = str(value)
                    elif key == 'sourceUrl':
                        links[counter].url = str(value)

                        
                if(counter == 4):
                    break
                else:
                    counter = counter + 1

            text = s
            #args = {'form': form, 'text': text}
            args = {'form': form, 'links': links}
    return render(request, 'userP1.html', args)
