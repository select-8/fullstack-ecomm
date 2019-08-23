from django.conf.urls import url
from django.urls import path, include
from .views import all_products

urlpatterns = [
    path('all_products/', all_products, name='products')
]
