from django.db import models


class ProductCategory(models.Model):
    title = models.CharField('имя категории', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория продуктов'
        verbose_name_plural = 'Категории продуктов'


class Product(models.Model):
    title = models.CharField('имя продукта', max_length=30)
    category = models.CharField('категория', max_length=30, null=True)
    price = models.FloatField('цена')
    description = models.TextField('описание', max_length=300)
    image = models.ImageField('изображение', upload_to='image/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
