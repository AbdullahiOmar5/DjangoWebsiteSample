from django.shortcuts import render
from django.http import HttpResponse
from .models import Product



def say_hello(request):
    products = Product.objects.all()
    return render(request, "index.html",
                    {"products":products})