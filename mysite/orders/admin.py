from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'created', 'paid',
                    ]
    list_filter = ['paid', 'created']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
