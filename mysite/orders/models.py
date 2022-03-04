from django.db import models


class Order(models.Model):
    first_name = models.CharField('имя', max_length=50)
    last_name = models.CharField('фамилия', max_length=50)
    email = models.EmailField()
    address = models.CharField('адрес', max_length=250)
    postal_code = models.CharField('индекс', max_length=20)
    city = models.CharField('город', max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('main.Product', on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('количество', default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
