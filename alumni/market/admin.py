from django.contrib import admin
from market.models import Product
from login.models import CustomUser

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass