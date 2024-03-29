from django.shortcuts import render
import os
import json
from .models import Product
# Create your views here.


JSON_PATH = 'mainapp/json'


def loadMenuFromJSON():
    with open(os.path.join(JSON_PATH, 'menu.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


def main(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu, 'username': 'Гость'}
    return render(request, 'mainapp/main.html', context)


def products(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu, 'products': Product.objects.all()}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu}
    return render(request, 'mainapp/contacts.html', context)
