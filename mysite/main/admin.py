from django.contrib import admin
from .models import ProductCategory, Product, ProductImage

admin.site.register(ProductCategory)


class ProductImageAdmin(admin.ModelAdmin):
    pass


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 10
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Product, ProductAdmin)
