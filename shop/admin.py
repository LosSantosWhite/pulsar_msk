from django.contrib import admin

from shop.models import Product


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    pass
