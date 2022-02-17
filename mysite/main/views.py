from django.shortcuts import render
from .models import ProductCategory, Product


def index(request):
    topics = ProductCategory.objects.all()
    return render(request, 'main/index.html', {'topics': topics})


def topic(request, topic_id):
    topic = ProductCategory.objects.get(id=topic_id)
    products = Product.objects.all()
    return render(request, 'main/product_list.html', {'products': products, 'topic': topic})


def product(request, topic_id, product_id):
    topic = Product.objects.get(id=topic_id).category.id
    product = Product.objects.get(id=product_id).id
    products = Product.objects.all()
    return render(request, 'main/product.html', {'products': products, 'topic': topic, 'product': product})
