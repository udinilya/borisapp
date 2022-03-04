from django.shortcuts import render, get_object_or_404
from .models import OrderItem
from .forms import OrderCreateForm


def order_create(request):
    product = get_object_or_404(OrderItem.product)
    form = OrderCreateForm(request)
    if form.is_valid():
        order = form.save()
