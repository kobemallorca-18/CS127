from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def home(request):
    return render(request, 'main_website_app/home.html')

def products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'main_website_app/products.html', context)

def product(request):
    return render(request, 'main_website_app/product.html')

def products_plants(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'main_website_app/products.html', context)

def products_gardeningtools(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'main_website_app/products.html', context)


def about(request):
    return render(request, 'main_website_app/about.html')

def contact(request):
    return render(request, 'main_website_app/contact.html')

def register(request):
    return render(request, 'main_website_app/register.html')
