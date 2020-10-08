from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost_per_item', 'stock_quantity', 'volume']


admin.site.register(Product, ProductAdmin)