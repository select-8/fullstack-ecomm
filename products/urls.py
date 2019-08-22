from django.conf.urls import url, re_path, include
from .views import all_products

urlpatterns = [
    re_path(r'^$', all_products, name='products')
]