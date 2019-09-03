from django.conf.urls import url
from django.urls import path, re_path, include
from .views import all_products, product_detail, product_by_cat
from reviews.views import add_a_review

urlpatterns = [
    path('all_products/', all_products, name='products'),
    re_path(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
    re_path(r'^list/$', product_by_cat, name='product_filter'),
    re_path(r'^(?P<category_name>[-\w]+)/$', product_by_cat, name='products'),
    path('products/<int:pk>/review/', add_a_review, name='add_a_review'),
]
