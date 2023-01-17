from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Home page')

def products(request):
    return HttpResponse('products')

def customer(request):
    return HttpResponse('customer')

def contact(request):
    return HttpResponse('Contact page')