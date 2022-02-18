from django.shortcuts import render
from .models import ProductCategory, Product


def index(request):
    categories = ProductCategory.objects.all()
    return render(request, 'main/index.html', {'categories': categories})


def category(request, category_id):
    categories = ProductCategory.objects.get(id=category_id)
    products = Product.objects.all()
    return render(request, 'main/product_list.html', {'products': products, 'categories': categories})


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'main/product.html', {'product': product})
