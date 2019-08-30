from django.conf.urls import url
from django.urls import path, re_path, include
from .views import all_products, product_detail, product_by_cat

urlpatterns = [
    path('all_products/', all_products, name='products'),
    re_path(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
    re_path(r'^list/$', all_products, name='product_filter'),
    # re_path(r'^category/(?P<category>\w+)/$', all_products, name='cat_filter'),
    re_path(r'^(?P<category_name>[-\w]+)/$', product_by_cat, name='products'),
]
