from django.conf.urls import url
from django.urls import path, re_path, include
from .views import all_products, product_detail

urlpatterns = [
    path('all_products/', all_products, name='products'),
    re_path(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
]
