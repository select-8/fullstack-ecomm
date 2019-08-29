from django.conf.urls import url, re_path
from .views import view_cart, add_to_cart, adjust_cart, remove_from_cart

urlpatterns = [
    re_path(r'^$', view_cart, name='view_cart'),
    re_path(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    re_path(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
    re_path(r'^remove/(\d+)$', remove_from_cart, name='remove_from_cart'),
    ]