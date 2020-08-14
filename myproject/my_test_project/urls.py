"""my_test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home1'),
    path('inventory', views.inventory, name='inven'),
    path('aboutUs', views.aboutUsPage, name='about'),
    path('popularRecipes', views.popularRecipesPage, name='popular'),
    path('login', views.login_auth, name='logs'),
    path('index', views.homepage, name='home2'),
    path('userP1', views.getRecipe, name='user'),
    path('index2', views.ind2Page, name='inde2'),
    path('signup', views.signup, name='sign1'),
    path('signUp', views.signUp, name='sign2'),
    path('recipe', views.recipePage, name='reci'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

