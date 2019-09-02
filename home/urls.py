from django.urls import path
from .views import top_products

urlpatterns = [
    path(r'^$', top_products, name='home'),
]