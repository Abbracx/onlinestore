from django.contrib import admin

from .models import Manufacturer, Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass
