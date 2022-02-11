from django.shortcuts import render
from .models import ProductCategory


def index(request):
    product_category = ProductCategory.objects.all()
    return render(request, 'main/index.html', {'product_category': product_category})


def tshirt(request):
    return render(request, 'main/tshirt.html')
