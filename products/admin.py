from django.contrib import admin
from .models import Product, Category, Kind

# Register your models here.
admin.site.register(Category)
admin.site.register(Kind)
admin.site.register(Product)