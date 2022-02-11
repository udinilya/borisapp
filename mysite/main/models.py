from django.db import models


class ProductCategory(models.Model):
    title = models.CharField('имя категории', max_length=15)
    category_id = models.IntegerField('id категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория продуктов'
        verbose_name_plural = 'Категории продуктов'
