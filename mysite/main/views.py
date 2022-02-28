from django.shortcuts import render
from .models import ProductCategory, Product, ProductImage


def index(request):
    categories = ProductCategory.objects.all()
    return render(request, 'main/index.html', {'categories': categories})


def category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    return render(request, 'main/product_list.html', {'products': products})


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    images = ProductImage.objects.filter(product_id=product_id)
    return render(request, 'main/product.html', {'product': product, 'images': images})
