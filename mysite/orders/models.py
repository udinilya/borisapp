from django.db import models
from mysite.main.models import Product


class Order(models.Model):
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return 'Order {}'.format(self.id)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('количество', default=1)

    def __str__(self):
        return '{}'.format(self.id)
